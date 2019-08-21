def largest(a,n,k):
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if(a[j+1]>a[j]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    for i in range(0,k):
        print(a[i],end=" ")
n=int(input("enter the num of elements in array: "))
k=int(input("enter value of k: "))
a=[]
print("enter elements: ")
for i in range(0,n):
    a.append(int(input()))
largest(a,n,k)
