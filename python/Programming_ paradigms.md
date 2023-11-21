# Programming paradigms
The term programming paradigm refers to a style of programming. It does not refer to a specific language, but rather it refers to the way you program.

There are lots of programming languages that are well-known but all of them need to follow some strategy when they are implemented. And that strategy is a paradigm.

## Imperative programming paradigms

The paradigm consists of several statements, and after the execution of all of them, the result is stored. It’s about writing a list of instructions to tell the computer what to do step by step.

In an imperative programming paradigm, the order of the steps is crucial, because a given step will have different consequences depending on the current values of variables when the step is executed.

### Procedural programming paradigm

Procedural programming (which is also imperative) allows splitting those instructions into procedures.

**NOTE**: Procedures aren't functions. The difference between them is that functions return a value, and procedures do not. More specifically, functions are designed to have minimal side effects, and always produce the same output when given the same input. Procedures, on the other hand, do not have any return value. Their primary purpose is to accomplish a given task and cause a desired side effect.

A great example of procedures would be the well known for loop. The for loop's main purpose is to cause side effects and it does not return a value.

Languages that support the procedural programming paradigm are:

  +  C
  +  C++
  +  Java
  +  ColdFusion
  +  Pascal

Procedural programming is often the best choice when:

  + There is a complex operation which includes dependencies between operations, and when there is a need for clear visibility of the different application states ('SQL loading', 'SQL loaded', 'Network online', 'No audio hardware', etc). This is usually appropriate for application startup and shutdown (Holligan, 2016).
  + The program is very unique and few elements were shared (Holligan, 2016).
  + The program is static and not expected to change much over time (Holligan, 2016).
  + None or only a few features are expected to be added to the project over time (Holligan, 2016).

### Object-Oriented programming

OOP is the most popular programming paradigm because of its unique advantages like the modularity of the code and the ability to directly associate real-world business problems in terms of code.

    Object-oriented programming offers a sustainable way to write spaghetti code. It lets you accrete programs as a series of patches.
    ― Paul Graham

The key characteristics of object-oriented programming include Class, Abstraction, Encapsulation, Inheritance and Polymorphism.

A class is a template or blueprint from which objects are created.

Objects are instances of classes. Objects have attributes/states and methods/behaviors. Attributes are data associated with the object while methods are actions/functions that the object can perform.

Languages that support the object-oriented paradigm:

   + Python
   + Ruby
   + Java
   + C++
   + Smalltalk

Object-oriented programming is best used when:

  + You have multiple programmers who don’t need to understand each component (Holligan, 2016).
  + There is a lot of code that could be shared and reused (Holligan, 2016).
  + The project is anticipated to change often and be added to over time (Holligan, 2016).
    
### Parallel processing aproach

Parallel processing is the processing of program instructions by dividing them among multiple processors.

A parallel processing system allows many processors to run a program in less time by dividing them up.

Languages that support the Parallel processing approach:

  + NESL (one of the oldest ones)
  + C
  + C++

Parallel processing approach is often the best use when:

  + You have a system that has more than one CPU or multi-core processors which are commonly found on computers today.
  + You need to solve some computational problems that take hours/days to solve even with the benefit of a more powerful microprocessor.
  + You work with real-world data that needs more dynamic simulation and modeling.

## Declarative programming paradigms

Declarative programming is a style of building programs that expresses the logic of a computation without talking about its control flow.

Declarative programming is a programming paradigm in which the programmer defines what needs to be accomplished by the program without defining how it needs to be implemented. In other words, the approach focuses on what needs to be achieved instead of instructing how to achieve it.

Imagine the president during the state of the union declaring their intentions for what they want to happen. On the other hand, imperative programming would be like a manager of a McDonald's franchise. They are very imperative and as a result, this makes everything important. They, therefore, tell everyone how to do everything down to the simplest of actions.

So the main differences are that imperative tells you how to do something and declarative tells you what to do. 

### Logic programming paradigm

The logic programming paradigm takes a declarative approach to problem-solving. It's based on formal logic.

The logic programming paradigm isn't made up of instructions - rather it's made up of facts and clauses. It uses everything it knows and tries to come up with the world where all of those facts and clauses are true.

For instance, Socrates is a man, all men are mortal, and therefore Socrates is mortal. 

Languages that support the logic programming paradigm:

  + Prolog
  + Absys
  + ALF (algebraic logic functional programming language)
  + Alice
  + Ciao

Logic programming paradigm is often the best use when:

  + If you're planning to work on projects like theorem proving, expert systems, term rewriting, type systems and automated planning.
    
### Functional programming

The functional programming paradigm has been in the limelight for a while now because of JavaScript, a functional programming language that has gained more popularity recently.

The functional programming paradigm has its roots in mathematics and it is language independent. The key principle of this paradigm is the execution of a series of mathematical functions.

You compose your program of short functions. All code is within a function. All variables are scoped to the function.

In the functional programming paradigm, the functions do not modify any values outside the scope of that function and the functions themselves are not affected by any values outside their scope.

Languages that support functional programming paradigm:

  +  Haskell
  +  OCaml
  +  Scala
  +  Clojure
  +  Racket
  +  JavaScript

Functional programming paradigm is often best used when:

  +  Working with mathematical computations.
  +  Working with applications aimed at concurrency or parallelism.

### Database processing aproach

This programming methodology is based on data and its movement. Program statements are defined by data rather than hard-coding a series of steps.

A database is an organized collection of structured information, or data, typically stored electronically in a computer system. A database is usually controlled by a database management system (DBMS) ("What is a Database", Oracle, 2019).

To process the data and querying them, databases use tables. Data can then be easily accessed, managed, modified, updated, controlled and organized.

A good database processing approach is crucial to any company or organization. This is because the database stores all the pertinent details about the company such as employee records, transaction records and salary details.

Most databases use **Structured Query Language (SQL)** for writing and querying data.

Database processing approach is often best used when:

  + Working with databases to structure them.
  + Accessing, modifying, updating data on the database.
  + Communicating with servers.
