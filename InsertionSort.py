

def InsertionSort(Arr,n):
    for i in range(1,n):
        value=Arr[i]
        hole=i

        while hole>0 and Arr[hole-1]>value:
            Arr[hole]=Arr[hole-1]
            hole=hole-1

        Arr[hole]=value


Array=[7,2,4,1,5,3]
n=6
InsertionSort(Array,n)
for i in range(len(Array)):
    print ("%d" %Array[i])
