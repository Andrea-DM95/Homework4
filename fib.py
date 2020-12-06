known_fibo = {0:0, 1:1}
def fibo(n,k):
    if n not in known_fibo:
        known_fibo[n] = fibo(n-1,k) + k*fibo(n-2,k)
    return known_fibo[n]
f=open("rosalind_fib.txt","r")
n,k=f.readline().split()
n=int(n)
k=int(k)
f.close()
nf=open("output_fib.txt","w")
nf.write(str(fibo(n,k)))
nf.close()