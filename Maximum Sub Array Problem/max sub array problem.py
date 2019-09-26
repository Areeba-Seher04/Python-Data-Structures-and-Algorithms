import random
list1=list(range(random.randint(-6,-1),random.randint(5,12)))
random.shuffle(list1)
string=','
list1=list(map(str,list1))
list1=string.join(list1)
try:
    file=open("f1.txt","x")
except:
    file=open("f1.txt","w")
file.write(list1)
file.close()
file=open("f1.txt","r")
my_list=file.read()
my_list=my_list.split(',')
my_list=list(map(int,my_list))
print(my_list)

def MaxCrossingOver(arr,l,m,h):
    sm=0
    left_sm=-10000
    right_sm=-10000
    for i in range(m,l-1,-1):
        sm+=arr[i]
        if sm > left_sm:
            left_sm=sm
    sm=0
    for j in range(m+1,h+1):
        sm+=arr[j]
        if sm > right_sm:
            right_sm=sm
    return left_sm+right_sm

def MaxSubArray(arr,l,h):
    if l == h:
        return arr[0]
    m=(l+h)//2
    return max(MaxSubArray(arr,l,m),MaxSubArray(arr,m+1,h),MaxCrossingOver(arr,l,m,h))

def main():
    arr = my_list
    n=len(arr)
    my_ans=MaxSubArray(arr,0,n-1)
    print("Maximum Contigous sum is : ", my_ans)

main()
