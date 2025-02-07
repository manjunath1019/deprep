def bruteforce_solution(nums:list,target:int):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            curr_sum=(nums[i]+nums[j])
            if target==curr_sum:
                return (i,j)
    return (-1,-1)

def get_two_sum_solution1(nums:list,target:int):
    dict= {}
    for i in range(len(nums)):
        diff = target-nums[i]
        if nums[i] in dict:
            return True
        else:
            dict[diff] =nums[i]
    return False

def get_two_sum_for_sorted_list(nums:list,target:int):
    n = len(nums)
    left= 0
    right = n-1
    while left<=right:
        cur_sum=nums[left]+nums[right]
        if target == cur_sum:
            return True
        if target > cur_sum:
            left+=1
        else:
            right-=1
    return False

if __name__ == '__main__':
    nums = [2,3,4,6,9]
    result=bruteforce_solution(nums,10)
    print(result)

    bool = get_two_sum_solution1(nums,19)
    print(bool)

    nums1 = [-5,-4,-3,1,2,3,5,6,9]
    bool1= get_two_sum_for_sorted_list(nums1,target=9)
    print(bool1)