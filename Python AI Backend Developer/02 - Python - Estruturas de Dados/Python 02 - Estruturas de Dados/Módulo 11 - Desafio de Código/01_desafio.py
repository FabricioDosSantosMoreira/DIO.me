
def recomendar_plano(consumo: float) -> str:

    if consumo <= 10:
        s = "Plano Essencial Fibra - 50Mbps"
    elif consumo > 10 and consumo <=20:
        s = "Plano Prata Fibra - 100Mbps"
    else:
        s = "Plano Premium Fibra - 300Mbps"

    return s
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))

# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:

    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))