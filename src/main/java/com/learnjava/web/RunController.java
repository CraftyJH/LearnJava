package com.learnjava.web;

import com.learnjava.dto.RunRequest;
import com.learnjava.dto.RunResponse;
import com.learnjava.service.JavaCompileRunService;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
public class RunController {

    private final JavaCompileRunService compileRunService;

    public RunController(JavaCompileRunService compileRunService) {
        this.compileRunService = compileRunService;
    }

    @PostMapping(value = "/run", consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.APPLICATION_JSON_VALUE)
    @CrossOrigin(origins = "*")
    public RunResponse run(@RequestBody RunRequest request) {
        return compileRunService.compileAndRun(request.code(), request.className(), request.timeoutSeconds());
    }
}
