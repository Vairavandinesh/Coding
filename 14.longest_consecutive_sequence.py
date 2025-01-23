def longest_seq(arr):
    a=set(arr)
    longest=0
    for i in a:
        if i-1 not in a:
            x=i
            count=1
            while (x+1 in a):
                x+=1
                count+=1
            longest=max(longest,count)
    return longest
arr=[100,4,200,1,3,2]
print(longest_seq(arr))