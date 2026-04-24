/* global monaco, marked */

const API = "";

let curriculum = null;
let currentSection = null;
let currentLesson = null;
let editor = null;
let expandedSections = new Set();

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
        const b = el(
          "button",
          {
            type: "button",
            className: lesson.id === currentLesson?.id ? "active" : "",
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
    document.getElementById("classNameInput").value = ch.className || "Main";
    editor?.setValue(ch.starterCode || "");
    document.getElementById("editorStatus").textContent = "";
  } else {
    cp.classList.add("hidden");
  }

  if (!sec.projectsAtEnd) {
    renderProjects(sec);
  } else {
    updateProjectsVisibility(sec, lesson);
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
  } catch (e) {
    document.getElementById("stderr").textContent = String(e);
    document.getElementById("stdout").textContent = "";
    document.getElementById("editorStatus").textContent = "Error";
  } finally {
    runBtn.disabled = false;
  }
}

function resetStarter() {
  if (currentLesson?.challenge?.starterCode != null) {
    editor?.setValue(currentLesson.challenge.starterCode);
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
      resolve();
    });
  });
}

async function boot() {
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

boot().catch((e) => {
  document.getElementById("theoryContent").textContent = "Startup error: " + e;
});
