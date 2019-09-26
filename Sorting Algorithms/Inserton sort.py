def insertion_sort(array):
    for j in range(1,len(array)):
        key=array[j]
        i=j-1
        while i >= 0 and array[i] > key:
            print(array)
            array[i+1]=array[i]
            i=i-1
        array[i+1]=key

def main():
    array=[32,2,9,24,78,12,11]
    insertion_sort(array)
    print("the sorted array is : ",array)
main()
