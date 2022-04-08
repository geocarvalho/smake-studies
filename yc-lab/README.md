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

## 4. []()