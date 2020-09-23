#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 10:21:10 2020

@author: mjabeen
"""




 

samfilepath = '/Users/mjabeen/Documents/DPhil_2020/OBDS/obds_wd/ERR1755082.test.sam'
bedfilepath = '/Users/mjabeen/Documents/DPhil_2020/OBDS/obds_wd/ERR1755082.test.bed'

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', dest='samfilepath',
                    help='input file path')
parser.add_argument('--output', '-o', dest='bedfilepath',
                    help='output file path')
args=parser.parse_args()


with open(args.samfilepath, 'r') as samfile: #create file called samfile using the path, r=read
    with open(args.bedfilepath, 'w') as bedfile: #open bedfile at the path and w= write
        for line in samfile:  #do this line by line
            if line[0] == '@': #get rid of header
                pass  #anything else that isnt header can proceed
      
        
        #we want chromosome (col 3)
            else: #do the following for all execpt header, read each line and split as follow
                column = line.split() #parse the line into a list of fields/columns
                chrom = column[2]
            #start pos (col 4, but 0 based)
                startpos = int(column[3]) - 1 #need to convert from 1-based SAM file to 0-based bed file, -1 
            #end pos col 4 +len col 10
                endpos = int(column[3]) + len(column[9])
            #name (col 1)
                name = column[0]
            # score (col 5)
                score = column[4]
            # strand (.)
                strand = '.'
                
                bedfile.write(f'{chrom}\t{startpos}\t{endpos}\t{name}\t{score}\t{strand}\n')