def onebits(n):
    #for converting decimal to binary
    result=''
    while(n!=0):
        if (n%2!=0):
            result+='1'
        else:
            result+='0'
        n//=2
    a=result[::-1]
    #for finding the number of 1s
    count=0
    for i in range(len(a)):
        if a[i]=='1':
            count+=1
    return count
print(onebits(11))
