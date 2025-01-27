def stocks(nums):
    #using two pointers to traverse the array to find the best time to buy and sell the stocks
    i=0
    maxi=0
    for j in range(1,len(nums)):
        if nums[j]>nums[i]:
            maxi=max(maxi,nums[j]-nums[i])
        else:
            i=j
    return maxi