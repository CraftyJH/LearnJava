/* global monaco, marked */

const API = "";

const STORAGE_KEY = "javaMasteryProgressV1";
const SAVE_DEBOUNCE_MS = 650;

let curriculum = null;
let currentSection = null;
let currentLesson = null;
let editor = null;
let expandedSections = new Set();
let draftSaveTimer = null;

/** @type {{ doneLessons: string[], drafts: Record<string, { code: string, className: string }> }} */
let progress = { doneLessons: [], drafts: {} };

function lessonKey(section, lesson) {
  return `${section.id}::${lesson.id}`;
}

function loadProgress() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) {
      progress = { doneLessons: [], drafts: {} };
      return;
    }
    const o = JSON.parse(raw);
    progress = {
      doneLessons: Array.isArray(o.doneLessons) ? o.doneLessons : [],
      drafts: o.drafts && typeof o.drafts === "object" ? o.drafts : {},
    };
  } catch {
    progress = { doneLessons: [], drafts: {} };
  }
}

function saveProgress() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
  } catch (e) {
    console.warn("Could not save progress", e);
  }
  updateProgressUI();
}

function isLessonDone(section, lesson) {
  return progress.doneLessons.includes(lessonKey(section, lesson));
}

function setLessonDone(section, lesson, done) {
  const key = lessonKey(section, lesson);
  const set = new Set(progress.doneLessons);
  if (done) set.add(key);
  else set.delete(key);
  progress.doneLessons = [...set];
  saveProgress();
  renderSectionNav();
}

function persistDraft(section, lesson) {
  if (!editor || !section || !lesson) return;
  const key = lessonKey(section, lesson);
  progress.drafts[key] = {
    code: editor.getValue(),
    className: document.getElementById("classNameInput").value.trim() || "Main",
  };
  saveProgress();
}

function updateProgressUI() {
  const el = document.getElementById("progressStatus");
  if (!curriculum || !currentSection || !currentLesson) {
    el.textContent = "";
    return;
  }
  const total = curriculum.sections.reduce((n, s) => n + (s.lessons?.length || 0), 0);
  const done = progress.doneLessons.length;
  el.textContent = `${done}/${total} lessons marked done`;
  const markBtn = document.getElementById("markDoneBtn");
  markBtn.textContent = isLessonDone(currentSection, currentLesson) ? "Undo done" : "Mark done";
}

function exportProgress() {
  const blob = new Blob(
    [
      JSON.stringify(
        {
          version: 1,
          exportedAt: new Date().toISOString(),
          doneLessons: progress.doneLessons,
          drafts: progress.drafts,
        },
        null,
        2
      ),
    ],
    { type: "application/json" }
  );
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = `java-mastery-progress-${new Date().toISOString().slice(0, 10)}.json`;
  a.click();
  URL.revokeObjectURL(a.href);
}

function importProgressFile(file) {
  const reader = new FileReader();
  reader.onload = () => {
    try {
      const o = JSON.parse(String(reader.result));
      const incomingDone = Array.isArray(o.doneLessons) ? o.doneLessons : [];
      const incomingDrafts = o.drafts && typeof o.drafts === "object" ? o.drafts : {};
      progress.doneLessons = [...new Set([...progress.doneLessons, ...incomingDone])];
      progress.drafts = { ...progress.drafts, ...incomingDrafts };
      saveProgress();
      applyDraftToEditor();
      renderSectionNav();
      alert("Progress merged from file.");
    } catch (e) {
      alert("Could not import: invalid JSON.");
    }
  };
  reader.readAsText(file);
}

function clearProgress() {
  if (!confirm("Clear all saved progress and drafts in this browser?")) return;
  progress = { doneLessons: [], drafts: {} };
  localStorage.removeItem(STORAGE_KEY);
  updateProgressUI();
  renderSectionNav();
  if (currentLesson?.challenge) {
    editor?.setValue(currentLesson.challenge.starterCode || "");
    document.getElementById("classNameInput").value = currentLesson.challenge.className || "Main";
  }
}

function applyDraftToEditor() {
  if (!currentSection || !currentLesson || !editor) return;
  const key = lessonKey(currentSection, currentLesson);
  const d = progress.drafts[key];
  const ch = currentLesson.challenge;
  if (d?.code) {
    editor.setValue(d.code);
    if (d.className) document.getElementById("classNameInput").value = d.className;
  } else if (ch) {
    editor.setValue(ch.starterCode || "");
    document.getElementById("classNameInput").value = ch.className || "Main";
  }
}

function scrollOutputIntoView() {
  const body = document.querySelector(".output-body");
  if (body) body.scrollTo({ top: 0, behavior: "smooth" });
}

function el(tag, props = {}, children = []) {
  const node = document.createElement(tag);
  Object.assign(node, props);
  for (const c of children) {
    if (typeof c === "string") node.appendChild(document.createTextNode(c));
    else if (c) node.appendChild(c);
  }
  return node;
}

async function fetchCurriculum() {
  const res = await fetch(`${API}/api/curriculum`);
  if (!res.ok) throw new Error("Failed to load curriculum");
  return res.json();
}

async function fetchLesson(path) {
  const res = await fetch(`${API}/api/lesson?path=${encodeURIComponent(path)}`);
  if (!res.ok) throw new Error("Failed to load lesson");
  return res.text();
}

function renderSectionNav() {
  const root = document.getElementById("sectionNav");
  root.innerHTML = "";
  for (const sec of curriculum.sections) {
    const open = expandedSections.has(sec.id);
    const block = el("div", { className: "section-block" });
    const titleBtn = el(
      "button",
      {
        type: "button",
        className: "section-title",
        onclick: () => {
          if (expandedSections.has(sec.id)) expandedSections.delete(sec.id);
          else expandedSections.add(sec.id);
          renderSectionNav();
        },
      },
      [sec.title, el("span", { className: "chev" }, [open ? "▼" : "▶"])]
    );
    block.appendChild(titleBtn);
    if (open) {
      const ul = el("ul", { className: "lesson-list" });
      for (const lesson of sec.lessons) {
        const done = isLessonDone(sec, lesson);
        const cls = [lesson.id === currentLesson?.id && "active", done && "lesson-done"].filter(Boolean).join(" ");
        const b = el(
          "button",
          {
            type: "button",
            className: cls,
            onclick: () => selectLesson(sec, lesson),
          },
          [lesson.title]
        );
        ul.appendChild(el("li", {}, [b]));
      }
      block.appendChild(ul);
    }
    root.appendChild(block);
  }
}

function renderProjects(sec) {
  const panel = document.getElementById("projectsPanel");
  const list = document.getElementById("projectsList");
  list.innerHTML = "";
  const projects = sec.majorProjects || [];
  if (!projects.length) {
    panel.classList.add("hidden");
    return;
  }
  panel.classList.remove("hidden");
  for (const p of projects) {
    const card = el("div", { className: "project-card" });
    card.appendChild(el("h3", {}, [p.title]));
    card.appendChild(el("p", { className: "muted" }, [p.description]));
    if (p.stretchGoals?.length) {
      card.appendChild(el("p", { className: "muted" }, ["Stretch goals:"]));
      card.appendChild(el("ul", {}, p.stretchGoals.map((g) => el("li", {}, [g]))));
    }
    list.appendChild(card);
  }
}

function updateProjectsVisibility(sec, lesson) {
  const lessons = sec.lessons || [];
  const last = lessons[lessons.length - 1];
  const isLast = last && lesson.id === last.id;
  if (sec.projectsAtEnd) {
    if (isLast) renderProjects(sec);
    else document.getElementById("projectsPanel").classList.add("hidden");
  }
}

async function selectLesson(sec, lesson) {
  if (currentSection && currentLesson && editor) {
    persistDraft(currentSection, currentLesson);
  }

  currentSection = sec;
  currentLesson = lesson;
  renderSectionNav();

  document.getElementById("breadcrumb").textContent = `${sec.title} → ${lesson.title}`;

  const theoryEl = document.getElementById("theoryContent");
  theoryEl.innerHTML = "<p class='muted'>Loading theory…</p>";
  try {
    const md = await fetchLesson(lesson.theoryPath);
    theoryEl.innerHTML = marked.parse(md);
  } catch (e) {
    theoryEl.innerHTML = `<p class='muted'>Could not load theory: ${e.message}</p>`;
  }

  const ch = lesson.challenge;
  const cp = document.getElementById("challengePanel");
  if (ch) {
    cp.classList.remove("hidden");
    document.getElementById("challengeInstructions").textContent = ch.instructions;
    const hints = document.getElementById("hintsList");
    hints.innerHTML = "";
    const hb = document.getElementById("hintsBlock");
    if (ch.hints?.length) {
      hb.classList.remove("hidden");
      for (const h of ch.hints) hints.appendChild(el("li", {}, [h]));
    } else {
      hb.classList.add("hidden");
    }
    applyDraftToEditor();
    document.getElementById("editorStatus").textContent = "";
  } else {
    cp.classList.add("hidden");
    if (editor) {
      editor.setValue('public class Main {\n    public static void main(String[] args) {\n    }\n}\n');
      document.getElementById("classNameInput").value = "Main";
    }
  }

  if (!sec.projectsAtEnd) {
    renderProjects(sec);
  } else {
    updateProjectsVisibility(sec, lesson);
  }

  const challengeRow = document.getElementById("ideRowChallenge");
  const chVis = !document.getElementById("challengePanel").classList.contains("hidden");
  const prVis = !document.getElementById("projectsPanel").classList.contains("hidden");
  challengeRow.classList.toggle("ide-row-collapsed", !chVis && !prVis);

  updateProgressUI();
  if (editor) {
    editor.layout();
  }
}

async function runCode() {
  const code = editor?.getValue() ?? "";
  const className = document.getElementById("classNameInput").value.trim() || "Main";
  const runBtn = document.getElementById("runBtn");
  runBtn.disabled = true;
  document.getElementById("editorStatus").textContent = "Compiling…";
  try {
    const res = await fetch(`${API}/api/run`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code, className, timeoutSeconds: 12 }),
    });
    const data = await res.json();
    document.getElementById("stdout").textContent = data.stdout || "";
    document.getElementById("stderr").textContent = data.stderr || "";
    document.getElementById("compileOut").textContent = data.compileOutput || "";
    document.getElementById("compileDetails").open = Boolean(data.compileOutput) && !data.success;
    document.getElementById("editorStatus").textContent = data.success ? "Finished" : "Failed";
    if (currentSection && currentLesson) persistDraft(currentSection, currentLesson);
    scrollOutputIntoView();
  } catch (e) {
    document.getElementById("stderr").textContent = String(e);
    document.getElementById("stdout").textContent = "";
    document.getElementById("editorStatus").textContent = "Error";
    scrollOutputIntoView();
  } finally {
    runBtn.disabled = false;
  }
}

function resetStarter() {
  if (currentLesson?.challenge?.starterCode != null) {
    editor?.setValue(currentLesson.challenge.starterCode);
    document.getElementById("classNameInput").value = currentLesson.challenge.className || "Main";
    if (currentSection && currentLesson) persistDraft(currentSection, currentLesson);
  }
}

function initMonaco() {
  const mount = document.getElementById("editorMount");
  require.config({
    paths: { vs: "https://cdn.jsdelivr.net/npm/monaco-editor@0.45.0/min/vs" },
  });
  return new Promise((resolve) => {
    require(["vs/editor/editor.main"], () => {
      editor = monaco.editor.create(mount, {
        value:
          'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello");\n    }\n}\n',
        language: "java",
        theme: "vs-dark",
        fontSize: 14,
        minimap: { enabled: true },
        automaticLayout: true,
        tabSize: 4,
        scrollBeyondLastLine: false,
      });
      editor.onDidChangeModelContent(() => {
        clearTimeout(draftSaveTimer);
        draftSaveTimer = setTimeout(() => {
          if (currentSection && currentLesson) persistDraft(currentSection, currentLesson);
        }, SAVE_DEBOUNCE_MS);
      });
      document.getElementById("classNameInput").addEventListener("input", () => {
        clearTimeout(draftSaveTimer);
        draftSaveTimer = setTimeout(() => {
          if (currentSection && currentLesson) persistDraft(currentSection, currentLesson);
        }, SAVE_DEBOUNCE_MS);
      });
      resolve();
    });
  });
}

async function boot() {
  loadProgress();
  curriculum = await fetchCurriculum();
  document.getElementById("courseSubtitle").textContent = curriculum.subtitle || "";
  expandedSections = new Set(curriculum.sections.map((s) => s.id));
  const firstSec = curriculum.sections[0];
  const firstLesson = firstSec.lessons[0];
  renderSectionNav();
  await initMonaco();
  await selectLesson(firstSec, firstLesson);
}

document.getElementById("runBtn").addEventListener("click", runCode);
document.getElementById("resetBtn").addEventListener("click", resetStarter);
document.getElementById("clearOutBtn").addEventListener("click", () => {
  document.getElementById("stdout").textContent = "";
  document.getElementById("stderr").textContent = "";
  document.getElementById("compileOut").textContent = "";
});

document.getElementById("markDoneBtn").addEventListener("click", () => {
  if (!currentSection || !currentLesson) return;
  const done = isLessonDone(currentSection, currentLesson);
  setLessonDone(currentSection, currentLesson, !done);
});

document.getElementById("exportProgressBtn").addEventListener("click", exportProgress);
document.getElementById("importProgressInput").addEventListener("change", (ev) => {
  const f = ev.target.files?.[0];
  if (f) importProgressFile(f);
  ev.target.value = "";
});
document.getElementById("clearProgressBtn").addEventListener("click", clearProgress);

window.addEventListener("beforeunload", () => {
  if (currentSection && currentLesson && editor) persistDraft(currentSection, currentLesson);
});

boot().catch((e) => {
  document.getElementById("theoryContent").textContent = "Startup error: " + e;
});
