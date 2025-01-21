class Solution:
    def singleNumber(self, nums):
        a={}
        #iterate through the array,if an element occurs increase its count by 1
        for i in nums:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1
        for i,value in a.items():
            if value==1:
                return i
sol=Solution()
print(sol.singleNumber([4,1,2,1,2]))