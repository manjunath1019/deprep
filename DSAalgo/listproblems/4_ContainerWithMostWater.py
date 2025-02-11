"""
Find the maximum amount of water that can be contained between any two lines, together with the x-axis

input = [1,5,4,3]

output 6
Explanation : 5 and 3 are distance apart so the size of the base = 2 and height of container min(5,3)  = 3
so total area =3 * 2 =6

"""

#Brute force
def containerMostWaterSolution1(list1):
    MAXAREA = 0
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            width = j-i
            area = min(list1[i],list1[j]) * width
            MAXAREA =max(MAXAREA,area)
    return MAXAREA

#Two pointer
def containerMostWaterSolution2(list2):
    left, right = 0 , len(list2)-1
    MAXAREA2 = 0
    while left < right:
        width1 = right -left
        area2 = min(list2[left],list2[right]) * width1
        MAXAREA2 = max(MAXAREA2,area2)
        if list2[left] < list2[right]:
            left +=1
        else:
            right -=1
    return MAXAREA2

if __name__ == '__main__':
    mainlist = [1,8,6,2,5,4,8,3,7]
    solutionarea1 = containerMostWaterSolution1(mainlist)
    print("Brute Force Approach : " , solutionarea1)

    solutionarea2 = containerMostWaterSolution2(mainlist)
    print("Better Optmized Approach Compared Brute force: " , solutionarea2)
