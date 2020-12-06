from itertools import product
def lexf(s,n):
    return list(product(s, repeat=n))


f=open("rosalind_lexf.txt","r")
s=f.readline().split()
n=int(f.readline())
f.close()
per=lexf(s,n)
nf=open("output_lexf.txt","w")
for subl in per:
    for item in subl:
        nf.write(str(item))
    nf.write('\n')
nf.close()