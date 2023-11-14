In Python, a lambda function (also commonly called an anonymous function) is a one-line shorthand for function. 

>> def add_two(my_input):
>>
>> 
>>   return my_input + 2

The same function could be written as a lambda function:

>> add_two = lambda my_input: my_input + 2

Let’s break this syntax down:

    The function is stored in a variable called add_two.
    The lambda keyword declares that this is a lambda function (similar to how we use def to declare a normal function).
    my_input is a parameter used to hold the value passed to add_two.
    In the lambda function version, we are returning my_input + 2 without the use of a return keyword (the normal Python function explicitly uses the keyword return).

Our lambda functions can be more complex than the above example. For instance, let’s say we want a function that will perform differently based on different inputs.

Let’s say that we have a function check_if_A_grade that outputs 'Got an A!' if a grade is at least 90, and otherwise says you 'Did not get an A.'.

We can do this using a conditional if statement in a lambda function, with syntax that looks like this:

>> check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A.'

This is what our line of code does:

    lambda grade: declares a lambda function with the parameter grade
    Return 'Got an A!' if this statement is true.
    Otherwise, return 'Did not get an A.'

Lambda functions are the preferred way of creating one-line functions. The reduced syntax assists code readability and the functions can be implemented where code reuse is not the primary objective. If we wanted our function complexity to extend beyond one line, we would opt for a regular function since making our function longer would impair readability. 


