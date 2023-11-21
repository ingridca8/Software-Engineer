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

