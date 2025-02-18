def printer(n):
    if n==0:
        return 
    printer(n-1)
    print(n)
print(printer(7))