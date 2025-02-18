def power(x,n,count):
    if count>n-1:
        return 1
    return x*power(x,n,count+1)
print(power(2,3,0))