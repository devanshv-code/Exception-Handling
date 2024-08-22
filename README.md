# Exception-Handling
## What is Exception ? 
An exception is an event that happens during a program's execution and disturb the normal flow of the program.
## Why it is Dangerous ? 
1.  Lead to sudden termination of the program.

2.  Can block the application.

3.  Data loss problem.

4.  Corrupt data files.
## Error and Exception
Errors cannot be handled but exception can be handled using exception handling syntax.
#### example of error is :
print("hello)
## What is Exception Handling ? 
Exception handling is the process of managing *exception* in a program to prevent it from crashing.

#### Exception handling generally involves four blocks:

1.try

2.except

3.else

4.finally
## Blocks
____________________________________________________________________________________________________________________________________________________________________________

### 1. Try Block:


#### Purpose: 
Contains the code that might raise an exception.


#### Syntax:
try: 

#Code that might cause an exception
___________________________________________________________________________________________________________________________________________________________________________
### 2. Except Block:


#### Purpose: 
Catches and handles the exception if one occurs in the try block.


#### Syntax:


except ExceptionType: 

#Code to handle the exception
___________________________________________________________________________________________________________________________________________________________________________

### 3. Else Block:

#### Purpose: 
Contains code that runs if no exception occurs in the try block.

#### Syntax:

else: 

#Code to execute if no exception was raised
___________________________________________________________________________________________________________________________________________________________________________
### 4. Finally Block:

#### Purpose: 
Contains code that always runs, regardless of whether an exception occurred or not.

#### Syntax:

finally: 

#Code that always runs
___________________________________________________________________________________________________________________________________________________________________________
##### try block: Code that might cause an exception.
____________________________________________________
##### except block: Handles specific exceptions.
____________________________________________________

##### else block: Runs if no exceptions are raised.
____________________________________________________

##### finally block: Always runs, used for cleanup.
____________________________________________________
## TYPES 
#### ValueError:


Happens when you try to use the wrong type of value in a function or operation.

#### IndexError:


Occurs when you try to access an index that is out of the range of a list or other sequence types.

#### ZeroDivisionError:


Happens when you try to divide a number by zero.

#### NameError:


Occurs when you try to use a variable or function that hasn’t been defined yet.





