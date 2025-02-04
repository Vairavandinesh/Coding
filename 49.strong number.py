def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
a=145
org=a
rem=0
while a!=0:
    rem+=fact(a%10)
    a//=10
print(org==rem)