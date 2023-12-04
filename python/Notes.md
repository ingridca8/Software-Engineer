## raise keyword

The raise keyword is used to raise an exception.

You can define what kind of error to raise, and the text to print to the user.

**Examples**

    if not type(x) is int:
    raise TypeError("Only integers are allowed") 

    if x < 0:
    raise Exception("Sorry, no numbers below zero")

## isinstance() Function

The isinstance() function returns True if the specified object is of the specified type, otherwise False.

If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.

**Syntax**

    isinstance(object, type)

**Examples**

    Check if "Hello" is one of the types described in the type parameter:
    x = isinstance("Hello", (float, int, str, list, dict, tuple)) 
