# Task 1: Declaring Variables and Displaying Personal Information

name = "Abdullah said"
gender = "Male"
age = 24
address = "Rashideya UAE"
degree = "BS Software Engineering"
dob = "20th June 2000"
email = "abdullah@gmail.com"
mob = "+9715234567890"

print("Personal Information")
print("Name:", name)
print("Gender:", gender)
print("Age:", age)
print("Address:", address)
print("Degree:", degree)
print("Date of Birth:", dob)
print("Email:", email)
print("Contact Number:", mob)

# Task 2: Type Casting and Swapping Two Variables
   
a = 10  
b = 20.5  

# Before Swapping
print("Before Swapping:")  
print("a =", a, "(Type:", type(a), ")")  
print("b =", b, "(Type:", type(b), ")")  

# Type Casting and Swapping
a, b = float(a), int(b)  

# After Swapping
print("\nAfter Swapping:")  
print("a =", a, "(Type:", type(a), ")")  
print("b =", b, "(Type:", type(b), ")")  


# Task 3: Declaring Variables with Different Data Types
int_var = 100  
float_var = 25.75  
str_var = "Hello World"  
bool_var = True  
list_var = [1, 2, 3, 4]  
tuple_var = (5, 6, 7)  
dict_var = {"name": "abdullah", "age": 24}  

# Displaying values and types  
print("int_var =", int_var, "(Type:", type(int_var), ")")  
print("float_var =", float_var, "(Type:", type(float_var), ")")  
print("str_var =", str_var, "(Type:", type(str_var), ")")  
print("bool_var =", bool_var, "(Type:", type(bool_var), ")")  
print("list_var =", list_var, "(Type:", type(list_var), ")")  
print("tuple_var =", tuple_var, "(Type:", type(tuple_var), ")")  
print("dict_var =", dict_var, "(Type:", type(dict_var), ")")  
