def insertionSort(arr,start,end):
    for i in range(start+1,end+1):
        key=arr[i]
        j=i-1
        while j >= start and arr[j] > key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
def merge(left_array,right_array):
    i=0
    j=0
    temp=[]
    while i < len(left_array) and j < len(right_array):
        if left_array[i] > right_array[j]:
            temp.append(right_array[j])
            j+=1
        else:
            temp.append(left_array[i])
            i+=1
    while i < len(left_array):
        temp.append(left_array[i])
        i+=1
    while j < len(right_array):
        temp.append(right_array[j])
        j+=1
    return temp
