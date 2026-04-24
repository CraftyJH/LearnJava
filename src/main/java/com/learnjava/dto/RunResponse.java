package com.learnjava.dto;

public record RunResponse(boolean success, String stdout, String stderr, String compileOutput) {
}
