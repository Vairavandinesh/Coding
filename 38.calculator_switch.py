okay=input("shall we continue ? (enter proceed to continue): ")
while okay=="proceed":
    option=int(input("Enter operations : 1-add,2-diff,3-mul,4-divide "))
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))
    if option==1:
        print(a+b)
    elif option==2:
        if a>b:
            print(a-b)
        elif b>a:
            print(b-a)
    elif option==3:
        print(a*b)
    elif option==4:
        if a>b:
            print(a//b)
        elif a<b:
            print(b//a)
    okay=input("Continue ?")