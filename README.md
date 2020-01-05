# OOP Basics 🏫 

This class is going to cover the basics of OOP 

### Covered in this class:

**4 Pillars:** 
- Abstraction
- Inheritance
- Polymorphism
- Encapsulation

Other learning outcomes:
- git + GitHub
- Documentation with Markdown
- Best practices and organisation

### Definitions

Add your definitions here:
**Class**
Is a blueprint of an object
It wraps methods and attributes

**Methods**
Just like functions, they can take in arguements, run a block of code 
however they can only be used by an instance of 
its class. 

**Attributes** 
Hold information about our SPECIFIC object.
Are set in the def __init__()  method like any other 
function.

**__ init __ ()**
AKA - Constructor or initialised.
This method runs every time an object is created.
So when you do:
````
animal = Animal('Fred', 10 ,2)
````
**Instance / object**
It is an occurrence of an object

**self**
refers to the object / instance

**Inheritance**
Is the ability of classes to inherit characteristics (parameters)
and behaviours (methods) from parents class. 

**Polymorphism**
Poly means many, and morph means forms. So polymorphism is
'Many forms.'
Polymorphism in OOP is  the ability to change
methods and characteristics for instances of child classes
    - Method Polymorphism
    
**Abstraction**
Is hiding complexity from the user. 
- Heating food in the microwave with one button - what happens?
- Changing gears in a car.
- Coding languages and Binary in computing 

Specific to us, we will:
    - Write nice documentation for how to import and use our code
    - Use inheritance and importing to hide the code
    - Ultimately we can package it into a module that could be 
    imported with PIP 
    
**Encapsulation**
Is restricting and making methods or attributes private.
In python things by default are public to make them private you use 
double underscore __

When a method or an attribute is private it can only be accessed
by its own internal (in the class) methods. It cannot
be called from the run file.
    
## Task 
Create a new project
- Create a class animal 
- Characteristics:
    - alive 
    - bones
- Methods:
    - eat
    - sleep
    - make_sound()

- create a class Dog()
- Make it inherit from animal
- Give it all the attributes of animal plus:
    - owner
    - name
    - dog collar 

- methods:
    - all the other ones plus:
    - eat_bone
    - run
    - greet_owner
    - polymorph the method make_sound to return the string 'woouff'
    
One of these methods needs to take an argument
 Another method should have a default value.
 
 - Have a run file:
    - import all your classes
    - create 2 animals
    - create 2 dogs
    - call some methods on them