from math import sqrt
a=int(input("Enter a number : "))
if a<2:
    print("Its not prime")
else:
    is_prime=True
    for i in range(2,int(sqrt(a))+1):
        if a%i==0:
            is_prime=False
            break
    if is_prime:
        print("Its a prime number")
    else:
        print("Its not a prime number")