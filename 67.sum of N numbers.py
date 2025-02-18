def summ(n):
    if n==1:
        return 1
    return n+summ(n-1)
print(summ(5))