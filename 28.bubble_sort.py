arr=[64,34,25,12,22,11,90]
#bubble sort can only swap its adjacent elements , so we have to travers the array twice
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j]<arr[i]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)