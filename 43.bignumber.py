a,b,c=1,5,10
if(a>b):
    if(a>c):
        print("a is greater")
    else:
        print("c is greater")
elif(a<b):
    if(b>c):
        print("b is greater")
    else:
        print("c is greater")
elif (a==b and c<b):
    print('a and b are greater and equal')
elif (a==b==c):
    print("all are equal")
elif (a>b and b==c):
    print("a is greater than b and c there are equal")
elif(a==c and b<c):
    print("a and c are greater than b")
