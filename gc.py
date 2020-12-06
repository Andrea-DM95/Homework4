from collections import Counter
def gc(d):
    mGC={}
    lGC=[]
    for k,v in d.items():
        c=Counter(v)
        GC=((c['G']+c['C'])/len(v))*100
        lGC.append(GC)
        mGC[GC]=k
    m=max(lGC)
    return "{}\n{}".format(mGC[m],m)

fasta={}
with open("rosalind_gc.txt", 'r') as f:
    for line in f:
        if line.startswith('>'):
            key=line[1:-1]
            fasta[key]=""
        else:
            fasta[key]+=line.strip()
nf=open("output_gc.txt","w")
nf.write(gc(fasta))
nf.close()