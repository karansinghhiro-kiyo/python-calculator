import random

a = int(input("🔢 Enter number a: "))

b = int(input("🔢 Enter number b: "))

operation = input("🧮 Choose +, -, *, /: ")

if operation == "+":
    print("➕ Result:", a + b)

elif operation == "-":
    print("➖ Result:", a - b)

elif operation == "*":
    print("✖️ Result:", a * b)

elif operation == "/":
    print("➗ Result:", a / b)