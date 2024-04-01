# DNA Toolset/Code testing file
from PythonDNAToolkit import *
import random 

#creating a random DNA seq for testing:
rndDNAstr = ''. join([random.choice(Nucleotides)
                      for nuc in range(50)])

DNAStr = validateSeq(rndDNAstr)
print(validateSeq(rndDNAstr))
print(countNucFrequency(DNAStr))