## Syntax errors - Estoura antes de buildar
# x = 42
# y = 206
# if x == y <<<<<< (falta :)
#   print("Success!!")

## Runtime errors - Estoura ao buildar
# x = 42
# y = 0
# print(x/y) <<<<< (Divisão por 0)

## Logic erros
# x = 206
# y = 42 
# if x < y
#   print(f"{x} if greater than {y}")
errorX = 10
errorY = 0

try:
    print(errorX / errorY)
except ZeroDivisionError as identifier:
    print("Not allowed to divide by zero.")
else:
    print("Something else went wrong.")
finally:
    print("This is our cleanup colde.")
