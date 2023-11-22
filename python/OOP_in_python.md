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

