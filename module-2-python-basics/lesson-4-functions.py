"""
Module 2 — Lesson 4: Functions (def / parameters / return)
Student: Cruz, Jan Andrei O.
Date: September 26, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
so basically a function is a recipe with a name. you write the steps
once, give it a name like drink_price, and then whenever you need that
job done you just call the name instead of writing everything again.

when you call it you can feed stuff INTO it (like what size the drink
is) and those inputs are called parameters. then it does its thing and
can hand exactly one thing BACK with the word return. that's the
return value. if it never says return you just get None, which is like
getting nothing back.


============================================
KEY VOCABULARY
============================================
- function: basically a recipe with a name. I write it once with def
  and then I can run it whenever I want just by saying its name
- parameter: the inputs a function needs — the "empty slots" in the
  recipe. like size and iced in def drink_price(size, iced=True)
- argument: the actual values I plug in when I call the function, like
  "medium" in drink_price("medium"). parameters are the slots,
  arguments are what I put in them (this mix-up got me at first lol)
- return value: the one thing the function hands back with return. if
  I forget to return anything I get None
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

def drink_price(size, iced=True):
    
    if size == "small":
        price = 15
    elif size == "medium":
        price = 20
    else:
        price = 25            
    if iced:
        price = price + 3     
    return price             


kuya_total = drink_price("medium") * 3        
print("3 medium iced drinks =", kuya_total)

ate_total = drink_price("small", iced=False) * 2   
print("2 small no-ice drinks =", ate_total)       


bill = kuya_total + ate_total               
change = 100 - bill                        
print("Bill =", bill)
print("Change from 100 =", change)

def can_afford(money, cost):
    if money >= cost:
        return True
    return False

print("Can pay with 100?", can_afford(100, bill))
print("Can pay with 50?", can_afford(50, bill))



"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
Okay so this one actually happened to me while I was testing my first
draft. I wrote a function that ended with print(width * height) and I
thought it was working fine because I could literally see 12 on the
screen lol. But then when I did result = area(3, 4) and printed
result, I got None?? I was stuck on that for a minute.
The problem is print and return do totally different things. Print
just shows the number to me and then throws it away, so my code can't
use it anymore. Return actually hands the value back so I can save it
or do more math with it. And if a function never hits a return, python
just quietly gives you None without even warning you.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
