def first(arr,low,high,x,n):
    if(high>=low):
        mid=low+(high-low)//2
        if((mid==0 or x>arr[mid-1]) and arr[mid]==x):
            return mid
        elif(x>arr[mid]):
            return first(arr,(mid+1),high,x,n)
        else:
            return first(arr,low,(mid-1),x,n)
    return -1
def last(arr,low,high,x,n):
    if(high>=low):
        mid=low+(high-low)//2
        if((mid==n-1 or x<arr[mid+1]) and arr[mid]==x):
            return mid
        elif(x<arr[mid]):
            return last(arr,low,(mid-1),x,n)
        else:
            return last(arr,(mid+1),high,x,n)
    return -1
def countOccurrences(arr,n,x):
    res=0
    for i in range(n):
        if x==arr[i]:
            res+=1
    return res
arr=[1,2,2,2,2,3,4,7,8,8]
n=len(arr)
x=2
print(first(arr,0,n-1,x,n),end=" ")
print(last(arr,0,n-1,x,n),end=" ")
print(countOccurrences(arr,n,x))
