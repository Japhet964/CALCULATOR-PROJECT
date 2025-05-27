# Simple Calculator

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# operation = input("Enter the operation (+, -, *, /): ")

# if operation == '+':
#     result = num1 + num2
#     print("Result:", result)
# elif operation == '-':
#     result = num1 - num2
#     print("Result:", result)
# elif operation == '*':
#     result = num1 * num2
#     print("Result:", result)
# elif operation == '/':
#     if num2 != 0:
#         result = num1 / num2
#         print("Result:", result)
#     else:
#         print("Error: Cannot divide by zero.")
# else:
#     print("Invalid operation. Please choose +, -, *, or /.")


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the oparetion (+, *, -, /) :")

if operation == '+':
    result = num1 + num2
    print("result:", result)


elif operation == '*':
  result = num1 * num2
  print("result", result)


elif operation == '-':
   result = num1 - num2
   print("result:", result)


elif operation == '/':
   result = num1 / num2
   print("result:", result)

   
   