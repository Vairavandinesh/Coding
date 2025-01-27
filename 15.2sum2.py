def sum2(arr,n):
    d = {}
    for i in range(len(arr)):
        if i not in d:
            d[arr[i]] = i
        if n-arr[i] in d:
            return sorted([i+1,d[n-arr[i]]+1])
        
arr=[2,7,11,15]
target=15
print(sum2(arr,target))


















"""def twosum(arr,target):
    #using two pointers to calculate sum
    i=0
    j=len(arr)-1
    
    while (i<j):
        a=arr[i]+arr[j]
        if target==a:
            return [i+1,j+1]
        elif target<a:
            j-=1
        else:
            i+=1
    return False
arr=[2,7,11,15]
target=9
print(twosum(arr,target))"""