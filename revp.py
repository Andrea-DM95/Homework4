def revc(dna):
    r_dna=dna[::-1]
    old="ATGC"
    new="TACG"
    table=r_dna.maketrans(old,new)
    return r_dna.translate(table)

def revp(dna):
    pair=[]
    for i in range(len(dna)-3):
        for l in range(4,13):
            while i+l<= len(dna):
                c=dna[i:i+l]
                if c==revc(c):
                    pair.append([i+1,l])
                break
    return pair

dna=''
f=open("rosalind_revp.txt","r")
id=f.readline()
for line in f:
    dna+=line.strip()
f.close()
print(dna)
nf=open("output_revp.txt","w")
for e in revp(dna):
    nf.write("{} {}\n".format(*e))
nf.close()