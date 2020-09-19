#Program to calculate factorial and to compute the factors of the given number using recursion and iteration

#factorial program using recursion
def factorial_r(n):
    if n < 0:
        return 0
        
    if (n == 1 or n == 0):
        return 1
        
    else:
        return n * factorial_r(n - 1)
    
num = int(input("Enter a number for finding it's factorial using recursion: "))      
print("Factorial of ", num, "using recursion is ", factorial_r(num))

#Factorial Program using iteration 
def factorial_i(n): 
    if n < 0: 
        return 0
    
    elif n == 0 or n == 1: 
        return 1
    
    else: 
        fact = 1
        while(n > 1): 
            fact = fact * n 
            n -= 1
        return fact 

num = int(input("Enter a number for finding it's factorial using iteration: "))  
print("Factorial of", num, "using iteration is", factorial_i(num))

#Finding factor of number using recursion
def factors_r(n, i):
    if (i <= n): 
        if (n % i == 0):
            print(i, end = " ")
        factors_r(n, i + 1)

num = int(input("\nEnter a number for finding it's factors using recursion: "))
print("The factors of", num, "are:")
factors_r(num, 1)

#Finding factor of number using iteration
def factors_i(n):
   print("The factors of", n, "are:")
   for i in range(1, n + 1):
       if n % i == 0:
           print(i, end = " ")

num = int(input("Enter a number for finding it's factors using iteration: "))
factors_i(num)









        
