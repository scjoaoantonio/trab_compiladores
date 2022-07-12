import re
from sre_constants import LITERAL
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


# Função para indicar o erro semantico
def erro_semantico(tipo, erro):
    if (tipo == "1"):
        print("Erro identificado, variável ja registrada:", erro)
    if (tipo == "2"):
        print("Erro identificado, variável nao registrada:", erro)
    if (tipo == "3"):
        print("Erro identificado, variável nao inicializada:", erro)
    if (tipo == "4"):
        print("WARNING! Código inalcançável", erro)
    if (tipo == "5"):
        print("Erro identificado, variável declarada mas não usada:", erro)


temp_label = 0
cont_label = 0
cont_texto = 0
cont_abrir = 0
cont_fechar = 0
l_fechar = []
l_abrir = []
l_variaveis = []
l_valores = []
l_tipos = []
l_usos = []


# Verificação do sintático dos tokens, irá ler token por token, indentificar seu tipo e verificar a compatibilidade dele com o próximo token
for i in range(num_tokens):

    if(l_tokens[i] in lex.comentario_key):
        continue

    elif(l_tokens[i] in lex.reservadas_key):
        if(l_tokens[i] not in lex.comentario_key):
            if(l_tokens[i+1] not in lex.pontuacao_open_key):
                erro_sintatico(l_tokens[i], l_tokens[i+1])
        if(l_tokens[i] == 'printf'):
            gerador.gerarprint(l_tokens[i+2], str(cont_texto))
            cont_texto += 1
        if(l_tokens[i] == 'for'):
            gerador.gerarfor(cont_label)
            cont_label += 1
            temp_label += 1
        if(l_tokens[i] == 'while'):
            gerador.gerarfor(cont_label)
            cont_label += 1
            temp_label += 1
        if(l_tokens[i] == 'if'):
            gerador.gerarfor(cont_label)
            cont_label += 1
            temp_label += 1
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

        if(l_tokens[i] == '+'):
            if(l_tokens[i-1] not in lex.operadores_key):
                if(l_tokens[i+1] not in lex.operadores_key):
                    for k in range(len(l_variaveis)):
                        if(l_variaveis[k] == l_tokens[i-3]):
                            gerador.gerarsoma(
                                k, l_tokens[i-1], l_tokens[i+1])
        if(l_tokens[i] == '++'):
            gerador.gerarsoma(
                k, l_tokens[i-1], '1')

        if(l_tokens[i] == '-'):
            if(l_tokens[i-1] not in lex.operadores_key):
                if(l_tokens[i+1] not in lex.operadores_key):
                    for k in range(len(l_variaveis)):
                        if(l_variaveis[k] == l_tokens[i-3]):
                            gerador.gerarsub(k, l_tokens[i-1], l_tokens[i+1])
        if(l_tokens[i] == '*'):
            if(l_tokens[i-1] not in lex.operadores_key):
                if(l_tokens[i+1] not in lex.operadores_key):
                    for k in range(len(l_variaveis)):
                        if(l_variaveis[k] == l_tokens[i-3]):
                            gerador.gerarmult(k, l_tokens[i-1], l_tokens[i+1])
        if(l_tokens[i] == '/'):
            if(l_tokens[i-1] not in lex.operadores_key):
                if(l_tokens[i+1] not in lex.operadores_key):
                    for k in range(len(l_variaveis)):
                        if(l_variaveis[k] == l_tokens[i-3]):
                            gerador.gerardiv(k, l_tokens[i-1], l_tokens[i+1])
        if(l_tokens[i] == '=='):
            if(l_tokens[i-1] not in lex.operadores_key):
                if(l_tokens[i+1] not in lex.operadores_key):
                    for k in range(len(l_variaveis)):
                        if(l_variaveis[k] == l_tokens[i-1]):
                            gerador.gerarigual(
                                k, l_tokens[i-1], l_tokens[i+1], cont_label)
        if(l_tokens[i] == '!='):
            if(l_tokens[i-1] not in lex.operadores_key):
                if(l_tokens[i+1] not in lex.operadores_key):
                    for k in range(len(l_variaveis)):
                        if(l_variaveis[k] == l_tokens[i-1]):
                            gerador.gerardiferente(
                                k, l_tokens[i-1], l_tokens[i+1], cont_label)
        if(l_tokens[i] == '>'):
            if(l_tokens[i-1] not in lex.operadores_key):
                if(l_tokens[i+1] not in lex.operadores_key):
                    for k in range(len(l_variaveis)):
                        if(l_variaveis[k] == l_tokens[i-1]):
                            gerador.gerarmaiorque(
                                k, l_tokens[i-1], l_tokens[i+1], cont_label)
        if(l_tokens[i] == '<'):
            if(l_tokens[i-1] not in lex.operadores_key):
                if(l_tokens[i+1] not in lex.operadores_key):
                    for k in range(len(l_variaveis)):
                        if(l_variaveis[k] == l_tokens[i-1]):
                            gerador.gerarmenorque(
                                k, l_tokens[i-1], l_tokens[i+1], cont_label)
        if(l_tokens[i] == '<='):
            if(l_tokens[i-1] not in lex.operadores_key):
                if(l_tokens[i+1] not in lex.operadores_key):
                    for k in range(len(l_variaveis)):
                        if(l_variaveis[k] == l_tokens[i-1]):
                            gerador.gerarmenorigual(
                                k, l_tokens[i-1], l_tokens[i+1], cont_label)
        if(l_tokens[i] == '>='):
            if(l_tokens[i-1] not in lex.operadores_key):
                if(l_tokens[i+1] not in lex.operadores_key):
                    for k in range(len(l_variaveis)):
                        if(l_variaveis[k] == l_tokens[i-1]):
                            gerador.gerarmaiorigual(
                                k, l_tokens[i-1], l_tokens[i+1], cont_label)

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
            for k in range(len(l_variaveis)):
                if(l_variaveis[k] == l_tokens[i+1]):
                    gerador.gerardeclaracao(
                        k, l_tokens[i+1], l_tokens[i+3])
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
            l_abrir.append(l_tokens[i])
            cont_abrir += 1
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
            l_abrir.append(l_tokens[i])
            cont_abrir += 1
            if(l_tokens[i+1] != ']'):
                if(l_tokens[i+1] not in lex.pontuacao_open_key):
                    if(l_tokens[i+1] not in lex.tipo_variavel_key):
                        if(l_tokens[i+1] not in lex.operadores_mudanca_key):
                            if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                                if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                                    erro_sintatico(l_tokens[i], l_tokens[i+1])
        elif(l_tokens[i] == '{'):
            l_abrir.append(l_tokens[i])
            cont_abrir += 1
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
            l_fechar.append(l_tokens[i])
            cont_fechar += 1
            if(i == num_tokens - 1):
                gerador.gerarfim()
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
            temp_label -= 1
            cont_label -= 1
            if(temp_label == 0):
                gerador.fecharlabel(temp_label, 'sim')
            else:
                gerador.fecharlabel(cont_label, 'sim')
            cont_label += 1

        elif(l_tokens[i] == ']'):
            l_fechar.append(l_tokens[i])
            cont_fechar += 1
            if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                    if(l_tokens[i+1] not in lex.pontuacao_key):
                        if(l_tokens[i+1] not in lex.operadores_key):
                            if(l_tokens[i+1] not in lex.operadores_logicos_key):
                                erro_sintatico(l_tokens[i], l_tokens[i+1])

        elif(l_tokens[i] == ')'):
            l_fechar.append(l_tokens[i])
            cont_fechar += 1
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

if(cont_abrir != cont_fechar):
    erro_sintatico('Verifique os itens', '"()","{}","[]"')

gerador.juntarcodigos()
