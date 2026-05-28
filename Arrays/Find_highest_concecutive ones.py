def count_max_ones(arr):
    max_count=0
    consecutives_ones=1
    for i in range(0,len(arr)):
        # print(i)
        if arr[i]==1 and i>0 and arr[i-1]==1:
            consecutives_ones+=1
            if consecutives_ones>max_count:
                max_count=consecutives_ones
        else:
            consecutives_ones=1
    return max_count
print(count_max_ones([1,1,0,0,1,1,1,0,1]))
print(count_max_ones([1,1,0,0,1,1,1,0,0]))
print(count_max_ones([1,1,0,0,1,1,1,0,0,1,1,1,1,1,1,1]))
#Time complexity is o(n) and space complexity o(1)
