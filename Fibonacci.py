
n = int(input("Enter the number of Fibonacci numbers to generate"))  

x = 0  
y = 1  
print("The first", n, "Fibonacci numbers are:")
for i in range(n): 
    print(x)  
    next_fib = x + y  
    x = y  
    y = next_fib  
