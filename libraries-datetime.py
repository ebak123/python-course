from datetime import datetime, timedelta # Importação da função datetime da biblioteca datetime. Importação da função timedelta que faz operações lógicas com as datas.
current_date = datetime.now() # Utiliza o método now() do objeto datetime, que retorna a data atual
print(f"Today is: {current_date}")
days = timedelta(days=5) # Define um periodo de tempo
outro_dia = current_date - days # Utiliza o período de tempo para determinar dias anteriores
print(outro_dia)
print(f"Dia: {current_date.day} Mês: {current_date.month} Ano: {current_date.year}") # Formatação de datas
print(datetime)
birthday = input(f"Quando é seu aniversário? (dd/mm/aaaa)")
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print(f"Birthday: {birthday_date}")