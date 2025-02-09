"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non - decreasing order.
Example 1:
Input: nums = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
Explanation: After squaring, the array becomes
[16, 1, 0, 9, 100].
After sorting, it becomes
[0, 1, 9, 16, 100].

Example 2:
Input: nums = [-7, -3, 2, 3, 11]
Output: [4, 9, 9, 49, 121]
"""
class Solution:
    def sortedSquare(self,nums: list[int]) -> list[int] :
        l = len(nums)
        left =0
        right = l-1
        position = l-1
        outputresult = [0]*l
        while left < right or left ==right:
            leftsquare = nums[left]*nums[left]
            rightsquare = nums[right]*nums[right]
            #print("left and right" , left,right)
            if leftsquare < rightsquare:
                outputresult[position]= rightsquare
                right = right - 1
            else:
                outputresult[position]= leftsquare
                left=left+1
            position = position-1
            #print(outputresult)
        return outputresult
if __name__ == '__main__':
    sortedArray = [-4, -1, 0, 3, 10]
    solution = Solution()
    result = solution.sortedSquare(sortedArray)
    print("Input : ",sortedArray)
    print("Outputs : " , result)