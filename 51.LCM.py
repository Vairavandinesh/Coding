a=10
b=20
if (a%b==0 and b%b==0):
    print(b)
elif (a%b!=0 or b%b!=0):
    for i in range(a*b,a,-1):
        if (a%b==0 and b%b==0):
            print(i)
else:
    print(a*b)

