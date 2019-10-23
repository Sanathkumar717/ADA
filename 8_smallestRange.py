
  
N = 5
  

ptr = [0 for i in range(501)] 
  

def findSmallestRange(arr, n, k): 
  
    i, minval, maxval, minrange, minel, maxel, flag, minind = 0, 0, 0, 0, 0, 0, 0, 0
          
     
    for i in range(k + 1): 
        ptr[i] = 0
  
    minrange = 10**9
          
    while(1):     
          
            
        minind = -1
        minval = 10**9
        maxval = -10**9
        flag = 0
  
         
        for i in range(k): 
              
               
            if(ptr[i] == n): 
                flag = 1    
                break
  
           
            if(ptr[i] < n and arr[i][ptr[i]] < minval): 
                minind = i 
                minval = arr[i][ptr[i]] 
              
             
            if(ptr[i] < n and arr[i][ptr[i]] > maxval): 
                maxval = arr[i][ptr[i]] 
              
          
  
       
        if(flag): 
            break
  
        ptr[minind] += 1
  
        
        if((maxval-minval) < minrange): 
            minel = minval 
            maxel = maxval 
            minrange = maxel - minel 
      
    print("The smallest range is [", minel, maxel,"]") 
  

arr= []
M=int(input("M: "))
L=int(input("L: "))
for i in range(M):
    ar=[]
    for i in range(L):
        ar.append(int(input()))
    arr.append(ar)
  
k = len(arr) 
  
findSmallestRange(arr, N, k) 
