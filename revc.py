def revc(dna):
    r_dna=dna[::-1]
    old="ATGC"
    new="TACG"
    table=r_dna.maketrans(old,new)
    return r_dna.translate(table)
    
f=open("rosalind_revc.txt","r")
dna=f.readline()
f.close()
nf=open("output_revc.txt","w")
nf.write(revc(dna))
nf.close()    