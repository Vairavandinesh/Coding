#perfect number: if the sum of the divisors of a number is equal to the number it is a perfect number
a=6
perfect=0
for i in range(1,(a//2)+1):
    if(a%i==0):
        perfect+=i
    if perfect>a:
        break
print(a==perfect)