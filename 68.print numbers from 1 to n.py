def reverseprinter(n):
    if n==0:
        return 0
    print(n)
    return reverseprinter(n-1)
reverseprinter(10)