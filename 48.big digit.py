bigd=0
a=int(input("Enter a number : "))
while a!=0:
    remainder=a%10
    if remainder>bigd:
        bigd=remainder
    a//=10
print(bigd)