# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade
# de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do
# arquivo usando este link (em minutos).






arquivo = float(input('Digite o tamanho do arquivo em MB: '))
velocidade = float(input('Digite a velocidade da conexão de Internet em Mbps: '))
tempo = (arquivo * 8) / (velocidade * 60)

print('O tempo aproximado de download é de', round(tempo, 2), 'minutos.')
