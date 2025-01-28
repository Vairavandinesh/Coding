weight=int(input("Enter the weight:"))
if weight==0:
    print("0 minutes")
elif weight>0 and weight<=2000:
    print("25 minutes")
elif weight>2000 and weight<=4000:
    print("35 minutes")
elif weight>4000:
    print("45 minutes")
elif weight>7000:
    print("Overloaded")
elif weight<0:
    print("invalid input")
