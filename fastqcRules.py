#this is a snakemake file to perform fastqc for all the srr in a directory

import glob
import os

inputPath = "/path/to/rawReads"    #path to your raw reads
finalPath = "/path/to/output"   #path to your output directory
nthreads = 4       #number of threads

SRR, FR = glob_wildcards(inputPath + "/{srr}_{fr}.fastq") 

rule end:
	input:
		fastqc = expand(finalPath + "/QCreport/{srr}_{fr}_fastqc.html", srr = SRR, fr = FR)
		
rule fastQC:
	input:
		rawRead = inputPath + "/{srr}_{fr}.fastq"

	output:
		fastQC_read = finalPath + "/QCreport/{srr}_{fr}_fastqc.html"
		
	params:
		outPath = finalPath + "/QCreport",
    		threads = nthreads
    
	shell:
		"fastqc -t {params.threads} -o {params.outPath} {input.rawRead} "
	
