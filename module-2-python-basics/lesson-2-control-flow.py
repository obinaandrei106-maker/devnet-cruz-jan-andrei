"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Cruz, Jan Andrei O.
Date: September 25, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Control flow is how a program makes decisions about what it should do next. 
In Python, if, elif, and else are used to make these decisions.The if statement
checks a condition. If the condition is true, Python runs the code inside that block. 
The elif statement means "else if" and allows us to check another condition 
when the previous one was false. The else statement runs when none of the previous 
conditions are true. For example, a program can check a student's grade and display 
whether the student passed, needs improvement, or failed. This allows the program to 
respond differently depending on the information it receives.


============================================
KEY VOCABULARY
============================================
- condition: A statement that the program checks to determine whether something is true or false.
- if: Used to execute a block of code when a condition is true.
- elif: Short for "else if." It checks another condition if the previous if or elif condition was false.
- else: It runs when none of the previous conditions are true. 
- comparison operator: A symbol used to compare values, such as >, <, ==, !=, >=, and <=.
- boolean expression: An expression that produces either True or False.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# Temperature checker 
temperature = 32 
if temperature >= 35: 
    print("It is very hot today.") 
elif temperature >= 25: 
    print("The weather is warm.") 
elif temperature >= 15: 
    print("The weather is cool.") 
else: print("It is cold today.")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I want to avoid is putting the conditions in the wrong order. 
In an if / elif / else statement, Python checks the conditions from top to 
bottom and stops when it finds the first true condition. I also want to avoid 
forgetting the colon (:) after an if, elif, or else statement and forgetting the 
proper indentation.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
