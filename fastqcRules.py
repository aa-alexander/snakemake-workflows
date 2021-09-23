#this is a snakemake file to perform fastqc for all the srr in a directory
import glob
import os

inputPath =      #path to your raw reads
finalPath =      #path to your output directory
threads =        #number of threads

SRR, FR = glob.glob("{srr}_{fr}.fastq") 

rule end:
	input:
		report = expand(finalPath + "/QCreport/multiQCreport.html", srr = SRR, fr = FR)
		
rule fastQC:
	input:
		rawRead = inputPath + "/{srr}_{fr}.fastq*"

	output:
		fastQC_read = finalPath + "/QCreport/{srr}_{fr}_fastqc.html"
		
	params:
		outPath = finalPath + "/QCreport"
    threads = threads
    
	shell:
		"fastqc -t {params.threads} -o {params.outPath} {input.rawRead1} "
	
rule multiQC:
	input:
		fastqc = rules.fastQC.output.fastQC_read
    
	output:
		multiQCreport = finalPath + "/QCreport/multiQCreport.html"
    
	params:
		path = finalPath + "/QCreport"
    
	shell:
		"multiqc {params.path} --filename {output.multiQCreport}"
