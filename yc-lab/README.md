# YC lab - snakemake workshop
## 1. [Writting your first Snakefile](https://youtu.be/Gg0SsEs16Jc)
```
$ snakemake --cores 1 hello.bello.tsv
```

## 2. [How snakemake finds your Snakefile](https://youtu.be/J73GCLsadrI)
```
# Run the Snake file inside workflow
$ snakemake --cores 1 hello.bello.tsv
# Run a specific snakefile
$ snakemake --cores 1 --snakefile my_snakefile.smk hi.txt
```

## 3. [Using configfile in your snakemake pipeline](https://youtu.be/Bdxh0fSBOSA)
```
$ snakemake -c 1 output.csv
```

## 4. [Including external snakefiles, modularization](https://youtu.be/EEhmR5bQUG4)
```
$ snakemake -c 1 world.txt
```

## 5. [Importance of the first rule in your snakefile](https://youtu.be/QieqgX9nPfQ)
```
$ snakemake -c 1
```

## 6. [ Using Snakemake with Singularity for creating reproducible pipelines](https://youtu.be/ty2OoCHlWb4)
```
$ snakemake -c 1 --use-singularity
$ singularity pull docker://python:3.11.0a5-bullseye
```

## 7. [Using the "batch" argument to run your workflow in chunks](https://youtu.be/TlXIpd4OGZw)
```
$ snakemake -c 1 --debug-dag
$ snakemake -c 1 --batch all=1/3
$ snakemake -c 1 --batch all=1/10
```

## 8. [Using wildcards to generalise your workflows and basic trouble shooting](https://youtu.be/bMMTOQ9Ri7k)