def bubblesorting(nums):
    for i in range(len(nums)-1,-1,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
            print(nums)
    return nums
c
if __name__ == '__main__':
    nums = [5,8,10,2,9]
    result = bubblesorting(nums)
    print(result)