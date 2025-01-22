def decimal_to_binary(n):
    binary=''
    while(n!=0):
        if (n%2!=0):
            binary+='1'
        else:
            binary+='0'
        n//=2
    return binary[::-1]
print(decimal_to_binary(13))