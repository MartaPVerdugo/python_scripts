#!/usr/bin/env python

"""
align2filter.py
Date: 27.4.2017
Adapted from Victoria Mullin by Marta Verdugo
Script to go from aligned sai files to rmdup.bam

"""

## import statements
import os
import sys

# get folder
cwd = os.getcwd()

# make data list
data_list = []
sys.stderr.write("made empty list\n")



def main(config_file_name):
    """Main Entry Point"""
    sys.stderr.write("about to parse\n")
    sys.stderr.write("Samples for analysis are....\n")
    for line in open(config_file_name):
        if not line.startswith('#'):
            line = parse_line(line)
            data_list.append(line)
            sys.stderr.write((line["sai_file"])+"\n")


    for line in data_list:
        sys.stderr.write("reading sai name \n")
        sys.stderr.write((line["sai_file"])+"\n")
        ##os.mkdir(line["file_name"])

        sys.stderr.write('\n\n')
        sys.stderr.write("Starting analysis \n")



        ## Add read groups, convert sai to sam

        cmd = "bwa samse -r '{r}' {g} {s} {n}_trimmed.fastq > {f}_align.sam".format(s=line['sai_file'], r=line['read_groups'], g=line['genome'], n=line['name'], f=line['final_name'])
        os.system(cmd)

        ## Samtools
        cmd = 'samtools view -Sb {f}_align.sam > {f}_align.bam'.format(f=line['final_name'])
        os.system(cmd)
        cmd = 'samtools sort {f}_align.bam {f}_align_sort'.format(f=line['final_name'])
        os.system(cmd)
        cmd = 'samtools rmdup -s {f}_align_sort.bam {f}_align_sort_rmdup.bam'.format(f=line['final_name'])
        os.system(cmd)
        cmd = 'samtools flagstat {f}_align.bam >> {f}_flagstat.log'.format(f=line['final_name'])
        os.system(cmd)
        cmd = 'samtools flagstat {f}_align_sort_rmdup.bam >> {f}_flagstat.log'.format(f=line['final_name'])
        os.system(cmd)



    sys.stderr.write("DONE \n")

def parse_line(line):

    columns = line.strip().split(",")

    # Read the file
    sai_file = columns[0]
    read_groups = columns[1]
    genome = columns[2]
    name = columns[3]
    final_name= columns[4]


    line_info = {
        "line" : line,
        "columns" : columns,
        "sai_file" : columns[0],
        "read_groups" : columns[1],
        "genome" : columns[2],
        "name" : columns[3],
        "final_name" : columns[4]
    }
    return(line_info)

main(sys.argv[1])
