# Introduction to Iterables

In Python, an iterable is an object that is capable of being looped through one element at a time. We commonly use iterables to perform the process of iteration and it is the backbone for how we perform consistent operations on sets of data.

While these may be new terminologies, we have actually been using iterables frequently. Dictionaries, lists, tuples, and sets are all classified as iterables! We have even performed the process of iteration anytime we used looping mechanisms such as for loops.

## Iterator Objects: __iter__() and iter()
An iterator object is a special object that represents a stream of data that we can operate on. To accomplish this, it uses a built-in function called **iter()**.

To go behind the scenes even further, iter(list) is actually calling a method defined within the iterable called __iter__(). All iterables have this __iter__() method defined. 

In summary, the __iter__() method simply returns the iterator object that allows us to iterate over the iterable. Calling list.__iter__() will retrieve the same iterator object as calling iter(list). This means that the built-in function iter() and the iterable’s method __iter__() can be used interchangeably. While the object itself might not seem super useful just yet, we’ll see how to manipulate the stream of data inside of it in the next exercises. 

