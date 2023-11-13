# Namespaces
## What are namespaces
A namespace is a collection of currently defined symbolic names along with information about the object that each name references. You can think of a namespace as a dictionary in which the keys are the object names and the values are the objects themselves. Each key-value pair maps a name to its corresponding object.
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
