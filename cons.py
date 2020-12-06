from collections import Counter
def cons (dna):
    A=[]
    C=[]
    G=[]
    T=[]
    new=['']*len(dna[0])
    ancestor=''
    #print(len(new))
    for i in range(len(dna)):
        for x in range(len(dna[0])):
            new[x]+=dna[i][x]
    for e in new:
        c=Counter(e)
        A.append(c['A'])
        C.append(c['C'])
        G.append(c['G'])
        T.append(c['T'])
        ancestor+=str((c.most_common(1))[0][0])
    
    return ancestor,A,C,G,T

fasta={}
with open("rosalind_cons.txt", 'r') as f:
    for line in f:
        if line.startswith('>'):
            key=line[1:-1]
            fasta[key]=""
        else:
            fasta[key]+=line.strip()
dna=list(fasta.values())
#print(dna)
ancestor,A,C,G,T=cons(dna)
nf=open("output_cons.txt","w")
nf.write(ancestor)
nf.write('\n')
nf.write('A: '+' '.join(str(a) for a in A))
nf.write('\n')
nf.write('C: '+' '.join(str(c) for c in C))
nf.write('\n')
nf.write('G: '+' '.join(str(g) for g in G))
nf.write('\n')
nf.write('T: '+' '.join(str(t) for t in T))
nf.close()