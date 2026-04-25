package com.learnjava.web;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.core.io.ClassPathResource;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;

@RestController
@RequestMapping("/api")
public class CurriculumController {

    private final ObjectMapper objectMapper;

    public CurriculumController(ObjectMapper objectMapper) {
        this.objectMapper = objectMapper;
    }

    @GetMapping(value = "/curriculum", produces = MediaType.APPLICATION_JSON_VALUE)
    public JsonNode curriculum() throws IOException {
        try (InputStream in = new ClassPathResource("static/data/curriculum.json").getInputStream()) {
            return objectMapper.readTree(in);
        }
    }

    @GetMapping(value = "/lesson", produces = MediaType.TEXT_PLAIN_VALUE, params = "path")
    public String lesson(String path) throws IOException {
        if (path == null || path.isBlank()) {
            return "";
        }
        String normalized = path.replace("..", "").replace('\\', '/');
        if (normalized.startsWith("/")) {
            normalized = normalized.substring(1);
        }
        if (!normalized.startsWith("lessons/") || !normalized.endsWith(".md")) {
            throw new IllegalArgumentException("Invalid lesson path");
        }
        ClassPathResource resource = new ClassPathResource("static/" + normalized);
        if (!resource.exists()) {
            throw new IllegalArgumentException("Lesson not found");
        }
        return new String(resource.getInputStream().readAllBytes(), StandardCharsets.UTF_8);
    }
}
