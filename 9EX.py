file2=open('float_data.txt','w')
i=0
while i<1000000:
    file2.write(str(randint(0,100)+randint(1,99)/100))
    i+=1
file2.close()
