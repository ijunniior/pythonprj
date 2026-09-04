#!/usr/bin/env python3

autor = "Luiz Celso Barbosa Junior"

#Lista: é uma sequência ordenada de valores.

portas_alvo = [22, 80, 443, 3306, 8080, 3000, 5000, 8000, 137, 138, 139, 445]
portas_alvo.append(21) #adiciona a porta 21 na variável, que é uma lista, portas_alvo.
servicos = ["ssh", "https", "dns" ]


print('A Lista de portas é: ', portas_alvo)
print(f'A lista de portas é: {portas_alvo}')

for NUM in range (1,11):
	print(NUM)

# Dicionário é um tipo de serviço que trabalha sobre chave:valor

status_servicos = {
	'host': '8.8.8.8',
	'porta': '443',
	'estado': 'aberta',
	'servico': 'https',
}

print (status_servicos['host'])
print (status_servicos['servico'])

servicos = {
	22: 'SSH',
	80: 'HTTP',
	443: 'HTTPS',
	3306: 'MYSQL',
}

for PORTA in portas_alvo:
	nome = servicos.get(PORTA, 'desconhecido')
	print(f'Porta {PORTA}: Servico {nome} ')
