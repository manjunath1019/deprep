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