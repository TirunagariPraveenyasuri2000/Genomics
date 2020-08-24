import Bio
from Bio.Blast import NCBIWWW
fasta_string='TGGGCCTCATATTTATCCTATATACCATGTTCGTATGGTGGCGCGATGTTCTACGTGAATCCACGTTCGAAGGACATCATACCAAAGTCGTACAATTAGGACCTCGATATGGTTTTATTCTGTTTATCGTATCGGAGGTTATGTTCTTTTTTGCTCTTTTTCGGGCTTCTTCTCATTCTTCTTTGGCACCTACGGTAGAG'
result_handle=NCBIWWW.qblast("blastn","nt",fasta_string)
from Bio.Blast import NCBIXML
blast_record=NCBIXML.read(result_handle)
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        print("***Alignment***")
        print('sequence:',alignment.title)
        print('e_value:',hsp.expect)
