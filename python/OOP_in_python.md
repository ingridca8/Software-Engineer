# Inheritance

In general

    class ParentClass:
      #class methods/properties...
    
    class ChildClass(ParentClass):
      #class methods/properties...

Example

    class Animal:  
      def eat(self): 
        print("Nom Nom Nom...eating food!")

    class Dog(Animal):
      def bark(self):
        print('Bark!')

    class Cat(Animal):
     def meow(self):
       print('Meow!')   

We will get

    fluffy = Dog()
    zoomie = Cat()
    
    fluffy.eat() # Nom Nom Nom...eating food!
    zoomie.eat() # Nom Nom Nom...eating food!

## Overriding Methods

When implementing inheritance, a child class may want to change the behavior of a method from its parent class. In Python, all we have to do is override a method definition. An overriding method in a subclass is one that has the same definition as the parent class but contains different behavior. 

When overriding methods we sometimes want to still access the behavior of the parent method. In order to do that we need a way to call the method of the parent class. Python gives us a way to do that using super().

super() gives us a proxy object. With this proxy object, we can invoke the method of an object’s parent class (also called its superclass). We call the required function as a method on super():

    class Animal:
      def __init__(self, name, sound="Grrrr"):
        self.name = name
        self.sound = sound
    
      def make_noise(self):
        print("{} says, {}".format(self.name, self.sound))
    
    class Cat(Animal):
      def __init__(self, name):
        super().__init__(name, "Meow!") 
    
    pet_cat = Cat("Rachel")
    pet_cat.make_noise() # Rachel says, Meow!

## Multiple Inheritance

Let’s now look at a feature allowed by Python called multiple inheritance. As you may have guessed from the name, this is when a subclass inherits from more than one superclass. One form of multiple inheritance is when there are multiple levels of inheritance. This means a class inherits members from its superclass and its super-superclass.

    class Animal:
      def __init__(self, name):
        self.name = name
     
      def say_hi(self):
        print("{} says, Hi!".format(self.name))
    
    class Cat(Animal):
      pass
    
    class Angry_Cat(Cat):
      pass
    
    my_pet = Angry_Cat("Mr. Cranky")
    my_pet.say_hi() # Mr. Cranky says, Hi!
    

Another form of multiple inhertance involves a subclass that inherits directly from two classes and can use the attributes and methods of both.

    class Animal:
      def __init__(self, name):
        self.name = name
    
    class Dog(Animal):
      def action(self):
        print("{} wags tail. Awwww".format(self.name))
    
    class Wolf(Animal):
      def action(self):
        print("{} bites. OUCH!".format(self.name))
    
    class Hybrid(Dog, Wolf):
      def action(self):
        super().action()
        Wolf.action(self)
    
    my_pet = Hybrid("Fluffy")
    my_pet.action() # Fluffy wags tail. Awwww
                    # Fluffy bites. OUCH!

The above example shows the class Hybrid is a subclass of both Dog and Wolf which are also both subclasses of Animal. All 3 subclasses can use the features in Animal and Hybrid can use the features of Dog and Wolf. But, Dog and Wolf can not use each other’s features.

This form of multiple inheritance can be useful by adding functionality from a class that does not fit in with the current design scheme of the current classes.

Care must be taken when creating an inheritance structure like this, especially when using the super() method. In the above example, calling super().action() inside the Hybrid class invokes the .action() method of the Dog class. This is due to it being listed before Wolf in the Hybrid(Dog, Wolf) definition.

The line Wolf.action(self) calls the Wolf class .action() method. The important thing to note here is that self is passed as an argument. This ensures that the .action() method in Wolf receives the Hybrid class instance to output the correct name.

# Polymorphism

In computer programming, polymorphism is the ability to apply an identical operation onto different types of objects. This can be useful when an object type may not be known at the program runtime. Polymorphism can be applied using Python in multiple ways. We have already experienced a form of it when exploring inheritance.

    class Animal:
      def __init__(self, name):
        self.name = name
    
      def make_noise(self):
        print("{} says, Grrrr".format(self.name))
    
    class Cat(Animal):
    
      def make_noise(self):
        print("{} says, Meow!".format(self.name))
    
    class Robot:
      
      def make_noise(self):
        print("beep.boop...BEEEEP!!!")

The example above shows an Animal class, its subclass Cat, and another standalone class Robot. Each class has a method .make_noise() with different outputs. The identical method name with different behaviors is a form of polymorphism.

## Dunder Methods

The code below shows that when working with different object types like, int, str or list, the + operator performs different functions. This is known as operator overloading and is another form of polymorphism.

    # For an int and an int, + returns an int
    2 + 4 == 6

    # For a string and a string, + returns a string
    "Is this " + "addition?" == "Is this addition?"

    # For a list and a list, + returns a list
    [1, 2] + [3, 4] == [1, 2, 3, 4]

To implement this behavior, we must first discuss dunder methods. Every defined class in Python has access to a group of these special methods. We’ve explored a few already, the constructor __init__() and the string representation method __repr__(). The name dunder method is derived from the Double UNDERscores that surround the name of each method.

Recall that the __repr__() method takes only one parameter, self, and must return a string value. The returned value should be a string representation of the class, which can be seen by using print() on an instance of the class. Review the sample code below for an example of how this method is used.

Defining a class’s dunder methods is a way to perform operator overloading.

    class Animal:
      def __init__(self, name):
        self.name = name
    
      def __repr__(self):
        return self.name
    
      def __add__(self, another_animal):
        return Animal(self.name + another_animal.name)
    
    a1 = Animal("Horse")
    a2 = Animal("Penguin")
    a3 = a1 + a2
    print(a1) # Prints "Horse"
    print(a2) # Prints "Penguin"
    print(a3) # Prints "HorsePenguin"

The above code has the class Animal with a dunder method, .__add__(). This defines the + operator behavior when used on objects of this class type. The method returns a new Animal object with the names of the operand objects concatenated. In this example, we have created a "HorsePenguin"!

The line of code a3 = a1 + a2 invokes the .__add__() method of the left operand, a1, with the right operand a2 passed as an argument. The name attributes of a1 and a2 are concatenated using the .__add__() parameters, self and another_animal. The resulting string is used as the name of a new Animal object which is returned to become the value of a3.

# Abstraction
Abstraction helps with the design of code by defining necessary behaviors to be implemented within a class structure. By doing so, abstraction also helps avoid leaving out or overlapping class functionality as class hierarchies get larger.

    from abc import ABC, abstractmethod

    class Animal(ABC):
      def __init__(self, name):
        self.name = name

      @abstractmethod
      def make_noise(self):
        pass

    class Cat(Animal):
      def make_noise(self):
        print("{} says, Meow!".format(self.name))

    class Dog(Animal):
      def make_noise(self):
        print("{} says, Woof!".format(self.name))

    kitty = Cat("Maisy")
    doggy = Dog("Amber")
    kitty.make_noise() # "Maisy says, Meow!"
    doggy.make_noise() # "Amber says, Woof!"

The below line of code would throw an error.

    an_animal = Animal("Scruffy")
    # TypeError: Can't instantiate abstract class Animal with abstract method make_noise

The abstraction process defines what an Animal is but does not allow the creation of one. The .__init__() method still requires a name, since we feel all animals deserve a name.

The .make_noise() method exists since all animals make some form of noise, but the method is not implemented since each animal makes a different noise. Each subclass of Animal is now required to define their own .make_noise() method or an error will occur.

These are some of the ways abstraction supports the design of an organized class structure.

# Encapsulation

Encapsulation is the process of making methods and data hidden inside the object they relate to. Languages accomplish this with what are called access modifiers like:

   + Public 
  +  Protected (one underscore *_name*)
   + Private (two underscores *__name*)

In general, public members can be accessed from anywhere, protected members can only be accessed from code within the same module and private members can only be accessed from code within the class that these members are defined.

Python doesn’t have any inbuilt mechanism to prevent access from any member (i.e. all members are public in Python). However, there is a common convention amongst developers to use a single underscore **self._x** to indicate that a member is protected. Accessing a protected member outside of the module will not cause an error, it is added by developers to inform other developers that they should be careful when accessing this member in such a manner.

Similarly, we can declare a member as private with two leading underscores **self.__x**. This is more than just a convention in Python because of a mechanism called *name mangling*. Members that are preceded with two underscores have their names modified in the background to **obj._Classname__x**. While they can still be publicly accessed, the purpose of this mechanism is to prevent clashing member names of any inheriting classes that might define a member of the same name.

Note that this is different from the dunder methods we discussed earlier. A dunder method has two leading and two trailing underscores and is treated differently than a private member. One important difference is that dunder method names are no
mangled.

    class Employee():
    def __init__(self):
        self.id = None
        # Write your code below
        self._id = 7
        self.__id = 8

    e = Employee()
    print(dir(e))

## Getters, Setters and Deleters

Using getter, setter, and deleter functions are one way to implement encapsulation within Python where the state of class attributes can be handled within the class. These functions are useful in making sure that the data being handled is appropriate for the defined class functionality.

    class Animal:
      def __init__(self, name):
        self._name = name
        self._age = None

      def get_age(self):
        return self._age

      def set_age(self, new_age):
        if isinstance(new_age, int):
          self._age = new_age
        else:
          raise TypeError

      def delete_age(self):
        print("_age Deleted")
        del self._age

Looking at the Animal class above there is an _age attribute with a single underscore. This notates it is intended to be used only within the module. There are then 3 methods related to age each with a different purpose. These define the getter, setter, and deleter of the specific property.

The first method related to age is a getter and returns self._age. The setter is implemented below that. It includes logic that ensures that the value passed to new_age is an integer. If so, self._age = new_age. If not, raise an error. This is useful and shows the power of using these functions for encapsulation.

The deleter is implemented below the setter. It outputs a confirmation message and uses the del keyword to delete the self._age attribute.

    a = Animal("Rufus")
    print(a.get_age()) # None

    a.set_age(10)
    print(a.get_age()) # 10

    a.set_age("Ten") # Raises a TypeError

    a.delete_age() # "_age Deleted"
    print(a.get_age()) # Raises a AttributeError

Above we see a.get_age() gets the _age value, a.set_age(10) sets the value and a.delete_age() deletes the attribute entirely. A TypeError occurs with a.set_age("Ten") because the defined logic in the setter is looking only for an integer. An AttributeError occurs with a.get_age() after the attribute was deleted.

# Review

  +  Inheritance

Python allows classes to inherit on multiple levels. Meaning a class can inherit from a base class as well as a derived class. Python also supports multiple inheritance, where one class can inherit from any number of other classes. This allows us to describe complex relationships between objects with minimal repeated code.

 +   Polymorphism

Polymorphism is a concept that allows functions and objects to behave in different ways depending on context. There is the polymorphism of functions like len() or the addition operator +, which can act differently depending on the provided data.

  +  Abstraction

Python supports the concept of abstraction by allowing objects with methods that have the same name, to be called in a general manner. Further, Python provides the Abstract Base Class (ABC) for us to create a more clearly defined interface.

  +  Encapsulation

Python’s approach to encapsulation is unique compared to most other object-oriented programming languages. In Python, all members of an object are publicly accessible but there are conventions to indicate to developers that a member is intended to be protected or private. 
