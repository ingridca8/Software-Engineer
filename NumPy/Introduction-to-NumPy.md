# NumPy
[NumPy Documentation](https://docs.scipy.org/doc/)

NumPy is great at storing and manipulating numerical data in arrays.

## Import NumPY
To use NumPy with Python, import it at the top of your file using the following line:

    import numpy as np

Writing as np allows us to use np as a shorthand for NumPy, which saves us time when calling a NumPy function (less typing = fewer errors!)

## NumPy Arrays

NumPy includes a powerful data structure known as an array. A NumPy array is a special type of list. It’s a data structure that organizes multiple items. Each item can be of any type (strings, numbers, or even other arrays).

Arrays are most powerful when they are used to store numbers. This is because arrays give us special ways of performing mathematical operations that are both simpler to write and more efficient computationally. 

A NumPy array looks a lot like a Python list:

    my_array = np.array([1, 2, 3, 4, 5, 6])

We can transform a regular list into a NumPy array by using np.array() and saving the value to a new variable:

    my_list = [1, 2, 3, 4, 5, 6]
    my_array = np.array(my_list)

## Creating an Array from a CSV

Typically, you won’t be entering data directly into an array. Instead, you’ll be importing the data from somewhere else.

We’re able to transform CSV (comma-separated values) files into arrays using the np.genfromtxt() function:

Consider the following CSV, sample.csv,

    34,9,12,11,7

We can import this into a NumPy array using the following code:

    csv_array = np.genfromtxt('sample.csv', delimiter=',')

Note that in this case, our file sample.csv has values separated by commas, so we use delimiter=',', but sometimes you’ll find files with other delimiters, the most common being tabs or colons. 

