A=[1,4,5,6,2,34,56,23]
i = 0
while i<(len(A)-1):
    A[i],A[i+1]=A[i+1],A[i]
    i+=2
print (A)
