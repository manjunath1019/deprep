def findValidparethese(str1):
    dict = {
        '(':')',
        '[':']',
        '{':'}',
        '<':'>'
    }
    stack=[0]*len(str1)
    i=0
    for item in str1:
        if item in dict.keys():
            stack[i]=item
            i+=1
        else:
            if i>0 and (item==dict[stack[i-1]]):
                stack[i-1]=0
                i-=1
            else:
                return False
        print(stack)
    return True
if __name__ == '__main__':
    str1 = "({[]})"
    bool =findValidparethese(str1)
    print(bool)