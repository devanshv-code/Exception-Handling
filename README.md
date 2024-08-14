# Exception-Handling
## What is Exception ? 
An exception is an event that happens during a program's execution and disturb the normal flow of the program.
## Why it is Dangerous ? 
1.  Lead to sudden termination of the program.

2.  Can block the application.

3.  Data loss problem.

4.  Corrupt data files.
## Error and Exception
errors cannot be handled but exception can be handled using exception handling syntax.
#### example of error is :
print("hello)
## What is Exception Handling ? 
Exception handling is the process of managing *exception* in a program to prevent it from crashing.

#### Exception handling generally involves four blocks:

1.try

2.except

3.else

4.finally

### Try Block:


#### Purpose: 
Contains the code that might raise an exception.


#### Syntax:
try: # Code that might cause an exception

### Except Block:


#### Purpose: 
Catches and handles the exception if one occurs in the try block.


#### Syntax:


except ExceptionType: # Code to handle the exception
### Else Block:

#### Purpose: 
Contains code that runs if no exception occurs in the try block.

#### Syntax:

else: # Code to execute if no exception was raised

### Finally Block:

#### Purpose: 
Contains code that always runs, regardless of whether an exception occurred or not (often used for cleanup).

#### Syntax:

finally: # Code that always runs

##### try block: Code that might cause an exception.

##### except block: Handles specific exceptions or errors.

##### else block: Runs if no exceptions are raised.

##### finally block: Always runs, used for cleanup.



