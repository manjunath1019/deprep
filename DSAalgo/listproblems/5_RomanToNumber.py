"""

Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


"""
def convertToNumber(input):
    roman ={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    total = 0
    for i in range(len(input)-1):
        romanCurrentchar= input[i]
        romanNexttchar = input[i+1]
        print(romanCurrentchar,romanNexttchar)
        if roman[romanCurrentchar] < roman[romanNexttchar]:
            total-=roman[romanCurrentchar]
        else:
            total+=roman[romanCurrentchar]
    return total+roman[input[-1]]

if __name__ == '__main__':
    Rnbr  = "MCMXIV"
    k=convertToNumber(Rnbr)
    print(k)