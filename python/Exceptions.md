# Exceptions
## Introduction to Exceptions

It is truly an amazing feeling when our code works exactly the way we want it to. On the other hand, it can be equally frustrating when our code runs into errors. Since errors are such an integral part of working with Python, it’s important to know how to control errors and use them to our advantage effectively. In this lesson, we will explore a specific type of error, an exception.

At this point, we are probably very familiar with the most common type of error: a syntax error. Syntax errors are mistakes in the structure of Python code. They are caught during a special parsing stage before a program is executed. They always prevent the entire program from running. For example, here is the error output of a syntax error:

    File "script.py", line 1
      def print_five
                   ^
    SyntaxError: invalid syntax

As opposed to a syntax error, an exception is a different kind of error that can occur with syntactically correct code. Exceptions are runtime errors because they occur during program execution, only when the offending code (the code causing the error) is reached. An example of an exception, and one we have probably seen before, is a NameError:

    Traceback (most recent call last):
      File "script.py", line 1, in <module>
        print(five)
    NameError: name 'five' is not defined

Although the NameError has a similar output to a SyntaxError (both end with Error), it falls under the category of exceptions. Exceptions and syntax errors make up the two core categories for any error we will run into.

![Python Error Categories](https://static-assets.codecademy.com/Courses/Intermediate-Python/Types%20of%20Errors.svg "Error Categories")

We’ll encounter many different kinds of exceptions, some of which will be unfamiliar. Luckily, as we saw in the example above, Python gives us a tool for gaining insight into exceptions - the traceback. A traceback is a summary that includes the exception type, a message, and the series of function calls preceding the exception, along with file names and line numbers.






