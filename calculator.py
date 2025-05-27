# Simple Calculator

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

   
   
