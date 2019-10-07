# Para rodar o código salvo como .py, apenas executar o comando 'python nomedoarquivo.py'
print("Hello world")  # Como printar algo na tela
name = input("Tell me your name: ")  # Como receber input do usuario
print(name + " Teste")  # concatenando strings
# ------------------------------------------------------------------------------------------
## Comparação de strings são case sensitives, logo é necessário utilizar algo como .lower() para comparálas
sentence = "The dog is named Sammy"
print(sentence.upper())  # Transforma a sentença para letras maiusculas
print(sentence.lower())  # Transforma a sentença para letras minúsculas
print(sentence.capitalize())  # Transforma a primeira letra apenas em letra maiúscula
print(sentence.count("a"))  # Conta uma determinada coisa dentro de um todo
# ------------------------------------------------------------------------------------------
first_name = "Joao"
last_name = "Mhurilo"
# python <3
print("Hello, {} {}".format(first_name, last_name))
print("Hello, {1} {1}".format(first_name, last_name))
# python <=3
print(f"Hello, {first_name} {last_name}")
# ------------------------------------------------------------------------------------------
a = 3
b = 2
diasNum = 28
firstStr = '20'
secondStr = '5'
print(a + b)  # + : Soma
print(a - b)  # - : Subtrai
print(a / b)  # / : Divisão
print(a * b)  # '*' : Multiplica (Sem aspas)
print(a ** b)  # '**' : Expoente a ^ b (Sem aspas)
print(f"{diasNum} dias em Fevereiro")
print(str(diasNum) + " dias em Fevereiro")
print(int(firstStr) + int(secondStr))
print(float(firstStr) + float(secondStr))
# python <=3
print(f"{a+b}")