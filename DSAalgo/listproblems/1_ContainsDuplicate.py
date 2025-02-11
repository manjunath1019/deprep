"""
Given an integer list nums,
return true if any element appears at least twice in the list,
and
return false if every element is distinct.

nums =[1,1,1,3,3,4,3,2,4,2]
return True

nums = [1,2,3,4,6,7]
return False
"""
def bruteForceSolution(nums):
    n =len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]==nums[j]:
                return True
    return False

def find_contains_duplicate_solution_1(nums:list):
    track = {}
    n=len(nums)
    for item in nums:
        if item in track:
            return True
        else:
            track[item]=1
    return False

if __name__ == '__main__':
    nums = [-1,1,2,3,4,-1]
    result = find_contains_duplicate_solution_1(nums)
    print(result)
    print("-------------------------------------")
    result2= bruteForceSolution(nums)
    print(result2)