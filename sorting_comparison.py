def selection(a):
    count=0
    for i in range(0,n):
        min=i
        for j in range(i+1,n):
            count=count+1
            if(a[j]<a[min]):
                min=j
        temp=a[i]
        a[i]=a[min]
        a[min]=temp
    return count

def bubble(a):
    count=0
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            count=count+1
            if(a[j+1]>a[j]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return count
def mergeSort(arr):
    count=0
    if len(arr) >1: 
        mid = len(arr)//2  
        L = arr[:mid]  
        R = arr[mid:] 
        mergeSort(L) 
        mergeSort(R) 
  
        i = j = k = 0
          
       
        while i < len(L) and j < len(R):
            count=count+1
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        
        while i < len(L):
            count=count+1
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R):
            count=count+1
            arr[k] = R[j] 
            j+=1
            k+=1
    return count
  

    



n=int(input("enter the num of elements in array: "))
a=[]
print("enter elements: ")
for i in range(0,n):
    a.append(int(input()))
print("selection sort: ",selection(a))
print("bubble sort: ",bubble(a))
print("merge sort: ",mergeSort(a))
