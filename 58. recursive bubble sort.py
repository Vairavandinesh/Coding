def recursivebubblesort(arr,n):
    if n==1:
        return arr
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    return recursivebubblesort(arr,n-1)
arr=[4,1,3,9,7]
n=len(arr)
print(recursivebubblesort(arr,n))
