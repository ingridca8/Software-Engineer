# Introduction to Iterables

In Python, an iterable is an object that is capable of being looped through one element at a time. We commonly use iterables to perform the process of iteration and it is the backbone for how we perform consistent operations on sets of data.

While these may be new terminologies, we have actually been using iterables frequently. Dictionaries, lists, tuples, and sets are all classified as iterables! We have even performed the process of iteration anytime we used looping mechanisms such as for loops.

## Iterator Objects: .__ iter __() and iter()
An iterator object is a special object that represents a stream of data that we can operate on. To accomplish this, it uses a built-in function called **iter()**.

To go behind the scenes even further, iter(list) is actually calling a method defined within the iterable called __iter__(). All iterables have this __ iter __() method defined. 

In summary, the __ iter __ () method simply returns the iterator object that allows us to iterate over the iterable. Calling list.__ iter __() will retrieve the same iterator object as calling iter(list). This means that the built-in function iter() and the iterable’s method __ iter __() can be used interchangeably. While the object itself might not seem super useful just yet, we’ll see how to manipulate the stream of data inside of it in the next exercises. 

## Iterator Objects:__ next __() and next()

Now that we used an iterator’s __ iter__() method to create an iterator object, how does our for loop know which value to retrieve on each iteration?

Well, the iterator object has a method called __ next__(), which retrieves the iterator’s next value. Let’s take a look using our SKU iterable for our shop:

    sku_list = [7046538, 8289407, 9056375, 2308597]
    sku_iterator = iter(sku_list)
    next_sku = sku_iterator.__next__()
    print(next_sku)

Running this code would produce the following result for next_sku:

    7046538

Similarly to __ iter__() and iter(), there is a Python built-in function called next() that we can use in place of calling the __ next__() method. Calling next() simply calls the iterator object’s __ next__() method.

But how does the iterator object know when to stop retrieving values? Does it keep calling __ next__() forever? Well, luckily __ next__() method will raise an exception called StopIteration when all items have been iterated through.

