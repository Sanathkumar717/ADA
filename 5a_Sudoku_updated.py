import math

def print_grid(arr): 
    for i in range(n): 
        for j in range(n): 
            print (arr[i][j],end=" ") 
        print ('n') 
  
          

def find_empty_location(arr,l): 
    for row in range(n): 
        for col in range(n): 
            if(arr[row][col]==0): 
                l[0]=row 
                l[1]=col 
                return True
    return False
  

def used_in_row(arr,row,num): 
    for i in range(n): 
        if(arr[row][i] == num): 
            return True
    return False
  
 
def used_in_col(arr,col,num): 
    for i in range(n): 
        if(arr[i][col] == num): 
            return True
    return False
  

def used_in_box(arr,row,col,num): 
    for i in range(int(math.sqrt(n))): 
        for j in range(int(math.sqrt(n))): 
            if(arr[i+row][j+col] == num): 
                return True
    return False
  

def check_location_is_safe(arr,row,col,num): 
      
    
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%(int(math.sqrt(n))),col - col%(int(math.sqrt(n))),num) 
  

def solve_sudoku(arr): 
      
      
    l=[0,0] 
      
       
    if(not find_empty_location(arr,l)): 
        return True
      
    
    row=l[0] 
    col=l[1] 
      
     
    for num in range(1,n+1): 
          
         
        if(check_location_is_safe(arr,row,col,num)): 
              
            
            arr[row][col]=num 
  
            
            if(solve_sudoku(arr)): 
                return True
  
            
            arr[row][col] = 0
              
            
    return False 
  

if __name__=="__main__": 
      

    n=int(input("n: "))
    grid=[[0 for x in range(n)]for y in range(n)] 
      
     
    grid=[]
    
    for i in range(n):
        a=[]
        for i in range(n):
            a.append(int(input()))
    
        grid.append(a)
      
    
    if(solve_sudoku(grid)): 
        print_grid(grid) 
    else: 
        print ("No solution exists")
