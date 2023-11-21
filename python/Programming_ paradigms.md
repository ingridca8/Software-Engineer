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

### functional programming
### Database processing aproach

