def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
a=fact(153)
new=0
n=153
while n!=0:
    n=n%10
    new+=fact(n)
    n//=10

print(new)