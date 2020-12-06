def subs (dna,search):
    index=[]
    pos=dna.find(search)
    while pos>=0:
        index.append(pos+1)
        pos=dna.find(search,pos+1)
    return " ".join(str(i) for i in index)


    
with open("rosalind_subs.txt", 'r') as f:
    dna=f.readline().strip()
    search=f.readline().strip()
nf=open("output_subs.txt","w")
nf.write(subs(dna,search))
nf.close()