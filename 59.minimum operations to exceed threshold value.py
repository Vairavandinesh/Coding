#input1 nums=[2,11,10,1,3] k=10
#output1 2
#input2 nums=[1,1,2,4,9] ,k=20
#output2 4
#explanation : minimum operations to make the minimum element of the array greater than or equal to k
def minoperations(nums,k):
    count=0
    x=min(nums)
    while x<k:
        a=min(nums)
        firstmin=nums.pop(nums.index(a))
        b=min(nums)
        secondmin=nums.pop(nums.index(b))
        nums.append((min(a,b)*2)+max(a,b))
        x=min(nums)
        count+=1
    return count