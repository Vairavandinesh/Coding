a="madam"
#method 1: string slicing
print(a==a[::-1])
#method 2: 2 pointers
#Note : if the letters differ by capital and small , it wont consider it as a palindrome
i=0
j=len(a)-1
while i<j:
    if a[i]==a[j]:
        i+=1
        j-=1
    elif a[i]!=a[j]:
        print("Not palindrome")
        break
    print("Palindrome")