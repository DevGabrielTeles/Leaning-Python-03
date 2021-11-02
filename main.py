# set (list_of_days)
# input: user input array
# output: converted set

# Variables
dia_para_hora = 24
hora_para_minuto = 60
minuto_para_segundo = 60


# Function with if statement
def dia_para_segundos(num_dias):
    return f"{num_dias} dia(s) são {num_dias * dia_para_hora * hora_para_minuto * minuto_para_segundo} segundos"


# Validando dado string
def validacao():
    try:

        total_dias = int(i)
        if total_dias > 0:
            calculo = dia_para_segundos(total_dias)
            print(calculo)
        elif total_dias == 0:
            print("Você inseriu um valor inválido, insira um valor positivo diferente de 0.")
        else:
            print("Você inseriu um valor inválido, insira um valor positivo diferente de 0.")


    except ValueError:
        print("Não tente burlar a entrada.")


# Restarting the application to keep running
# Looping could be done in Python with while or for
# Input
print("Quando quiser sair da aplicação digite: sair ")
user_input = 0
while user_input != "sair":
    user_input = input("Digite o número de dias e te darei o total de segundos (exemplo: 1, 2, 3):")
    # Every user input will be save in a list
    # Split function will give us a list of the input values
    list_of_days = user_input.split(",")
    print(list_of_days)
    print(set(list_of_days))
    print(type(set(list_of_days)))
    # set function elimine repeated inputs
    for i in set(user_input.split(",")):
        validacao()
