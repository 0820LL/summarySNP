#!python
#author: lilin
#date: 2014-09-22

import argparse

def deter_type(snp_DN):
    if len(snp_DN) == 2:
        if int(snp_DN[0].strip()) == 0 or int(snp_DN[1].strip()) == 0:
            return 'homo'
        if int(snp_DN[0].strip()) != 0 or int(snp_DN[1].strip()) != 0:
            return 'hete'

def summarize_snp(snpFile):
    (DN_homo,DN_hete) = (0,0)
    (HF_homo,HF_hete) = (0,0)
    (HN_homo,HN_hete) = (0,0)
    (NF_homo,NF_hete) = (0,0)
    (Y1_homo,Y1_hete) = (0,0)
    (Y2_homo,Y2_hete) = (0,0)
    (Y3_homo,Y3_hete) = (0,0)
    (Y4_homo,Y4_hete) = (0,0)
    infile = open(snpFile,'r')
    for line in infile:
        if line[0] == '#':
            continue
        snp_DN = line.split('\t')[4].split(',')
        snp_type = deter_type(snp_DN)
        if snp_type == 'homo':
            DN_homo += 1
        if snp_type == 'hete':
            DN_hete += 1
        snp_HF = line.split('\t')[5].split(',')
        snp_type = deter_type(snp_HF)
        if snp_type == 'homo':
            HF_homo += 1
        if snp_type == 'hete':
            HF_hete += 1
        snp_HN = line.split('\t')[6].split(',') 
        snp_type = deter_type(snp_HN)
        if snp_type == 'homo':
            HN_homo += 1
        if snp_type == 'hete':
            HN_hete += 1
        snp_NF = line.split('\t')[7].split(',')
        snp_type = deter_type(snp_NF)
        if snp_type == 'homo':
            NF_homo += 1
        if snp_type == 'hete':
            NF_hete += 1
        snp_Y1 = line.split('\t')[8].split(',')
        snp_type = deter_type(snp_Y1)
        if snp_type == 'homo':
            Y1_homo += 1
        if snp_type == 'hete':
            Y1_hete += 1
        snp_Y2 = line.split('\t')[9].split(',')
        snp_type = deter_type(snp_Y2)
        if snp_type == 'homo':
            Y2_homo += 1
        if snp_type == 'hete':
            Y2_hete += 1
        snp_Y3 = line.split('\t')[10].split(',')
        snp_type = deter_type(snp_Y3)
        if snp_type == 'homo':
            Y3_homo += 1
        if snp_type == 'hete':
            Y3_hete += 1
        snp_Y4 = line.split('\t')[11].split(',')
        snp_type = deter_type(snp_Y4)
        if snp_type == 'homo':
            Y4_homo += 1
        if snp_type == 'hete':
            Y4_hete += 1
    infile.close()
    total_homo = DN_homo+HF_homo+HN_homo+NF_homo+Y1_homo+Y2_homo+Y3_homo+Y4_homo
    total_hete = DN_hete+HF_hete+HN_hete+NF_hete+Y1_hete+Y2_hete+Y3_hete+Y4_hete
    outfile = open('summarize_result.txt','w')
    outfile.write("\tDN\tHF\tHN\tNF\tY1\tY2\tY3\tY4\ttotal\n")
    outfile.write("homozygosis\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" %(DN_homo,HF_homo,HN_homo,NF_homo,Y1_homo,Y2_homo,Y3_homo,Y4_homo,total_homo))
    outfile.write("heterozygosis\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" %(DN_hete,HF_hete,HN_hete,NF_hete,Y1_hete,Y2_hete,Y3_hete,Y4_hete,total_hete))
    outfile.write("total\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" %(DN_homo+DN_hete,HF_homo+HF_hete,HF_homo+HN_hete,NF_homo+NF_hete,Y1_homo+Y1_hete,Y2_homo+Y2_hete,Y3_homo+Y3_hete,Y4_homo+Y4_hete,total_homo+total_hete))
    outfile.close()
def parser_argument():
    parser = argparse.ArgumentParser(description="summarize the SNP with homozygosis and heterozygosis.")
    parser.add_argument('--snp',help="the file SNPs.xls",required=True)
    argv = vars(parser.parse_args())
    snpFile = argv['snp'].strip()
    return snpFile

def main():
    snpFile = parser_argument()
    summarize_snp(snpFile)
    
if __name__ == '__main__':
    main()
