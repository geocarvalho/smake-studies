rule hello:
    output: "{prefix}.txt"
    shell:
        "echo hello\tworld > {output}"