import re
import lex
import gerador

# Ler o arquivo de tokens enviado pelo léxico e convertê-lo a uma lista
l_tokens = list(open('tokens.txt', 'r'))
l_tokens = [s.rstrip() for s in l_tokens]

# Contagem de tokens
num_tokens = len(l_tokens)


# Função para indicar o erro sintatico
def erro_sintatico(erro, erro2):
    print('Erro identificado:', erro, erro2)


# Função para indicar o erro sintatico
def erro_semantico(tipo, erro):
    if (tipo == "1"):
        print("Erro identificado, variável ja registrada:", erro)
    if (tipo == "2"):
        print("Erro identificado, variável nao registrada:", erro)
    if (tipo == "3"):
        print("Erro identificado, variável nao inicializada:", erro)
    if (tipo == "4"):
        print("Erro identificado, código inalcançável", erro)
    if (tipo == "5"):
        print("Erro identificado, variável declarada mas não usada:", erro)


l_variaveis = []
l_valores = []
l_tipos = []
l_usos = []
# contreg = 0

# Verificação do sintático dos tokens, irá ler token por token, indentificar seu tipo e verificar a compatibilidade dele com o próximo token
for i in range(num_tokens):

    if(l_tokens[i] in lex.comentario_key):
        continue

    elif(l_tokens[i] in lex.reservadas_key):
        if(l_tokens[i] not in lex.comentario_key):
            if(l_tokens[i+1] not in lex.pontuacao_open_key):
                erro_sintatico(l_tokens[i], l_tokens[i+1])

    elif(l_tokens[i] in lex.operadores_key):
        if(l_tokens[i] in lex.operadores_mudanca_key):
            if(l_tokens[i+1] not in lex.pontuacao_close_key):
                erro_sintatico(l_tokens[i], l_tokens[i+1])
        elif(l_tokens[i] not in lex.operadores_mudanca_key):
            if(l_tokens[i+1] not in lex.pontuacao_open_key):
                if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                    if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                        if not(re.findall(lex.t_literal, l_tokens[i+1])):
                            erro_sintatico(l_tokens[i], l_tokens[i+1])
        if(l_tokens[i] == '/'):
            if(l_tokens[i+1] == '0'):
                erro_semantico('4', "(Divisao por 0)")

        # if(l_tokens[i] == '+'):
        #     if(l_tokens[i-1] not in lex.operadores_key):
        #         if(l_tokens[i+1] not in lex.operadores_key):
        #             gerador.gerarcodigo(contreg, "DECLARACAO",
        #                                 l_tokens[i], l_tokens[i+1], l_tokens[i+2])

    elif(l_tokens[i] in lex.operadores_logicos):
        if(l_tokens[i+1] not in lex.pontuacao_open_key):
            if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                    erro_sintatico(l_tokens[i], l_tokens[i+1])

    elif(l_tokens[i] in lex.tipo_variavel_key):
        if (l_tokens[i+2] != "("):
            if (l_variaveis.count(l_tokens[i+1]) == 0):
                l_variaveis.append(l_tokens[i+1])
                l_tipos.append(l_tokens[i])
                l_usos.append(0)
                if(l_tokens[i+2] == "="):
                    l_valores.append(l_tokens[i+3])
                else:
                    erro_semantico("3", l_tokens[i+1])
            else:
                erro_semantico("1", l_tokens[i+1])
        if(l_tokens[i+2] != "("):
            gerador.gerardeclaracao(
                len(l_variaveis), l_tokens[i+1], l_tokens[i+3])
        if not(re.findall(lex.t_identificador, l_tokens[i+1])):
            if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                erro_sintatico(l_tokens[i], l_tokens[i+1])

    elif(re.findall(lex.t_identificador, l_tokens[i])):
        if(l_tokens[i+1] not in lex.pontuacao_key):
            if(l_tokens[i+1] not in lex.operadores_key):
                if(l_tokens[i+1] not in lex.operadores_logicos_key):
                    erro_sintatico(l_tokens[i], l_tokens[i+1])

    elif(re.findall(lex.t_numeros, l_tokens[i])):
        if(l_tokens[i+1] not in lex.pontuacao_key):
            if(l_tokens[i+1] not in lex.operadores_key):
                if(l_tokens[i+1] not in lex.operadores_logicos_key):
                    erro_sintatico(l_tokens[i], l_tokens[i+1])

    elif(l_tokens[i] in lex.pontuacao_key):
        if(l_tokens[i] == '('):
            if(l_tokens[i+1] != ')'):
                if(l_tokens[i+1] not in lex.pontuacao_open_key):
                    if(l_tokens[i+1] not in lex.tipo_variavel_key):
                        if(l_tokens[i+1] not in lex.operadores_mudanca_key):
                            if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                                if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                                    if not(re.findall(lex.t_literal, l_tokens[i+1])):
                                        erro_sintatico(
                                            l_tokens[i], l_tokens[i+1])
        elif(l_tokens[i] == '['):
            if(l_tokens[i+1] != ']'):
                if(l_tokens[i+1] not in lex.pontuacao_open_key):
                    if(l_tokens[i+1] not in lex.tipo_variavel_key):
                        if(l_tokens[i+1] not in lex.operadores_mudanca_key):
                            if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                                if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                                    erro_sintatico(l_tokens[i], l_tokens[i+1])
        elif(l_tokens[i] == '{'):
            if(l_tokens[i+1] != '}'):
                if(l_tokens[i+1] not in lex.reservadas_key):
                    if(l_tokens[i+1] not in lex.pontuacao_open_key):
                        if(l_tokens[i+1] not in lex.tipo_variavel_key):
                            if(l_tokens[i+1] not in lex.operadores_mudanca_key):
                                if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                                    if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                                        erro_sintatico(
                                            l_tokens[i], l_tokens[i+1])
        elif(l_tokens[i] == ':'):
            if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                erro_sintatico(l_tokens[i], l_tokens[i+1])
        elif(l_tokens[i] == '.'):
            if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                    erro_sintatico(l_tokens[i], l_tokens[i+1])
        elif(l_tokens[i] == ','):
            if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                    if not(re.findall(lex.t_literal, l_tokens[i+1])):
                        erro_sintatico(l_tokens[i], l_tokens[i+1])
        elif(l_tokens[i] == '}'):
            if(i == num_tokens - 1):
                # fim do programa
                print("\n")
                break
            else:
                if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                    if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                        if(l_tokens[i+1] not in lex.reservadas_key):
                            if(l_tokens[i+1] not in lex.tipo_variavel_key):
                                if(l_tokens[i+1] not in lex.pontuacao_open_key):
                                    if(l_tokens[i+1] not in lex.pontuacao_close_key):
                                        erro_sintatico(
                                            l_tokens[i], l_tokens[i+1])

        elif(l_tokens[i] == ']'):
            if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                    if(l_tokens[i+1] not in lex.pontuacao_key):
                        if(l_tokens[i+1] not in lex.operadores_key):
                            if(l_tokens[i+1] not in lex.operadores_logicos_key):
                                erro_sintatico(l_tokens[i], l_tokens[i+1])

        elif(l_tokens[i] == ')'):
            if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                    if(l_tokens[i+1] not in lex.pontuacao_key):
                        if(l_tokens[i+1] not in lex.operadores_key):
                            if(l_tokens[i+1] not in lex.operadores_logicos_key):
                                erro_sintatico(l_tokens[i], l_tokens[i+1])
        elif(i == num_tokens - 1):
            if(l_tokens[i] != '}'):
                print("Finalização incorreta do programa!")


for i in range(num_tokens):
    if(re.findall(lex.t_identificador, l_tokens[i])):
        if(l_tokens[i+1] != "("):
            if(l_tokens[i] in lex.reservadas_key) or (l_tokens[i] in lex.t_literal) or (l_tokens[i] in lex.tipo_variavel_key):
                continue
            elif(l_tokens[i] not in l_variaveis):
                erro_semantico("2", l_tokens[i])

for j in range(num_tokens):
    for i in range(len(l_variaveis)):
        if(l_tokens[j] == l_variaveis[i]):
            l_usos[i] += 1

for i in range(len(l_usos)):
    if(l_usos[i] == 1):
        erro_semantico('5', l_variaveis[i])


print(l_variaveis)
print(l_valores)
print(l_tipos)
print(l_usos)

# A = []
# for i in range(2):
#     linha = []
#     for j in range(len(l_variaveis)):
#         linha = linha + [l_valores]
#     A = A + [linha]
# print(A)
