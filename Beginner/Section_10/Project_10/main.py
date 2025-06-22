from art import logo

print(logo)

def calculator(num1, num2, operation):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    
    return result

while True:
    num1 = int(input("What's the first number?: "))
    operation = input("""
+
-
*
/
Pick an operation: """)
    num2 = int(input("What the next number?: "))
    result = calculator(num1, num2, operation)
    print(f"{num1} {operation} {num2} = {result}")
    
    keep_play = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if keep_play == 'n':
        break