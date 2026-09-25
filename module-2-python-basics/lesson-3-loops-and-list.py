"""
Module 2 — Lesson 3: Loops & Lists
Student: Cruz, Jan Andrei O.
Date: eptember 25, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Lists and loops are used when I need to work with a lot of information. A list is 
like a container where I can put several values together. For example, if I have the 
names of my classmates, I can put all their names in one list instead of making a separate 
variable for each person. A loop is used when I want the program to repeat something. 
A for loop can go through each item in a list one by one. A while loop keeps running 
as long as the condition is still true.

============================================
KEY VOCABULARY
============================================
- list: A group of values that I can store together in one variable.
- for loop: A way to repeat something for every item in a list.
- while loop: A loop that keeps running while a condition is true.
- index: The position of an item in a list. Python starts with 0 as the first position.
- iteration: One time that the loop repeats.
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

# My shopping list

shopping_list = ["Rice", "Milk", "Bread", "Eggs", "Coffee"]

for item in shopping_list:
    print("I need to buy:", item)

# Simple while loop

number = 1

while number <= 5:
    print(number)
    number += 1

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One mistake I want to avoid is forgetting that the first item in a 
Python list starts at index 0. I also need to be careful when using a 
while loop because if I forget to change the value in the condition, 
the loop might continue forever.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
