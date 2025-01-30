nums=[2,3,1]
#output=11
#subarrays = [2],[2,3],[3,1]
totalsum=0
for i in range(len(nums)):
    totalsum=totalsum+sum(nums[max(0,i-nums[i]):i+1])
print(totalsum)