#rectangle
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()
#right angle triangle
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
#inverted right angle triangle
for i in range(5):
    for j in range(5-i):
        print("*",end=" ")
    print()
#pyramid
for i in range(5):
    for j in range(5-i-1):
        print(" ",end=" ")
    for j in range(i*2+1):
        print("*",end=" ")
    print()
