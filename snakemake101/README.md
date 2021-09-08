# [Snakemake 101](https://www.youtube.com/watch?v=K9uyA6ATDjM&list=PLm-MsgmJxrTTgTTvU_qrZlyvJQH1lmuI8)

## Parte 1

* [Instale conda no seu sistema](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
* Criando um ambiente conda com snakemake

```
conda create -n snake -c bioconda snakemake -y
conda activate snake
# instale Graphviz and R
conda install -c bioconda graphviz -y
conda install r-essentials
```

## Parte 2

* Criar uma pasta para testarmos novos arquivos

```
mkdir toots
cd toots
touch Snakefile
```

