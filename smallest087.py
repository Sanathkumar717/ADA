def smallest(a,k):
    for i in range(0,k):
        min=i
        for j in range(i+1,n):
            if(a[j]<a[min]):
                min=j
        temp=a[i]
        a[i]=a[min]
        a[min]=temp
    print("k th smallest is: ",a[k-1])
n=int(input("enter the num of elements in array: "))
k=int(input("enter value of k: "))
a=[]
print("enter elements: ")
for i in range(0,n):
    a.append(int(input()))
smallest(a,k)
