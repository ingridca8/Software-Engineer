# Scope
Scope defines which namespaces our program will look into (to check names) and in what order. While multiple namespaces usually exist at once, this does not mean we can access all of them in different parts of our program! Exploring the concept of scope will allow us to start recognizing when and where certain objects may or may not be accessed.

Similar to namespaces, there are four different levels of scope. These levels are:

   + Built-in Scope (We will skip talking about this scope)
  +  Global Scope
  +  Enclosing Scope
  +  Local Scope

Note: As we explore the ideas around scope, there may be some confusion between what distinguishes the concept of scope and namespaces. While both concepts are interlinked and work together, namespaces are simply the mechanism for storing name-object pairs, while scope will serve as a rule system on where (which point in our code) we can retrieve those names. 

## Local scope
Whenever we decide to call a function, a new local scope will be generated. Each subsequent function call will generate a new local scope. Since the local scope is the deepest level of the four scopes, names in a local scope cannot be accessed or modified by any code called in outer scopes. As a rule of thumb, any names created in a local namespace are usually also locally scoped. 

    def favorite_color(): 
     color = 'Red'
    
    print(color) 

In this case, the name of color is scoped locally to the function favorite_color(). Since the statement print(color) is called outside of the function, it has no access to the local scope (and thus the local namespace) inside of favorite_color() and returns an error. 

## Enclosing/Nonlocal Scope
Enclosing scope allows any value defined in an enclosing function to be accessed in nested functions below it.

There are two caveats to be aware of with enclosing scope:

 +   The flow of scope access only flows upwards. This means that the deepest level has access to every enclosing namespace above it, but not the other way around.
  +  Immutable objects, such as strings or numbers, can be accessed in nested functions, but cannot be modified.

## Modifying Scope Behavior: nonlocal Statement
We can access names from the enclosing scope with nested functions, but we cannot modify them. Python does however provide a way for us to modify names in the enclosing scope, by using the nonlocal statement.

Given the following enclosing and nested function, there is a variable defined in the enclosing scope, which is not modifiable from within the nested function.

>>def enclosing_function():
>>  var = "value"

>>  def nested_function():
>>    var = "new_value"

>>  nested_function()

>>  print(var)

>>enclosing_function()

The output would be:

>> value

as the value of var was not modified by the nested function. After using the **nonlocal** statement, the variable is now modifiable from the local scope.

    def enclosing_function():
      var = "value"
    
      def nested_function():
          **nonlocal** var
            var = "new_value"

      nested_function()
      print(var)

## Global scope
At the highest level of access, we have the global scope. Names defined in the global namespace will automatically be globally scoped and can be accessed anywhere in our program. 

However, similar to local scope, values can only be accessed but not modified.

    enclosing_function()

The output would now be:

    new_value

## Modifying Scope Behavior: global Statement
Sometimes, we want to modify a global name from within a local scope.

Similar to the nonlocal statement, Python provides the **global** statement to allow the modification of global names from a local scope.

    global_var = 10

    def some_function():
      **global** global_var
      global_var = 20

    some_function()
    print(global_var)

The output would now be:

    20

In addition, the global statement can be used even if the name has not been defined in the global namespace. Using the global statement would create the new variable in the global namespace.

    def some_function():
      **global** x
      x = 30

    some_function()
    print(x)

This would output:

    30

In summary, the global keyword is used within a local scope to associate a variable name with a name in the global namespace. This association is only valid within the local scope when global is used.

## Scope Resolution: The LEGB Rule
While most of our focus so far has been around where we can access namespaces, to truly get a full picture of scoping rules, we must also examine how Python handles scope resolution.

Scope resolution is a term used to describe a search procedure for a name in the various namespaces. A set of rules dictates the order that the search needs to follow.

In Python, the unofficial rule (often referred to in literature but does not exist in the official documentation) is known as the LEGB rule.

LEGB stands for Local, Enclosing, Global, and Built-in. These four letters represent the order of namespaces Python will check to see if a name exists.

This process of scope resolution is crucial to understanding how programs are able to access names in different scopes. Keep in mind the order that Python searches always start at the lowest level (the local level) and always flows upward to the higher scopes.

The second scenario to examine is seeing what happens when we have two of the same name in different namespaces. 

>>age = 27 
>>
>>def func(): 
>>  age = 42
>>
>>  def inner_func():
>>    print(age)
>>  
>>  inner_func() 
>>
>>func()

Here the output will be 42 because Python could find a name (age) in the enclosing scope and did not continue to search for the value up into the global scope. If Python cannot find a name in any of the four scopes it searches, it will return a NameError exception. 
