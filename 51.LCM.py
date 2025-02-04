#using math module
import math
a=int(input("Enter n1:"))
b=int(input("Enter n2:"))
lcm=math.lcm(a,b)
print(lcm)
#with any module
def lcm(a,b):
    greater=max(a,b)
    while True:
        if greater%a==0 and greater%b==0:
            return greater
        greater+=1
print(lcm(a,b))