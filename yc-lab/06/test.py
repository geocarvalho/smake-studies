import sys

with open("hello.txt", "w") as f:
    f.write(sys.version)
    f.write("\n")