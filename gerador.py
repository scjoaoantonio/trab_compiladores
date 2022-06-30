# def gerarcodigo(reg, function, atual, prox, prox2):
#     with open('codigo.txt', 'a') as codigo:
#         if(function == "DECLARACAO"):
#             # codigo.write("load $r" + str(reg) + '\n')
#         elif(function == "ATRIBUICAO"):
#             print("ATRIBUICAO")
#         elif(function == "CONDICAO"):
#             print("CONDICAO")
#         elif(function == "REPETICAO"):
#             print("REPETICAO")


# olhar se isso é dec ou atribuição
def gerardeclaracao(cont, variavel, valor):
    with open('codigo.txt', 'a') as codigo:
        codigo.write("load $r" + str(cont) + ', ' + valor + '\n')


# Para juntar 2 arquivos em 1 só
# arq = open("resultado.txt", "w")
# arq1 = open("texto1.txt", "r")
# arq2 = open("texto2.txt", "r")
# arq.write(arq1.read()+arq2.read())
# arq.close()
