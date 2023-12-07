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

## Built-in Exceptions

In the previous exercise (and probably many times before), we saw one type of exception called the NameError. The NameError is just one of the many built-in exceptions — exceptions that are built into the Python language. Other built-in exceptions cover fields ranging from mathematical errors all the way to operating system errors. We don’t need to memorize them all, but it’s helpful to be familiar with some common ones and, more importantly, understand where they come from inside Python.

Exceptions are objects just like anything else. Most exceptions inherit directly from a class called Exception; however, they all are derived directly or indirectly from the BaseException class. We can examine the base classes by using the __ bases__ attribute on any specific exception:

    print(NameError.__bases__)

Will output:

    <class 'Exception'>

We can even call __ bases__ on the Exception class to see its origins:

    print(Exception.__bases__)

Will output:

    <class 'BaseException'>

The full hierarchy of built-in exceptions is the following:

    BaseException
     +-- Exception
          +-- StopIteration
          +-- StopAsyncIteration
          +-- ArithmeticError
          |    +-- FloatingPointError
          |    +-- OverflowError
          |    +-- ZeroDivisionError
          +-- AssertionError
          +-- AttributeError
          +-- BufferError
          +-- EOFError
          +-- ImportError
          |    +-- ModuleNotFoundError
          +-- LookupError
          |    +-- IndexError
          |    +-- KeyError
          +-- MemoryError
          +-- NameError
          |    +-- UnboundLocalError
          +-- OSError
          |    +-- BlockingIOError
          |    +-- ChildProcessError
          |    +-- ConnectionError
          |    |    +-- BrokenPipeError
          |    |    +-- ConnectionAbortedError
          |    |    +-- ConnectionRefusedError
          |    |    +-- ConnectionResetError
          |    +-- FileExistsError
          |    +-- FileNotFoundError
          |    +-- InterruptedError
          |    +-- IsADirectoryError
          |    +-- NotADirectoryError
          |    +-- PermissionError
          |    +-- ProcessLookupError
          |    +-- TimeoutError
          +-- ReferenceError
          +-- RuntimeError
          |    +-- NotImplementedError
          |    +-- RecursionError
          +-- SyntaxError
          |    +-- IndentationError
          |         +-- TabError
          +-- SystemError
          +-- TypeError
          +-- ValueError
          |    +-- UnicodeError
          |         +-- UnicodeDecodeError
          |         +-- UnicodeEncodeError
          |         +-- UnicodeTranslateError

Note that there are a lot of exceptions built into the language of Python. Is not necessary to know them all but it's good to know they exists.

## Raising Exceptions

Encountering exceptions isn’t always an accident. We can throw an exception at any time by using the raise keyword, even when Python would not normally throw it.

We might want to raise an exception anytime we think a mistake has or will occur in our program. This lets us stop program execution immediately and provide a useful error message instead of allowing mistakes to occur that may be difficult to diagnose at a later point.

One way to use the raise keyword is by pairing it with a specific exception class name. We can either call the class by itself or call a constructor and provide a specific error message. So for example we could do:

    raise NameError
    # or 
    raise NameError('Custom Message')

When only the class name is provided (as in the first example), Python calls the constructor method for us without any arguments (and thus no custom message will come up).

For a more concrete example, let’s examine raising a TypeError for a function that checks if an employee tries to open the cash register but does not have the correct access:

    def open_register(employee_status):
      if employee_status == 'Authorized':
        print('Successfully opened cash register')
      else:
        # Alternatives: raise TypeError() or TypeError('Message')
        raise TypeError

When an employee_status is not 'Authorized', the function open_register() will throw a TypeError and stop program execution.

Alternatively, when no built-in exception makes sense for the type of error our program might experience, it might be better to use a generic exception with a specific message. This is where we can use the base Exception class and provide a single argument that serves as the error message. Let’s modify the previous example, this time raising an Exception object with a message:

    def open_register(employee_status):
      if employee_status == 'Authorized':
        print('Successfully opened cash register')
      else:
        raise Exception('Employee does not have access!')

As a general rule of thumb, use an exception that provides the best explanation for the expected error for both the user and anyone that will read the code.

## Try / Except

So far, the exceptions we’ve encountered have caused our programs to stop executing. However, it is possible for programs to continue executing even after encountering an exception. This process is known as exception handling and is accomplished using the Python try/except clauses.

The following flow chart demonstrates the mechanics of try/except:

[Try/exception](https://static-assets.codecademy.com/Courses/Intermediate-Python/Flow%20diagram%202.svg)

Let’s break it down:

  +  Python will first attempt to execute code inside the try clause code block.
  +  If no exception is encountered in the code, the except clause is skipped and the program continues normally.
   + If an exception does occur inside of the try code block, Python will immediately stop executing the code and begin executing the code inside the except code block (sometimes called a handler).

Let’s see this in action in a small program that prints colors:

    colors = {
        'red': '#FF0000',
        'blue': '#0000FF',
        'yellow': '#FFFF00',
    }

    for color in ('red', 'green', 'yellow'):
      try:
        print('The hex value of ' + color + ' is ' + colors[color])
      except:
        print('An exception occurred! Color does not exist.')
      print('Loop continues...')

We get the following output:

    The hex value of red is #FF0000
    Loop continues...
    An exception occurred! Color does not exist.
    Loop continues...
    The hex value of yellow is #FFFF00
    Loop continues...

In the above code, the try block runs until it hit an exception. The hex value of the color red was successfully printed before it tried to access the hex value of green, which caused a KeyError since green is not in our colors dictionary and ran the code in the except block. However, the exception was handled so Python continued executing our code and went onto print the hex value of yellow.

Exception handling is a powerful tool that lets us gain more flexibility in dealing with errors in our applications. We can use it to perform an action multiple times until it succeeds, or perhaps simply print a message when a non-critical part of our program doesn’t work properly. 
