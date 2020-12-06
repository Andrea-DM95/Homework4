##WITH INDEX
def lis(l,n):
    pre=[0]*n
    att=[0]*(n+1)
    L=1
    for i in range(n):
        if l[i]>l[att[L]]:
            L+=1
            att[L]=i
            pre[i]=att[L-1]
        else:
            place=binary_search(l[i],l,att,L)
            pre[i]=att[place-1]
            att[place]=i
    result=[]
    k = att[L]
    for i in range(L, -1, -1):
        result.append(l[k])
        k = pre[k]
    #print(att)
    return result[::-1]

##WITH INDEX
def binary_search(element,l,array,end):
    mid = 0
    start = 0

    while (start <= end):
        mid = (start + end) // 2
        
        if element < l[array[mid]]:
            end = mid - 1
        else:
            start = mid + 1
    
    return start