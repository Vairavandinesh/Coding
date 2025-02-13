#rule : the adjacent elements should not have same parity
# array should be in the format odd even odd (or) even odd even
def isArraySpecial(nums):
    i=1
    while i<len(nums):
        if nums[i-1]%2==0 and nums[i]%2==0:
            return False
        elif nums[i-1]%2!=0 and nums[i]%2!=0:
            return False
        i+=1
    return True