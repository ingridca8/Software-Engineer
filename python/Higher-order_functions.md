# Introduction to Higher-Order functions
In Python, all functions, including the ones we’ve written, are classified as first-class objects (sometimes also called first-class citizens or first-class functions). This means they have four important characteristics:

    First-class objects can be stored as variables.
    First-class objects can be passed as arguments to a function.
    First-class objects can be returned by a function.
    First-class objects can be stored in data structures (e.g., lists, dictionaries, etc.).

We may have taken this functionality for granted before if we ever assigned a function to a variable or stored a function in a list.

But the fact that functions are first-class objects in Python, and therefore have all the flexibility of objects, enables us to write even more powerful types of functions called higher-order functions.

Higher-order functions operate on other functions via arguments or via return values. This means higher-order functions do one or both of the following:

    Accept a function as an argument
    Have a return value that is a function

## Functions as arguments
Take a look at the example higher-order function called total_bill():

>>> def total_bill(func, value):
>>>   total = func(value)
>>>   return total

The total_bill() function takes two arguments: func and value. When called, total_bill() applies func() to value and returns the result. In order to see it in action, let’s define a function called, add_tax(), and then pass it to our higher-order total_bill() function along with a numeric value:

>>> def add_tax(total):
>>>   tax = total * 0.06
>>>   new_total = total + tax
>>>   return new_total
>>>  
>>> total_bill(add_tax, 100)

Here, total_bill() is classified as a higher-order function because it takes in an argument that is a function (add_tax() in the above example). 

Now, no matter the function we pass as the argument and the behavior we want the function to accomplish, we can always consistently format the total and add a friendly message to the returned result. While we are only adding on a small manipulation at this point, we can really do any consistent manipulation that increases our code reuse and makes our programs more modular. This isn’t the only situation where higher-order functions shine, they are also fantastic for situations involving iteration!

## Wrapper function (First-Order functions)
Wrapper function or decorator allows us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it. In Decorators, functions are taken as the argument into another function and then called inside the wrapper function. To know more about decorator click here.

Below is the example of a simple decorator.

# defining a decorator  
def hello_decorator(func):  
    
    # inner1 is a Wrapper function in   
    # which the argument is called  
        
    # inner function can access the outer local  
    # functions like in this case "func"  
    def inner1():  
        print("Hello, this is before function execution")  
    
        # calling the actual function now  
        # inside the wrapper function.  
        func()  
    
        print("This is after function execution")  
            
    return inner1  
    
    
# defining a function, to be called inside wrapper  
def function_to_be_used():  
    print("This is inside the function !!")  
    
    
# passing 'function_to_be_used' inside the  
# decorator to control its behavior  
function_to_be_used = hello_decorator(function_to_be_used)  
    
    
# calling the function  
function_to_be_used()  

Output:

Hello, this is before function execution
This is inside the function !!
This is after function execution

## Functions as Arguments - Iteration

