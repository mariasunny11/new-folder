### Part 1: Basic Questions

# 1. Create a variable called name and store your name in it.
name = "maria"
print(name)

 # *2. Age, height, student - print data types*

#  age = 22
# height = 5.4;
# is_student = True


# *3. Print name, age, place in single statement*
name = "Arun"
age = 21
place = "delhi"
print(name, age, place)

# 4. Swap two variables without third variable

a = 10
 b = 20
 a, b = b, a
 print(a, b) 

# *5. Combine first and last name*
# first_name = "Anand"
# last_name = "Kumar"
# full_name = first_name + " " + last_name
# print(full_name)
# *6. Change value 100 to 200*
# x = 100
# x = 200
# print(x)
# *7. Difference between = and == ?*
# - `=` is Assignment Operator: Assigns value. Eg: `x = 10`
# - `==` is Comparison Operator: Checks if two values are equal. Eg: `10 == 10` gives True

# *8. Rules for naming variables*
# 1. Must start with letter or underscore `_`
# 2. Cannot start with a number
# 3. Can contain only letters, numbers, underscore
# 4. Case-sensitive `age` and `Age` are different
# 5. Cannot use Python keywords like `if`, `for`, `class`

# ### Part 2: Type Conversion

# *9. int to float*
# n = 25
# print(float(n))  # 25.0
# *10. float to int*
# print(int(19.99)) # 19
# *11. string "500" to int + 100*
# s = "500"
# result = int(s) + 100
# print(result) # 600
# *12. Two numbers input sum as integer*
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(a + b)
# *13. Decimal input to float*
# num = float(input("Enter decimal: "))
# print(num, type(num))
# *14. int(8.9) =* `8` - decimal part is truncated, not rounded.

# *15. float(10) =* `10.0`

# *16. str(25) + str(15) =* `"2515"` - string concatenation, not addition.

# *17. bool(0), bool(1), bool("")*
# bool(0)  # False
# bool(1)  # True
# bool("") # False - empty string is False
# *18. int("hello") =* `ValueError: invalid literal for int()`. Cannot convert text to int.

# ### Part 3: Arithmetic Operators

# *19. Output:*
# a = 15
# b = 4
# print(a + b)  # 19
# print(a - b)  # 11
# print(a * b)  # 60
# print(a / b)  # 3.75
# print(a // b) # 3  -> floor division
# print(a % b)  # 3  -> remainder
# print(a ** b) # 50625 -> 15 power 4
# *20. Area of rectangle*
# length = 10
# width = 5
# area = length * width
# print(area)
# *21. Total price of three products*
# p1 = 100
# p2 = 250
# p3 = 300
# print(p1 + p2 + p3)
# *22. Square and Cube of input*
# n = int(input("Enter number: "))
# print("Square:", n**2)
# print("Cube:", n**3)
# *23. Minutes to seconds*
# minutes = int(input("Enter minutes: "))
# print(minutes * 60)
# *24. Total and Average*
# total = 75 + 80 + 90
# average = total / 3
# print("Total:", total)     # 245
# print("Average:", average) # 81.66
# *25. Price * Quantity*
# price = float(input("Price: "))
# qty = int(input("Quantity: "))
# print(price * qty)
# ### Part 4: Comparison and Logical Operators

# *26. Output:*
# print(10 > 5)    # True
# print(10 == 10)  # True
# print(7 != 7)    # False
# print(15 <= 20)  # True
# *27. Output:*
# print(10 > 5 and 8 < 12) # True and True = True
# print(10 < 5 or 8 < 12)  # False or True = True
# print(not True)          # False
# *28. Difference and vs or*
# - `and`: True only if BOTH conditions are True
# - `or`: True if at least ONE condition is True

# *29. Output:*
# a = 10
# b = 20
# print(a > b)  # False
# print(a < b)  # True
# print(a == b) # False
# *30. Expressions*
# print(25 > 15)                  # a
# print(10 == 10)                 # b
# print(8 != 5)                   # c
# print(20 > 10 and 15 < 25)      # d
# ### Part 5: Assignment and Other Operators

# *31. Output:*
# x = 10
# x += 5
# print(x) # 15

# x *= 2
# print(x) # 30

# x -= 4
# print(x) # 26
# *32. Difference x = x + 5 and x += 5*
# Both do same - add 5 to x. `x += 5` is shorthand for `x = x + 5`. Functionally same, second is shorter.

# *33. Output:*
# x = 17
# print(x // 5) # 3
# print(x % 5)  # 2

# *34. Final price after 10% discount*
price = float(input("Enter price: "))
final = price - (price * 10/100)
# or final = price 
#  print(final)

# *35. Output:*
a = 5
 b = 2
 print(a ** b + b * 3) # 5**2 + 2*3 = 25+6 = 31
 print((a + b) * 3)    # (7)*3 = 21
