# Unit testing
## Introduction to testing

When working with Python, or any programming language, there is a lot that can go wrong with our code. There are syntax errors and exceptions, but there are also mistakes in the program logic which cause it to behave in unexpected ways.

For these reasons, testing is crucial to creating quality software. The goal of testing isn’t just to find bugs but to find them quickly. Leaving bugs unfound and unresolved can lead to massive consequences in the real world.

The world of testing can generally be divided into two categories:

   + Manual Testing:
        + With manual testing, a physical person interacts with software much as a user would. In fact, we have been manually testing our code any time we run it and observe the results!
   + Automated Testing:
        + With automated testing, tests are performed with code. Generally, automated testing is faster and less prone to human error.

## The assert Statement

While some code are simple to test, most code will be much more complex. It would be very tedious to have to perform these tests manually. Our time would be better spent writing automated tests.

Luckily, Python provides an easy way to perform simple tests in our code - the **assert** statement. An assert statement can be used to test that a condition is met. If the condition evaluates to False, an AssertionError is raised with an optional error message.

The general syntax looks like this:

    assert <condition>, 'Message if condition is not met'

An assert statement is a quick and powerful way to verify that a program is in the correct state. They can be used to catch mistakes early and make sure we avoid any catastrophes.

## Unit Testing

Assertion statements are a good start to ensuring our programs are being tested, but they don’t necessarily tell us what we should test. Generally, we can start by testing the smallest unit of a program. 

In programming, these types of individual tests are called unit tests. We can test a single unit of a program, such as a function, loop, or variable. A unit test validates a single behavior and will make sure all of the units of a program are functioning properly. 

Let’s say we wanted to test a single function (a single unit). To test a single function, we might create several test cases. A test case validates that a specific set of inputs produces an expected output for the unit we are trying to test.

      # The unit we want to test
      def times_ten(number):
          return number * 10

      # A unit test function with a single test case
      def test_multiply_ten_by_zero():
          assert times_ten(0) == 0, 'Expected times_ten(0) to return 0'

We can create as many test cases as we see fit for a single unit, and we should try to test all the unique types of inputs our unit will work with. 

## Python's unittest Framework

There are some problems with the approach to our previous unit tests that would make them difficult to maintain. First, we had to call each function specifically when a new test was created. We also didn’t have any way of grouping tests, which is necessary when the number of tests increases. Perhaps most importantly, if one test failed, the AssertionError would prevent any remaining tests from running!

Luckily, Python provides a framework that solves these problems and provides many other tools for writing unit tests. This framework lives in the unittest module which is included in the standard library. It can be imported like so:

      import unittest

The unittest module provides us with a test runner. A test runner is a component that collects and executes tests and then provides results to the user. The framework also provides many other tools for test grouping, setup, teardown, skipping, and other features that we’ll soon learn about. 

      import unittest

      # Function that gets tested
      def times_ten(number):
          return number * 100

      # Test class
      class TestTimesTen(unittest.TestCase):
          def test_multiply_ten_by_zero(self):
              self.assertEqual(times_ten(0), 0, 'Expected times_ten(0) to return 0')

          def test_multiply_ten_by_one_million(self):
              self.assertEqual(times_ten(1000000), 10000000, 'Expected times_ten(1000000) to return 10000000')

          def test_multiply_ten_by_negative_number(self):
              self.assertEqual(times_ten(-10), -100, 'Expected add_times_ten(-10) to return -100')
      
      # Run the tests
      unittest.main()

## Assert Methods I: Equality and Membership

The framework relies on built-in assert methods instead of assert statements to track results without actually raising any exceptions. Specific assert methods take arguments instead of a condition, and like assert statements, they can take an optional message argument.

Let’s go over three commonly used assert methods for testing equality and membership, their general syntax, and their assert statement equivalents.

   + assertEqual: The assertEqual() method takes two values as arguments and checks that they are equal. If they are not, the test fails.

           self.assertEqual(value1, value2)

  +  assertIn: The assertIn() method takes two arguments. It checks that the first argument is found in the second argument, which should be a container. If it is not found in the container, the test fails.

           self.assertIn(value, container)

  +  assertTrue: The assertTrue() method takes a single argument and checks that the argument evaluates to True. If it does not evaluate to True, the test fails.

           self.assertTrue(value)

The equivalent assert statements would be the following:
| Method |	Equivalent |
| --- | --- |
| self.assertEqual(2, 5) |	assert 2 == 5 |
| self.assertIn(5, [1, 2, 3]) |	assert 5 in [1, 2, 3] |
| self.assertTrue(0) |	assert bool(0) is True |

The full list for equality and membership can be seen in the [Python documentation](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug).

## Assert Methods II: Quantitative Methods

Often we need to test conditions related to numbers. The unittest module provides a handful of assert methods to achieve this. Let’s take a look at two common assert methods related to quantitative comparisons, their general syntax, as well as their assert statement equivalents.

  +  assertLess: The assertLess() method takes two arguments and checks that the first argument is less than the second one. If it is not, the test will fail.

           self.assertLess(value1, value2)

  +  assertAlmostEqual: The assertAlmostEqual() method takes two arguments and checks that their difference, when rounded to 7 decimal places, is 0. In other words, if they are almost equal. If the values are not close enough to equality, the test will fail.

           self.assertAlmostEqual(value1, value2)

The equivalent assert statements would be the following:

| Method |	Equivalent |
| --- | --- |
| self.assertLess(2, 5) |	assert 2 < 5 |
| self.assertAlmostEqual(.22, .225) |	assert round(.22 - .225, 7) == 0 |

The full list of quantitative methods can be seen in the [Python documentation](https://docs.python.org/3/library/unittest.html#unittest.TestCase.output).

## Assert Methods III: Exception and Warning Methods

There is another group of assert methods related to exceptions and warnings. Note that while we haven’t covered warnings in detail yet, they are a type of exception. Let’s go over two of these methods and their general syntax.

 +   assertRaises: The assertRaises() method takes an exception type as its first argument, a function reference as its second, and an arbitrary number of arguments as the rest.

 It calls the function and checks if an exception is raised as a result. The test passes if an exception is raised, is an error if another exception is raised, or fails if no exception is raised. This method can be used with custom exceptions as well!

       self.assertRaises(specificException, function, functionArguments...)

 +   assertWarns: The assertWarns() method takes a warning type as its first argument, a function reference as its second, and an arbitrary number of arguments for the rest.

   It calls the function and checks that the warning occurs. The test passes if a warning is triggered and fails if it isn’t.

     self.assertWarns(specificWarningException, function, functionArguments...)

There are no particular concise ways to replicate these tests using the assert keyword so it is recommended to use these methods instead when possible!

The full list of exception and warning methods can be seen in the [Python documentation](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNotIsInstance).

## Parameterizing Tests

In previous examples, we created test cases for the times_ten() function with various inputs. However, the actual logic of our tests really didn’t change. To decrease repetition, Python provides us a specific toolset for tests with only minor differences. This is known as test parameterization. By parameterizing tests, we can leverage the functionality of a single test to get a large amount of coverage of different inputs.

To accomplish test parameterization, the unittest framework provides us with the subTest context manager.

By using subTest, each iteration of our loop is treated as an individual test. Python will run the code inside of the context manager on each iteration, and if one fails, it will return the failure as a separate test case failure. 

The general syntax goes like follows:

      for loop
       print statement
       with statement using subTest()
           assertIn() test case

