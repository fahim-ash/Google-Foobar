
# import numpy


arr=[-2, -3, 4, -5] # output 30
def solution(arr):

    if(arr.count(0) == len(arr)):
        return(str(0))

    if(len(arr) == 1 and len([n for n in arr if n < 0]) == 1):
        return(str(arr[0]))

    if(len([n for n in arr if n < 0]) == 1 and arr.count(0) == len(arr)-1):
        return(str(0))

    Val = 1

    for i in arr:
        if (i != 0 and i <= 1000):
            Val *= i

    if Val < 0:
        BigNeg = max([n for n in arr if n < 0])
        Val = Val/BigNeg

    return(str(int(Val)))



    # z=sorted(arr,key=abs,reverse=True)
    # max=0
    # for i in range(len(z)):
    #     list=z[:i+1]
    #     print(list)
    #     result1= numpy.prod(list)
    #     if result1>max:
            
    #         max=result1
    
    # return max



print(solution(arr))


