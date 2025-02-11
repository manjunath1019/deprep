"""
Given a string s having lowercase characters,
find the length of the longest substring without repeating characters.


Input: s = “aaa”
Output: 1
Explanation: The longest substring without repeating characters is “a”

Input: s = “abcdefabcbb”
Output: 6
Explanation: The longest substring without repeating characters is “abcdef”.

"""
def findLongestNonRepeating(str1):
    track = {}
    max_len=0
    start=0
    for right in range(len(str1)):
        cur_char = str1[right]
        if cur_char in track and track[cur_char] >= start:
            start=track[cur_char]+1
        else:
            max_len = max(max_len,right-start+1)
        track[cur_char]=right
    return max_len


if __name__ == '__main__':
    str1 = "abcacbdd"
    result = findLongestNonRepeating(str1)
    print(result)