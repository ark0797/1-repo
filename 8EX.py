from random import *
file1=open('int_data.txt','w')
i=0
while i<1000000:
    file1.write(str(randint(0,100)))
    i+=1
file1.close()
