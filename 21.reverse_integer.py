a=1234
reverse=0
while a!=0:
    reverse=(reverse*10)+a%10
    a//=10
print(reverse)