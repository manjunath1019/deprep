"""
Trapping Rainwater Problem states that given an array of n non-negative integers arr[]
representing an elevation map where the width of each bar is 1,
compute how much water it can trap after rain.

input: arr[] = [3, 0, 1, 0, 4, 0, 2]
Output: 10
Explanation: The expected rainwater to be trapped is shown in the above image.

Input: arr[] = [3, 0, 2, 0, 4]
Output: 7
Explanation: We trap 0 + 3 + 1 + 3 + 0 = 7 units.

Input: arr[] = [1, 2, 3, 4]
Output: 0
Explanation: We cannot trap water as there is no height bound on both sides

Input: arr[] = [2, 1, 5, 3, 1, 0, 4]
Output: 9
Explanation : We trap 0 + 1 + 0 + 1 + 3 + 4 + 0 = 9 units of water.
"""
def get_number_of_units(arr:list[int]):
    n=len(arr)
    units=0
    larr=[0]*n
    rarr=[0]*n
    lmax=rmax=0
    for i in range(n):
        lmax=max(lmax,arr[i])
        larr[i]=lmax
    for j in range(n-1,-1,-1):
        rmax=max(rmax,arr[j])
        rarr[j]=rmax
    print(larr,rarr)
    for item in range(n):
        value =min(larr[item],rarr[item])-arr[item]
        units+=  value
        print("Current Total units : " ,units, " Current units", value)
    print("=================================================================")
    return units

if __name__ == '__main__':
    #arr=[4,2,0,3,2,5]
    arr =[0,1,0,2,1,0,1,3,2,1,2,1]
    print(arr)
    result= get_number_of_units(arr)
    print("Total_units" , result)