def summary(nums):
    result=[]
    i=0
    while i<len(nums):
        start=nums[i]
        while i<len(nums)-1 and nums[i+1]==nums[i]+1:
            i+=1
        if start==nums[i]:
            result.append(str(nums[i]))
        else:
            result.append(str(start)+'->'+str(nums[i]))
        i+=1
    return result
print(summary([0,1,2,4,5,7]))