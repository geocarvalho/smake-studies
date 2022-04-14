rule world:
    output: "world.txt"
    shell: "echo world > {output}"