from collections import Counter
def count(dna):
    count=Counter(dna)
    return "{} {} {} {}".format(count['A'],count['C'],count['G'],count['T'])
f=open("rosalind_dna.txt","r")
dna=f.readline()
f.close()
nf=open("output_dna.txt","w")
nf.write(count(dna))
nf.close()
