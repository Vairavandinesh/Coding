a="35427"
for i in range(len(a)-1,-1,-1):
    #iterating from the 1s place , if its odd ,the entire string is odd
    #else skip the index and move left
    if (int(a[i])%2!=0):
        print(a[:i+1])
        break
print("")
