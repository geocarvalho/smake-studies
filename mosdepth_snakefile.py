import glob
import os

bam_lst = glob.glob("./bams/*bam")
samples = [os.path.basename(bam).split(".")[0] for bam in bam_lst]

rule all:
    input:
        expand("{filename}_variants.per-base.bed.gz", filename=samples)

rule mosdepth_target:
    input:
        bam = "bams/{filename}.sorted.bam",
        bed = "beds/sars-cov-2_variants.bed"
    output:
        regions = "{filename}_variants.per-base.bed.gz"
    singularity:
        "quay.io/biocontainers/mosdepth:0.2.4--he527e40_0 mosdepth"
    shell:
        """ mosdepth --by {input.bed} {wildcards.filename}_variants --fast-mode -T 1,10,50,100,500,1000,2000,3000,5000 {input.bam}
        """
# docker run -v $(pwd):/data quay.io/biocontainers/mosdepth:0.2.4--he527e40_0 mosdepth --by /data/beds/sars-cov-2_variants.bed /data/variants/{sample_n}/{sample_n}_variants --fast-mode -T 1,10,50,100,500,1000,2000,3000,5000 /data/bams/{sample_n}.sorted.bam
