#method 1
for i in range(4):
    for j in range(i+1):
        for k in range(j):
            print("{",end="")
        for k in range(j):
            print("}",end="")
    print()
#method 2
for i in range(4):
    for j in range(i+1):
        print("{"*j,end="")
        print("}"*j,end="")
    print()