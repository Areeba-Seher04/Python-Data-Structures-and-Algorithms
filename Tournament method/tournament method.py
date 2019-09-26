from random import *
def tour(array):
    
    mid=len(array)//2
    if len(array) == 1:
        
        return array[0]
    else:
        ans=min(tour(array[:mid]),tour(array[mid:]))
        
        return ans

def main():
    no=int(input("Enter Your size of list: "))
    array=[randint(1,50) for x in range(no)]
    print(array)
    print(tour(array))
    
main()
