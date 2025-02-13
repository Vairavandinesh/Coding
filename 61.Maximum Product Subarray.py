#find the subarray within the array , with highest multiplication value of all
#subarray should be contiguous , for getting high value , we should not skip inbetween values if it has negative values or 0
'''
input : nums=[2,3,-2,4]
output : 6
'''
def maxprodsubarray(nums):
    maxi=0
    prefix=1
    for i in nums:
        if i==0:
            prefix=1
            continue
        else:
            prefix*=i
        maxi=max(maxi,prefix)
    suffix=1
    for i in range(len(nums)-1,-1,-1):
        if nums[i]==0:
            suffix=1
            continue
        else:
            suffix*=nums[i]
        maxi=max(maxi,suffix)
    return maxi