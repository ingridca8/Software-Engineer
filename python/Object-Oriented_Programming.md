# Object-Oriented Programming

Object-oriented programming is a software development approach that focuses on defining and sculpting named classes as entities with attributes and behaviors. One key benefit of object-oriented programming? It makes reusing and maintaining code easier. 

Object-oriented programming (OOP) is a programming paradigm based on the concept of objects, which can contain data and code: data in the form of fields (often known as attributes or properties), and code in the form of procedures (often known as methods). 

## Building blocks of object-oriented programming 

The object-oriented programming paradigm uses the following building blocks to structure an application: 

### Classes 

Classes are user-defined data types used as a blueprint or template for the objects a software program will use in its operation. Classes define the methods and attributes that each object created from them has. Most object-oriented programming languages use classes, though some (like Go, for example) do not. 

### Objects 

In an object-oriented language that uses classes, objects are instances of those classes created with specific data. 

### Methods 

Methods are functions stated inside a class that define the behavior of the objects created from the class. They perform actions like returning information about the object or modifying the data contained in the object. 

### Attributes 

Attributes are variables defined inside a class that describe what data the objects created from the class will contain. 

## Pilars of Object-Orientatation

They're charactheristics or software design principles to help you write clean Object-Orientated code.

 + Inheritance
 + Encapsulation
 + Abstraction
 + Polymorphism

### Encapsulation

This principle means that all the important data and functionality of an object is contained within that object. Only select information that is needed outside of the object is exposed to the outside world. When an object is created from a class, the methods and attributes are encapsulated inside the object. Encapsulation also hides the implementation of this code inside the object. 

Encapsulation requires that you define some attributes and methods as public or private. “Public” dictates that the attributes and methods can be accessed, modified, or executed from the outside. “Private” limits access to use from inside the object. Attributes and methods can also be defined as protected. This means that classes that inherit from the parent class can also access these attributes and methods, just like the parent class. 

Encapsulation also adds a layer of security by preventing attributes from being changed or methods from being executed by the outside world, which can cause unintended data corruption.

The definition of encapsulation is "the action of enclosing something in or as if in a capsule". Removing access to parts of your code and making things private is exactly what Encapsulation is all about (often times, people refer to it as data hiding).

Encapsulation means that each object in your code should control its own state. State is the current "snapshot" of your object. The keys, the methods on your object, Boolean properties and so on. If you were to reset a Boolean or delete a key from the object, they're all changes to your state.

Limit what pieces of your code can access. Make more things inaccessible, if they aren't needed.

Why should we prefer privacy? Why not just have everything global?

   - Lots of unrelated bits of code will become dependent/coupled to one another via the global variable.
   - You will likely override the variables if the name get's reused, which can lead to bugs or unpredictable behaviour.
   - You will likely end up with Spaghetti Code – code that's hard to reason through and follow what is reading and writing to your variables and changing state.

### Abstraction

Abstraction is a means for providing a higher-level interface for interacting with objects. It extends the encapsulation principle by making only key attributes visible to a user and hiding the remaining complexity. This suggests that the complexity of the actual object can be represented by a simple class with a limited number of methods you can execute or attributes you can access. 

One way to imagine the concept of abstraction is to think about driving a car. To make the car turn right, you only have to turn the steering wheel right. The driver doesn’t have to know how the tires, rack and pinion, or power steering pump works — they just turn the wheel. Having to manage all of those other things while driving the car would cause chaos and a lot of accidents. 

**Note** It is like the dark box example, you put something inside a dark box and it returs to you something else, it doesn't matter how. 

### Polymorphism

Polymorphism means "the condition of occurring in several different forms." That's exactly what the fourth and final pillar is concerned with – types in the same inheritance chains being able to do different things.

If you have used inheritance correctly you can now reliably use parents like their children. When two types share an inheritance chain, they can be used interchangeably with no errors or assertions in your code.

### Inheritance

Inheritance allows a class to inherit the features of other classes. The original class is called the parent class, and the class inheriting the features is called the child class. Inheritance provides reusability. The child class can also add new attributes and methods. 

Inheritance is often used to create generic parent classes and child classes that have more specific functionality.

**Note** This is posible 'cause when you create a child class, you can only add or extend tha father class, never reduce it.
For example, if we create a car() class, wich has methods to turn on the car, drive it, stop it. Then we can create a child class for sport cars wich can do all the same as the car class but also has a turbo method. 

Reusability is the main benefit here. We know sometimes that multiple places need to do the same thing, and they need to do everything the same except for one small part. This is a problem inheritance can solve.

Whenever we use inheritance, we try to make it so that the parent and the child have **high cohesion**. Cohesion is how related your code is. For example, does the  Bird type extend from the DieselEngine type?

Keep your inheritance simple to understand and predictable. Don't inherit from somewhere completely unrelated because there's one method or property you need. Inheritance doesn't fix that particular problem well.

When using inheritance, you should require most of the functionality (you don't always need absolutely everything).

Developers have a principle called the **Liskov Substitution principle**. It states that if you can use a parent class (let's call it ParentType) anywhere you use a child (let's call it ChildType) – and ChildType inherits from the ParentType – then you pass the test.

The main reason you would fail this test, is if the ChildType is removing things from the parent. If ChildType removed methods it inherited from the parent, it'd lead to TypeError's where things are undefined that you are expecting not to be.

Inheritance chain is the term used to describe the flow of inheritance from the base object's prototype (the one that everything else inherits from) to the "end" of the inheritance chain.

Do your best to keep your inheritance chains clean and sensible. You can easily end up coding an anti-patterns when using Inheritance (called the Fragile base anti-pattern). This happens where your base prototypes are considered "fragile" because you make a "safe" change to the base object and then start to break all your children. 

