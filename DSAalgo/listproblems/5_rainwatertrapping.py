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