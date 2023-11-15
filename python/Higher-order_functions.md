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

     def total_bill(func, value):
        total = func(value)
        return total

The total_bill() function takes two arguments: func and value. When called, total_bill() applies func() to value and returns the result. In order to see it in action, let’s define a function called, add_tax(), and then pass it to our higher-order total_bill() function along with a numeric value:

     def add_tax(total):
       tax = total * 0.06
       new_total = total + tax
       return new_total
    
     total_bill(add_tax, 100)


Here, total_bill() is classified as a higher-order function because it takes in an argument that is a function (add_tax() in the above example). 

Now, no matter the function we pass as the argument and the behavior we want the function to accomplish, we can always consistently format the total and add a friendly message to the returned result. While we are only adding on a small manipulation at this point, we can really do any consistent manipulation that increases our code reuse and makes our programs more modular. This isn’t the only situation where higher-order functions shine, they are also fantastic for situations involving iteration!

## Functions as Arguments - Iteration
Let’s return to our total_bill() example. Now say we have a list of bills instead of just one, and we want to add tax or tip to each bill, depending on the type of sale it is.

One way to accomplish this could be to write out separate loops: one for sales that need to have tax added and one for sales that should have a tip added.

Now, we could write out another loop for when we need to add a tip instead of tax, but we can probably guess how many repetitions would be involved. A much more powerful solution would be to use a higher-order function to apply add_tax() or add_tip() to each balance in our list. Lets first define a higher-order function, total_bills(), that takes a function and a list as arguments, applies the function to each element in the list, standardizes the format of the result and adds a friendly message, appends the output to a new list, and finally returns the updated new list.

    def total_bills(func, list):
      #This list will store all the new bill values
      new_bills = []

      #This loop will iterate through our bills
      for i in range(len(list)):

        # Here we apply the function to each element of the list!
        total = func(list[i])
        new_bills.append("Total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")

      return new_bills

Next, let’s use the add_tax() function that we wrote before with our new total_bills() higher-order function:

    bills = [115, 120, 42]
 
    bills_w_tax = total_bills(add_tax, bills)
 
    print(bills_w_tax)

Would output:

    ['Total amount owed is $121.90. Thank you! :)',
     'Total amount owed is $127.20. Thank you! :)',
     'Total amount owed is $44.52. Thank you! :)']

And if we needed to add a tip instead of tax, we could simply swap out the function argument:

    bills_w_tip = total_bills(add_tip, bills)
 
    print(bills_w_tip)

Would output:

    ['Total amount owed is $138.00. Thank you! :)',
     'Total amount owed is $144.00. Thank you! :)',
     'Total amount owed is $50.40. Thank you! :)']

As these examples show, being able to pass functions in as arguments can be pretty handy, especially when we want to apply a function multiple times. In fact, it’s so handy that there’s a built-in higher-order function in Python that does just that—the map() function. 

## Functions as Return Values

So far, we have focused on higher-order functions that take another function as an argument. Remember, though, that a function that returns another function is also a higher-order function. Let’s see what this looks like in practice by considering a higher-order function, make_box_volume_function(), that will help us calculate the volumes of boxes when they have the same height:

    def make_box_volume_function(height):
        # defines and returns a function that takes two numeric arguments,        
        # length &  width, and returns the volume given the input height
        def volume(length, width):
            return length*width*height
    
        return volume
 
    box_volume_height15 = make_box_volume_function(15)
 
    print(box_volume_height15(3,2))

Would output:

    90

And if we had slightly shorter boxes:

    box_volume_height10 = make_box_volume_function(10)
     
    print(box_volume_height10(3,2))

Would output:

    60

In the example, we wrote a higher-order function, make_box_volume_function(), that takes a height as an argument and returns a new function that calculates the volume of any box with that height when it is passed the length and width of the box. As we can see, higher-order functions with functions as return values are just as reusable as higher-order functions with functions as arguments and, therefore, also reduce repetition and the chances for mistakes to creep into code.

# Built-In Higher-Order Functions
## Map

The map() higher-order function has the following base structure:

    returned_map_object = map(function, iterable)

When called, map() applies the passed function to each and every element in the iterable and returns a map object. The returned map object holds the results from applying the mapping function to each element in the passed iterable. We will usually convert the map into a list to enable viewing and further use. 

    def double(x):
     return x*2
     
    int_list = [3, 6, 9]
     
    doubled = map(double, int_list)
     
    print(doubled)
    
Would output:

    <map at 0x7f1ca0f58090>

In our example:

+ We defined a function called double() that takes in a value and returns the value doubled. This function can be used anywhere in our program—not only with map().
+ We also defined an iterable (int_list) that we wanted to apply the function to.
+ We then passed the function reference double as the function argument and int_list as the iterable to map()
     The map() function proceeded to apply double() onto each element in int_list.
+ When we printed the result, we could see that the output of the map() function was a specific type of object called a map object.

If we want to see the actual results of mapping double() to the elements of int_list, we need to convert the map object to a list using the built-in list() function:

    print(list(doubled))

This would output:

    [6, 12, 18]

Higher-order functions like map() work especially well with lambda functions. Because lambda functions are anonymous, we don’t need to define a new named function for map() if that function won’t be used again elsewhere. In this case, if we don’t plan on reusing double() somewhere else in our program, we can rewrite the double() function from the previous example with a lambda function like so:

    doubled = map(lambda input: input*2, int_list)
     
    print(list(doubled))

This would output:

    [6, 12, 18]

Using a lambda function with map() produced the same output as when the custom double() function was passed to map(), but it only required one line of code instead of three. Now let’s practice using map() to apply a lambda function to each element in a list. 

## Filter

Similar to map(), the filter() function takes a function and an iterable as arguments. Just as the name suggests, the goal of the filter() function is to “filter” values out of an iterable.

The filter() function accomplishes this goal by applying a passed filtering function to each element in the passed iterable. The filtering function should be a function that returns a boolean value: True or False. The returned filter object will hold only those elements of the passed iterable for which the filtering function returned True. 

