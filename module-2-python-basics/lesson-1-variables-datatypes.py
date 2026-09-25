"""
Module 2 — Lesson 1: Variables & Data Types
Student: Cruz, Jan Andrei O.
Date: September 25, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Variables and data types are fundamental concepts in programming. 
A variable may be thought of as a storage location, which is given a name 
and which holds a value that may be changed during program execution. 
For example, a variable could hold a persons name, age or grade.

A data type is a classification of a value. It is important that a 
programmer knows which type of data has been stored in a particular variable. 
This is because different types of data can be used for different purposes. 
An example of this would be storing a persons age as an integer in one variable 
and the same persons name as a string in another variable.

Understanding of variables and data types is important to programmers as programs 
will often need to store and process different types of information.


============================================
KEY VOCABULARY
============================================
- variable: A name that refers to a value stored in a program. 
It allows us to store and use information later.
- data type: Describes what kind of value a variable contains.
- int: A whole number without a decimal point, such as 18, 50, or 100.
- float: A number that contains a decimal point, such as 95.5 or 3.14.
- string: Text or a sequence of characters. Strings are usually written 
inside quotation marks, such as "Andrei".
- boolean: A value that can only be True or False. It is often used for 
conditions or decisions.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""
student_name = "Jan Andrei O. Cruz" 
student_age = 23 average_grade = 90.3 
is_enrolled = True 
print("Student Name:", student_name) 
print("Age:", student_age) 
print("Average Grade:", average_grade) 
print("Currently Enrolled:", is_enrolled)  


print(type(student_name)) 
print(type(student_age)) 
print(type(average_grade)) 
print(type(is_enrolled))


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I want to avoid is confusing strings with numbers. For example:

age = "20"

Here, 20 is a string because it is inside quotation marks. It is not an integer.

If I write:

age = 20

then age is an integer, which means I can use it for mathematical calculations.

Another mistake I want to avoid is using the wrong data type for a task. 
Understanding the difference between strings, integers, floats, and booleans 
helps prevent errors in a program.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""