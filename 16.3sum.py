def threesum(nums):
    nums.sort()
    dummy=[]
    for i in range(1,len(nums)):
        if(nums[i]==nums[i-1]):
            continue
        j=i+1
        k=len(nums)-1
        while(j<k):
            sum=nums[i]+nums[j]+nums[k]
            if sum==0:
                dummy.append([nums[i],nums[j],nums[k]])
                j+=1
                k-=1
                while(j<k and nums[j]==nums[j-1]):
                    j+=1
                while(j<k and nums[k]==nums[k+1]):
                    k-=1

            elif sum<0:
                j+=1
            else:
                k-=1
    return dummy
print(threesum([-1,0,1,2,-1,-4]))

