a=int(input("Enter number"))
sum=0
for i in range(1,(a//2)+1):
    if a%i==0:
        sum+=i
if sum==a:
    print("perfect number")
else:
    print("Not")