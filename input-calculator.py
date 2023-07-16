number_1 = input("Choose your first number ! ")
number_2 = input("Choose your second number ! ")
operator = input("Choose your operator between those [*, -, +, /, //, **, %] => ")

# ! Verfication of calcul operator
# ? Multiplication
if operator == '*':
  result = int(number_1) * int(number_2)
  print(result)
    
# ? Substraction
elif operator == '-':
  result = int(number_1) - int(number_2)
  print(result)

# ? Addition
elif operator == '+':
  result = int(number_1) + int(number_2)
  print(result)

# ? Division
elif operator == '/':
  result = int(number_1) / int(number_2)
  print(result)
  
# ? Int Division
elif operator == '//':
  result = int(number_1) // int(number_2)
  print(result)
  
# ? Power
elif operator == '**':
  result = int(number_1) ** int(number_2)
  print(result)
  
# ? Modulo
elif operator == '%':
  result = int(number_1) % int(number_2)
  print(result)
    
else:
    print("Error please choose a correct operator !")