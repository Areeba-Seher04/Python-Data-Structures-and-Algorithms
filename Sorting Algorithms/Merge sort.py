def merge(array,L_array,R_array):
    i=j=k=0
    while i< len(L_array) and j < len(R_array):
        if L_array[i] < R_array[j]:
            array[k]=L_array[i]
            k+=1
            i+=1
        else:
            array[k]=R_array[j]
            k+=1
            j+=1
    for x in range(i,len(L_array)):
        array[k]=L_array[x]
        k+=1
    for x in range(j,len(R_array)):
        array[k]=R_array[x]
        k+=1

def merge_sort(array):
    mid=len(array)//2
    L_array=[]
    R_array=[]
    if len(array) > 1:
        L_array=array[:mid]
        R_array=array[mid:]
        merge_sort(L_array)
        merge_sort(R_array)
    merge(array,L_array,R_array)

def main():
    array=[32,2,9,24,24,78,12,11]
    merge_sort(array)
    print("the sorted array is : ",array)
main()
