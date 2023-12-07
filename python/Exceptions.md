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

## Catching Specific Exceptions

The exception handlers from the previous exercise handled any exception hit during the try clause. However, in most cases, we will have an idea of the types of exceptions that might occur within our code. It is generally considered best practice to be as specific as possible with the exceptions we want to raise unless there is a specific reason for catching any type of exception.

We can catch a specific exception by listing it after the except keyword, as in the example below:

    try:
        print(undefined_var)
    except NameError:
        print('We hit a NameError')
    
In this case, the except block is only executed if a NameError is encountered (in the try block) rather than any exception. If any other exception occurs, it is unhandled, and the program terminates.

When we specify exception types, Python also allows us to capture the exception object using the as keyword. The exception object hosts information about the specific error that occurred. Examine our previous function but now capturing the exception object as errorObject:

    try:
        print(undefined_var)
    except NameError as errorObject:
        print('We hit a NameError')
        print(errorObject)

Would output:

    We hit a NameError
    name 'undefined_var' is not defined

Its worth noting errorObject is an arbitrary name and can be replaced with any name we see fit. The following code would work exactly the same:

    try:
        print(undefined_var)
    except NameError as e:
        print('We hit a NameError')
        print(e)

## Handling Multiple Exceptions

While handling a single exception is useful, Python also gives us the ability to handle multiple exceptions at once. We can list more than one exception type in a tuple with a single except clause. Here is what the syntax would look like:

    try:
        # Some code to try!
    except (NameError, ZeroDivisionError) as e:
        print('We hit an Exception!')
        print(e)

In the above example, we expect to encounter either a NameError or a ZeroDivisionError. We can list any number of exceptions in this tuple format as long as it makes sense for the code in our try block. This is where we can see the benefit of capturing our exception object (via the as clause) since it enables us to print (or operate on) the specific exception that is caught.

In addition to catching multiple exceptions, we can also pair multiple except clauses with a single try clause, enabling specific exceptions to be handled differently. For example:

    try:
        # Some code to try!
    except NameError:
        print('We hit a NameError Exception!')
    except KeyError:
        print('We hit a TypeError Exception!')
    except Exception:
        print('We hit an exception that is not a NameError or TypeError!')

## The else Clause

We’ve seen how exception handlers get executed when we encounter exceptions during a try clause - but what if we want to run some code only if we do not encounter an exception? Python provides us a way to do this as well - the else clause.

Our updated flow chart shows what happens when an else clause is added to the mix:

[Try/Except/Else](https://static-assets.codecademy.com/Courses/Intermediate-Python/Flow%20diagram%203.svg)

Python will only execute the else clause if no exception was encountered in the try clause.

Let’s examine a hypothetical program that authenticates a user. For now, we will use two imaginary functions check_password() and login_user(). Here is what the program looks like:

    try:
      check_password()
    except ValueError:
      print('Wrong Password! Try again!')
    else:
      login_user()
      # 20 other lines of imaginary code

In this program, we can assume if our function check_password() fails, it will return a ValueError. Thankfully, our exception handler takes care of this scenario. However, if our function doesn’t fail, the else clause allows us to log the user in!

Now, one could argue, we could have written our program a different way to achieve a similar outcome:

    try:
      check_password()
      login_user()
      # 20 other lines of imaginary code
    except ValueError:
      print('Wrong Password! Try again!')

Here, if our check_password() ever fails, we will be able to catch the exception just like before. Python does offer a bit of insight on this scenario in the official documentation:

>    The use of the else clause is better than adding additional code to the try clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the try … except statement.

This suggestion is valid in this case since in the alternative style, the ValueError could occur in any of the other lines of code other than check_password(), and it would be challenging to tell where it came from.

## The finally Clause

With try/except/else, we’ve seen how to run certain code when an exception occurs and other code when it does not. There is also a way to execute code regardless of whether an exception occurs - the finally clause.

Here is our final flow chart demonstrating try/except/else/finally:





## User-defined Exceptions



## Customizing User-defined Exceptions
