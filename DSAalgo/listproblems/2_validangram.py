def bruteForceApproach(str1:str,str2:str):
    str1_len=len(str1.replace(" ",""))
    str2_len=len(str2.replace(" ",""))
    sortedstr1= sorted(str1.replace(" ",""))
    sortedstr2=sorted(str2.replace(" ",""))
    print(sortedstr1,sortedstr2)
    if str1_len!= str2_len:
        return False
    for i in range(str1_len):
        if sortedstr1[i]!=sortedstr2[i]:
            return False
    return True

def findangram_solution1(str1,str2):
    dict = {}
    an1 =str1.lower().replace(" ","")
    an2 = str2.lower().replace(" ","")
    print(an1,an2)
    for i in range(len(an1)):
        if an1[i] in dict:
            dict[an1[i]]+=1
        else:
            dict[an1[i]]=1
    for i in range(len(an1)):
        if an2[i] in dict:
            dict[an2[i]]-=1
        else:
            dict[an2[i]]=1
    print(dict)

    for count in dict.values():
        if count!=0:
            return False
    return True

def findangram_solution2(str1,str2):
    counts= [0]*26
    print(counts)
    an1 =str1.lower().replace(" ","")
    an2 = str2.lower().replace(" ","")
    for char in an1:
        counts[ord(char)-ord('a')]+=1
    print(counts)
    for char in an2:
        counts[ord(char)-ord('a')]-=1
    print(counts)

    for cnt in counts:
        if cnt!=0:
            return False
    return True

if __name__ == '__main__':
    str1='school master'
    str2 ='the class room'
    bool = bruteForceApproach(str1,str2)
    print(bool)

    bool1 = findangram_solution1(str1,str2)
    print(bool1)

    bool2 = findangram_solution2(str1,str2)
    print(bool2)