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
