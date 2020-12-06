def rna(dna):
    return dna.replace('T','U')
    
f=open("rosalind_rna.txt","r")
dna=f.readline()
f.close()
nf=open("output_rna.txt","w")
nf.write(rna(dna))
nf.close()