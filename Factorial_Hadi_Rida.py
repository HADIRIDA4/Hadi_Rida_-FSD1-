#First method
f=int(input("PLEASE ENTER A NUMBER TO FIND IT'S FACTORIAL \n \t number : ") ) 
def Factorial(f) :
    v=1
    for i in range (f,0, - 1):
        v=v*i
       
    print(f"The factorial of of your input is \n \t {v} ")
Factorial(f)  
#USING Math library uncomment to check
#from math import factorial
#def Factorial_m(f):
    #return factorial(f) 
#print(f"The factorial of of your input is \n \t {Factorial_m(f) } ")