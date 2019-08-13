
def printFibonacciNumbers(n): 
      
    f1 = 0
    f2 = 1
    for x in range(0, n): 
        print(f2, end = " ") 
        next = f1 + f2 
        f1 = f2 
        f2 = next
n=int(input("enter value of n: "))
printFibonacciNumbers(n)
