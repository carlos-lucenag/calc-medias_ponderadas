#programa que calcula médias ponderadas

#1. receber a quantidade de notas e consequentemente de pesos
#2. realizar os calculos
#3. mostrar o resultado

verificador = 1

def calculadora_medias_ponderadas(qnt_notas):
    #declaração das listas e variáveis:
    lista_notas = list()
    lista_pesos = list()
    lista_nota_x_pesos = list()
    soma_pesos = float()
    soma_produtos = float()
    #recepção dos dados (notas e seus respectivos pesos):
    for i in range(qnt_notas):
        nota = float(input('\nDigite a nota: '))
        lista_notas.append(nota)
        peso = float(input('\nDigite o peso para a nota anterior: '))
        lista_pesos.append(peso)
    #cálculos:
    for i in range(len(lista_pesos)):
        soma_pesos += lista_pesos[i]
    #cálculo das notas x os pesos:
    for i in range(qnt_notas):
        nota_x_peso = lista_notas[i] * lista_pesos[i]
        lista_nota_x_pesos.append(nota_x_peso)
    #cáculo da soma dos produtos anteriores:
    for i in range(qnt_notas):
        soma_produtos += lista_nota_x_pesos[i]
    #cálculo final da média:
    media = soma_produtos / soma_pesos
    #saída:
    saida = f'\nA média ponderada calculada é igual a: {media:.3f}'
    return saida

while True:
    if verificador == 0: break
    print('\nBem vindo à minha calculadora de médias ponderadas, vamos começar...')
    qnt_notas = int(input('\nQuantas notas serão usadas? '))

    print(calculadora_medias_ponderadas(qnt_notas))

    print('\nSe desejar realizar outra operação, digite 1\nSe desejar encerrar o programa, digite 0\n')
    verificador = int(input())