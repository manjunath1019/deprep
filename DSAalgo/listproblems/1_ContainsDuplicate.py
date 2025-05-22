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
# Time complexity: O(n^2) - Nested loops compare each element with every other element.
# Space complexity: O(1) - No extra space is used besides the input list.
def find_duplicates_brute_force(nums: list[int]) -> bool:
    """
    Checks for duplicates in a list using a brute-force approach.

    Compares each element with every other element in the list.

    Args:
        nums: A list of integers.

    Returns:
        True if any element appears at least twice, False otherwise.
    """
    n =len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]==nums[j]:
                return True
    return False

# Time complexity: O(n) - Iterates through the list once.
# Space complexity: O(n) - In the worst case, the hash map stores all unique elements.
def find_duplicates_with_hashing(nums: list[int]) -> bool:
    """
    Checks for duplicates in a list using a hash map (dictionary).

    Iterates through the list, storing elements in a hash map.
    If an element is already in the map, a duplicate is found.

    Args:
        nums: A list of integers.

    Returns:
        True if any element appears at least twice, False otherwise.
    """
    track = {}
    n=len(nums)
    for item in nums:
        if item in track:
            return True
        else:
            track[item]=1
    return False

# Time complexity: O(n) - Converting list to set takes O(n) on average.
# Space complexity: O(n) - In the worst case, the set stores all unique elements.
def find_duplicates_with_set(nums: list[int]) -> bool:
    """
    Checks if a list contains duplicate elements using a set.

    Converts the list to a set and compares their lengths.
    If the set is shorter than the list, duplicates exist.

    Args:
        nums: A list of integers.

    Returns:
        True if any element appears at least twice, False otherwise.
    """
    set_nums = set(nums)
    if len(set_nums) < len(nums):
        return True
    else:
        return False

if __name__ == '__main__':
    test_cases = [
        {"name": "Empty list", "input": [], "expected": False},
        {"name": "No duplicates", "input": [1, 2, 3, 4, 5], "expected": False},
        {"name": "Simple duplicates", "input": [1, 2, 3, 1], "expected": True},
        {"name": "Existing list with duplicates", "input": [-1, 1, 2, 3, 4, -1], "expected": True},
        {"name": "All duplicates", "input": [7, 7, 7, 7], "expected": True},
        {"name": "Duplicates at beginning and end", "input": [1, 1, 2, 3, 4, 4], "expected": True},
    ]

    functions_to_test = [
        find_duplicates_brute_force,
        find_duplicates_with_hashing,
        find_duplicates_with_set,
    ]

    for test_case in test_cases:
        print(f"Test: {test_case['name']}")
        print(f"Input: {test_case['input']}")
        print(f"Expected: {test_case['expected']}")

        for func in functions_to_test:
            actual_output = func(test_case['input'])
            pass_status = actual_output == test_case['expected']
            print(f"  {func.__name__}: Result: {actual_output}, Pass: {pass_status}")
        print("-------------------------------------")