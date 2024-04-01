# DNA Toolkit file
import collections

Nucleotides = ["A", "C", "G", "T"]

# Validate Sequence Function: Chech the seq. to make sure it is a DNA String
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

#counting the freq of nucleotides
def countNucFrequency(seq):
   # tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    #for nuc in seq:
     #   tmpFreqDict[nuc] += 1
    #return tmpFreqDict
    return dict(collections.Counter(seq))
#If you want to reduce it you can import collections and remove the four lines under countNucFrequency(seq)