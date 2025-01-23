def twosum(arr,target):
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
print(twosum(arr,target))