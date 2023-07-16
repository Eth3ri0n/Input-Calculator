number_1 = int(input("Choose your first number ! "))
number_2 = int(input("Choose your second number ! "))
operator = input("Choose your operator between those [*, -, +, /, //, **, %] => ")

# ! Verfication of calcul operator
# ? Multiplication
if operator == '*':
  result = number_1 * number_2
  print(result)
    
# ? Substraction
elif operator == '-':
  result = number_1 - number_2
  print(result)

# ? Addition
elif operator == '+':
  result = number_1 + number_2
  print(result)

# ? Division
elif operator == '/':
  result = number_1 / number_2
  print(result)
  
# ? Int Division
elif operator == '//':
  result = number_1 // number_2
  print(result)
  
# ? Power
elif operator == '**':
  result = number_1 ** number_2
  print(result)
  
# ? Modulo
elif operator == '%':
  result = number_1 % number_2
  print(result)
    
else:
    print("Error please choose a correct operator !")