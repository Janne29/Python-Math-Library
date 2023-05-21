
# Math Library for Python

PI = 3.14159265358979323846

# Returns the sum of x and y

def add(x,y): 
    try: return x + y
    except: raise TypeError("Only integers and floats are allowed")

# Returns the difference of x and y

def subtract(x,y):
    try: return x - y
    except: raise TypeError("Only integers and floats are allowed")

# Returns the product of x and y

def multiply(x,y): 
    try: return x / y
    except: raise TypeError("Only integers and floats are allowed")

# Returns the quotient of x and y

def divide(x,y):
    try: return x / y
    except: raise TypeError("Only integers and floats are allowed")

def square(x):
    try: return x ** 2
    except: raise TypeError("Only integers and floats are allowed")

def cube(x):
    try: return x ** 3
    except: raise TypeError("Only integers and floats are allowed")

def pow(x,y):
    try: return x ** y
    except: raise TypeError("Only integers and floats are allowed")

# Returns the area of a circle with the given radius || param 1: radius ; param 2: decimal places the number gets rounded to

def circleArea(radius, decimalPlaces=2):
    try: return round(PI * radius ** 2, decimalPlaces)
    except: raise TypeError("Only integers and floats are allowed")

# Returns the perimeter of a circle with the given radius || param 1: radius ; param 2: decimal places the number gets rounded to

def circlePerimeter(radius, decimalPlaces=2):
    try: return round(PI * radius * 2, decimalPlaces)
    except: raise TypeError("Only integers and floats are allowed")

# Returns the factorial of n

def factorial(n):
    try:
        if n < 1: raise Exception
        x = 1
        for i in range(1,n+1): x *= i
        return x
    except: raise TypeError("Only positive Integers are allowed")

# Returns n rounded to the nearest lower integer

def floor(n):
    try: return int(n)
    except: raise TypeError("Only integers and floats are allowed")

# Returns n rounded to the nearest higher integer

def ceil(n):
    try: return int(n) + 1
    except: raise TypeError("Only integers and floats are allowed")

def binary(n):
    try: return int(bin(n)[2:])
    except: raise TypeError("Only positive integers are allowed")

def decimal(n):
    try: return int(str(n), 2)
    except: raise TypeError("Only integers and strings representing a binary number are allowed")





def sqrt(n, decimalPlaces=2):
    assert isinstance(n, (int, float)), "Only positive integers and floats are allowed"
    root = round(n**0.5, decimalPlaces)
    if int(root) == root: return int(root)
    return root
   
def cbrt(n, decimalPlaces=2):
    assert isinstance(n, (int, float)), "Parameters can only be int and float"
    root = round(n**(1/3), decimalPlaces)
    if int(root) == root: return int(root)
    return root

def root(n, exponent, decimalPlaces=2):
    assert isinstance(n, (int, float)), "Parameters can only be int and float"
    root = round(n**(1/exponent), decimalPlaces)
    if int(root) == root: return int(root)
    return root


