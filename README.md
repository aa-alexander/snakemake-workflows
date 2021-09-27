#snakemake-workflows

Snakemake is a python based workflow management system. Here you can find different snakemake files to perform some basic analysis. 
Install miniconda and use conda environment to install snakemake and other tools in one specific environment. After installing conda, the command to create a environment is
**`conda create -n snakemake-environment`**
**`conda activate snakemake-environment`**

Next install snakemake in this environment using the command, **`conda  -c conda-forge -c bioconda -n snakemake -y`**

To know more about snakemake : https://snakemake.readthedocs.io/en/stable/index.html

snakemake citation: 
*Mölder, F., Jablonski, K.P., Letcher, B., Hall, M.B., Tomkins-Tinch, C.H., Sochat, V., Forster, J., Lee, S., Twardziok, S.O., Kanitz, A., Wilm, A., Holtgrewe, M., Rahmann, S., Nahnsen, S., Köster, J., 2021. Sustainable data analysis with Snakemake. F1000Res 10, 33.*

All my snakemake files will be written as **"filename.py"** file. So while running snakemake "-s" parameter is given. Therefore the command line execution will look like - **`snakemake -j 1 -s filename.py`**


##FastQC-snakemake workflow

This workflow performs fastqc for all the fastq files in your input path directory and output the results in the output path directory. 

Before starting the worflow make sure you are in the snakemake-environment. Also, make sure you have installed fastQC in this environment. If not installed, install fastqc using -- **`conda install -c bioconda fastqc`**

Run the workflow using the command in your terminal -- **`snakemake -j 1 -s fastqcRules.py`**

