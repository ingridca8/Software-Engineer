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
