# Scope
Scope defines which namespaces our program will look into (to check names) and in what order. While multiple namespaces usually exist at once, this does not mean we can access all of them in different parts of our program! Exploring the concept of scope will allow us to start recognizing when and where certain objects may or may not be accessed.

Similar to namespaces, there are four different levels of scope. These levels are:

    Built-in Scope (We will skip talking about this scope)
    Global Scope
    Enclosing Scope
    Local Scope

Note: As we explore the ideas around scope, there may be some confusion between what distinguishes the concept of scope and namespaces. While both concepts are interlinked and work together, namespaces are simply the mechanism for storing name-object pairs, while scope will serve as a rule system on where (which point in our code) we can retrieve those names. 

## Local scope
Whenever we decide to call a function, a new local scope will be generated. Each subsequent function call will generate a new local scope. Since the local scope is the deepest level of the four scopes, names in a local scope cannot be accessed or modified by any code called in outer scopes. As a rule of thumb, any names created in a local namespace are usually also locally scoped. 

>> def favorite_color(): 
>>  color = 'Red'

>> print(color) 

In this case, the name of color is scoped locally to the function favorite_color(). Since the statement print(color) is called outside of the function, it has no access to the local scope (and thus the local namespace) inside of favorite_color() and returns an error. 

## Enclosing/Nonlocal Scope
Enclosing scope allows any value defined in an enclosing function to be accessed in nested functions below it.

There are two caveats to be aware of with enclosing scope:

    The flow of scope access only flows upwards. This means that the deepest level has access to every enclosing namespace above it, but not the other way around.
    Immutable objects, such as strings or numbers, can be accessed in nested functions, but cannot be modified.

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

>>def enclosing_function():
>>  var = "value"

>>  def nested_function():
>>    **nonlocal** var
>>    var = "new_value"

>>  nested_function()
>>  print(var)

>>enclosing_function()

The output would now be:

>>new_value
