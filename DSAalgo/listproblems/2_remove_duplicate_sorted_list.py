"""
Given an integer list nums sorted in non-decreasing order,
remove the duplicates
such that each unique element appears only once.
The order of the elements should be same.
Then return the number of unique elements in nums.

    Input: arr[] = [2, 2, 2, 2, 2]
    Output: [2]
    Explanation: All the elements are 2, So only keep one instance of 2.

    Input: arr[] = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    Output: [1, 2, 3, 4, 5]

    Input: arr[] = [1, 2, 3]
    Output: [1, 2, 3]
    Explanation : No change as all elements are distinct.


"""
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