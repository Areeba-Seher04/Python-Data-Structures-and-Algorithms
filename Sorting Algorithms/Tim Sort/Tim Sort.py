import Sorts
import random
global RUN
RUN=5


def TimSort(array,n):
    for i in range(0,n,RUN):
        Sorts.insertionSort(array,i,min(i+RUN-1,n-1))
    size=RUN
    while size < n:
        for x in range(0,n,size*2):
            array[x:x+2*size]=Sorts.merge(array[x:x+size],array[x+size:x+2*size])
        size*=2
def display(array,n):
    list(map(lambda x: print(x,end=" "),array))
def main():
    array=[x for x in range(7,55)]
    random.shuffle(array)
    display(array,len(array))
    print("\n"*5)
    TimSort(array,len(array))
    print("")
    print("After Sorting")
    display(array,len(array))
main()
