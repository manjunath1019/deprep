def bruteforceapproach(nums):
    pass

def removeduplicatesolution1(nums):
    replace=1
    for i in range(1,len(nums)):
        if nums[i-1]!=nums[i]:
            nums[replace]=nums[i]
            replace+=1
    print(nums)
    return replace



if __name__ == '__main__':
    nums = [5,5,6,7,7,8,9]
    result = removeduplicatesolution1(nums)
    print(nums[:result])