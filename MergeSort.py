


Arr=[54,26,93,17,77,31,44,55,20]

def Merge(L,R,A):               #Merge function takes 3 parameters L as left sorted Array, Right Sorted Array and A as Array to be sorted
    nL=len(L)                   #nL stores length of left sorted array
    nR=len(R)                   #nR stores length of Right sorted array

    i = 0                        #i will iterate left sorted array
    j = 0                       #j will iterate right sorted array,
    k = 0                       #k will iterate through A


    while i<nL and j<nR:
        if L[i] < R[j]:
            A[k]=L[i]                   #if left array's element has small value it will be stored in Array
            i +=1
        else:
            A[k]=R[j]                   #else right array's element will be stored in Array
            j +=1
        k+=1

    while i<nL:                        #In case Right sorted array is finished we'll store left array's element to A
        A[k]=L[i]
        i +=1
        k+=1

    while j<nR:                       #In case Left sorted array is finished we'll store Right array's element to A

        A[k]=R[j]
        j +=1
        k +=1

    return A                            #Returning Sorted Array A


def MergeSort(Arr):                                     #Will take Array Arr as parameter to sort the values in ascending order

    n=len(Arr)                                         #n stores length of Arr

    if(n<2):                                            #if length of array is 0 or 1 we'll return Arr
        return Arr

    mid = int(n/2)                                           #mid variable is used for indicating mid index of array
    left=list(range(0,mid))                             #left is an array of length to mid
    right=list(range(0,n-mid))                                  #Right is an array of length to n-mid

    for i in left:
        left[i]=Arr[i]                                  #Storing elements in Left array

    #print(left)

    for i in range(mid, n):

       right[i-mid] = Arr[i]                                #Storing elements in Right array
    #print(right)

    MergeSort(left)                                     #passing left array to MergeSort to divide further
    MergeSort(right)                                    #passing right array to MergeSort to divide further

    Merge(left,right,Arr)                               #passing left,right and Arr to Merge
    return Arr


print(MergeSort(Arr))