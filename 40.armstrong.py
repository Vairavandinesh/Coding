a=153
dummy=a
sum=0
while a!=0:
    remainder=a%10
    sum+=remainder**(len(str(dummy)))
    a//=10
print(dummy==sum)