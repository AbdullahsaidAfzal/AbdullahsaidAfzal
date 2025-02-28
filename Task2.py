# Task 2: OPERATORS

# Task 2.1: Arithmetic Operations (Addition, Subtraction, Multiplication, Division, Modulo)
num1 = 15
num2 = 4

print("---- Arithmetic Operations ----")
print("Addition:", num1, "+", num2, "=", num1 + num2)
print("Subtraction:", num1, "-", num2, "=", num1 - num2)
print("Multiplication:", num1, "*", num2, "=", num1 * num2)
print("Division:", num1, "/", num2, "=", num1 / num2)  
print("Modulo:", num1, "%", num2, "=", num1 % num2)  


# Task 2.2: Comparison Operators

print("---- Comparison Operators ----")
print(num1, ">", num2, ":", num1 > num2) 
print(num1, "<", num2, ":", num1 < num2)  
print(num1, ">=", num2, ":", num1 >= num2) 
print(num1, "<=", num2, ":", num1 <= num2) 
print(num1, "==", num2, ":", num1 == num2) 
print(num1, "!=", num2, ":", num1 != num2) 



# Task 2.3: Assignment Operators
x = 10
print(" Assignment Operators")
print("Initial value of x:", x)

x += 5 
print("After x += 5, x =", x)

x -= 3  
print("After x -= 3, x =", x)

x *= 2  
print("After x *= 2, x =", x)

x /= 4  
print("After x /= 4, x =", x)

x %= 3 
print("After x %= 3, x =", x)


# Task 2.4: Logical Operators

# Defining Boolean Variables
is_sunny = True
is_weekend = False

print("Logical Operators")
# Evaluating Logical Conditions
print("is_sunny AND is_weekend:", is_sunny and is_weekend)  
print("is_sunny OR is_weekend:", is_sunny or is_weekend)  
print("NOT is_sunny:", not is_sunny)  


# Additional Example of Logical Operators with Conditions
age = 24
has_license = True

print("Can the person drive?", (age >= 18) and has_license)  # True only if age is 18+ and has a license
