A=[1,22,33,4,5,5,5,67,90,56,56,56]
i=0
while i<len(A)-1:
    if A[i]!=A[i-1] and A[i]!=A[i+1]:
        print(A[i])
    i+=1
