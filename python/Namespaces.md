# Namespaces
## What are namespaces
A namespace is a collection of currently defined symbolic names along with information about the object that each name references. You can think of a namespace as a dictionary in which the keys are the object names and the values are the objects themselves. Each key-value pair maps a name to its corresponding object.

![alt text]([https://assets.digitalocean.com/articles/alligator/boo.svg](https://static-assets.codecademy.com/Courses/Intermediate-Python/Types-of-Namespaces_final.svg) "Namespaces")

As Tim Peters suggests, namespaces aren’t just great. They’re honking great, and Python uses them extensively. In a Python program, there are four types of namespaces:

    Built-In
    Global
    Enclosing
    Local

These have differing lifetimes. As Python executes a program, it creates namespaces as necessary and deletes them when they’re no longer needed. Typically, many namespaces will exist at any given time.
## Built in Namespaces
The built-in namespace contains the names of all of Python’s built-in objects. These are available at all times when Python is running. You can list the objects in the built-in namespace with the following command:

 dir(__ builtins __)

Let’s note a few interesting facts about the objects hosted built-in namespace:

    It contains many of the built-in functions we are able to use in our Python programs such as str(), zip(), slice(), sorted(), and many more.
    It also hosts many of the exceptions that we may encounter in our programs such as 'ArithmeticError', 'IndexError', 'KeyError', and many more.
    There are even constants like True and False

## Global Namespace
The global namespace exists one level below the built-in namespace. Generally, it includes all non-nested names in the module (file) we are choosing to run the Python interpreter on. The global namespace is created when we run our main program and has a lifetime until the interpreter terminates (usually when our program is finished running).

Thankfully, in order to see what objects exist in the global namespace, Python provides the globals() built-in function. 
The global namespace contains all of the non-nested objects of our program.

Anytime we use the import statement to bring in a new module into our program, instead of adding every name from that module to our current global namespace, Python will create a new namespace for it. This means there might be potentially multiple global namespaces in a single program.

## Local Namespaces
In Python, whenever the interpreter executes a function, it will generate a local namespace for that specific function. This namespace only exists inside of the function and remains in existence until the function terminates.

Similar to how we can see the global namespace using a built-in function called globals(), Python provides a function called locals() to see any generated local namespace.

## Enclosing Namespaces
There is just one more namespace we need to be aware of in our Python programs. This particular namespace is a special type of local namespace called the enclosing namespace.

Enclosing namespaces are created specifically when we work with nested functions and just like with the local namespace, will only exist until the function is done executing.

global_variable = 'global'

def outer_function():
  outer_value = "outer"

  def inner_function():
    inner_value = "inner"

 inner_function()

outer_function()

In this program, the following occurs:

    We define a function called outer_function() and nest another function inside it called inner_function(). To generate a namespace, functions must be executed, so we are calling both of them.
    Here, The outer_function() serves the role of an enclosing function while inner_function is an enclosed function. By creating this structure, we generate an enclosing namespace - a namespace created by an enclosing function and any number of enclosed functions inside it.

While Python doesn’t give us any particular function like enclosing() to visualize the namespace, we can use locals() to see when enclosed namespaces are generated.



