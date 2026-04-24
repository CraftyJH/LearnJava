package com.learnjava.dto;

public record RunRequest(String code, String className, int timeoutSeconds) {

    public RunRequest(String code, String className, int timeoutSeconds) {
        this.code = code;
        if (className == null || className.isBlank()) {
            this.className = "Main";
        } else {
            this.className = className.trim();
        }
        if (timeoutSeconds <= 0 || timeoutSeconds > 30) {
            this.timeoutSeconds = 10;
        } else {
            this.timeoutSeconds = timeoutSeconds;
        }
    }
}
