#Python variables - A Python variable is a reserved memory location to store values.
#Every value in Python has a datatype. Different data types in Python are Numbers, List, Tuple, Strings, Dictionary, etc.,

#How to Declare and use a Variable
a = 1
print(a)

#Re-declare a Variable - You can re-declare Python variables even after you have declared once. It will overwrite the value.
a = "Priya"
print(a)

#Python String Concatenation and Variable
a = "PriyaSundaram"
b = 25
print(a+str(b))

#Python Variable Types: Local & Global
#Global variable and Local variable. When you want to use the same variable for rest of your program or module you declare it as a global variable, 
#while if you want to use the variable in a specific function or method, you use a local variable while Python variable declaration

vbl1 = 100
print('Global Vbl: ', end = ' ')
print(vbl1)

def function1() :    
    vbl1 = 'Inside Method 1'
    print('Re-defining inside the method: ',end = ' ')
    print(vbl1)
function1()
print('After method 1: ', end = ' ')
print(vbl1)

def function2() :
    global vbl1
    print('Re-defining inside the method: ',end = ' ')
    print(vbl1)
    vbl1 = 'Inside Method 2'    
function2()
print('After method 2: ', end = ' ')
print(vbl1)

# Delete a variable - You can also delete Python variables using the command del “variable name”.
delVar = 10
print(delVar)
del delVar
print(delVar)


# Notes:
# Variables are referred to “envelop” or “buckets” where information can be maintained and referenced. Like any other programming language Python also uses a variable to store the information.
# Variables can be declared by any name or even alphabets like a, aa, abc, etc.
# Variables can be re-declared even after you have declared them for once
# Python constants can be understood as types of variables that hold the value which can not be changed. Usually Python constants are referenced from other files. Python define constant is declared in a new or separate file which contains functions, modules, etc.
# Types of variables in Python or Python variable types : Local & Global
# Declare local variable when you want to use it for current function
# Declare Global variable when you want to use the same variable for rest of the program
# To delete a variable, it uses keyword “del”.