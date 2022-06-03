# def analisadorsintatico():

import re
import lex

print("\n\n\nAnalisador Sintático:\n\n")

l_tokens = list(open('tokens.txt', 'r'))
l_tokens = [s.rstrip() for s in l_tokens]
'''
# Convert into a list of list
lfl = [_str.split(' ') for _str in l_tokens]
'''

num_tokens = len(l_tokens)


def error(erro, erro2):
    print('Erro identificado:', erro, erro2)


for i in range(num_tokens):

    if(l_tokens[i] in lex.comentario_key):
        continue

    elif(l_tokens[i] in lex.reservadas_key):
        if(l_tokens[i] not in lex.comentario_key):
            if(l_tokens[i+1] not in lex.pontuacao_open_key):
                error(l_tokens[i], l_tokens[i+1])

    elif(l_tokens[i] in lex.operadores_key):
        if(l_tokens[i] in lex.operadores_mudanca_key):
            if(l_tokens[i+1] not in lex.pontuacao_close_key):
                error(l_tokens[i], l_tokens[i+1])
        elif(l_tokens[i] not in lex.operadores_mudanca_key):
            if(l_tokens[i+1] not in lex.pontuacao_open_key):
                if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                    if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                        error(l_tokens[i], l_tokens[i+1])

    elif(l_tokens[i] in lex.operadores_logicos):
        if(l_tokens[i+1] not in lex.pontuacao_open_key):
            if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                    error(l_tokens[i], l_tokens[i+1])

    elif(l_tokens[i] in lex.tipo_variavel_key):
        if not(re.findall(lex.t_identificador, l_tokens[i+1])):
            if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                error(l_tokens[i], l_tokens[i+1])

    elif(l_tokens[i] in lex.tipo_variavel_key):
        if not(re.findall(lex.t_identificador, l_tokens[i+1])):
            if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                error(l_tokens[i], l_tokens[i+1])

    elif(re.findall(lex.t_identificador, l_tokens[i])):
        if(l_tokens[i+1] not in lex.pontuacao_key):
            if(l_tokens[i+1] not in lex.operadores_key):
                if(l_tokens[i+1] not in lex.operadores_logicos_key):
                    error(l_tokens[i], l_tokens[i+1])

    elif(re.findall(lex.t_numeros, l_tokens[i])):
        if(l_tokens[i+1] not in lex.pontuacao_key):
            if(l_tokens[i+1] not in lex.operadores_key):
                if(l_tokens[i+1] not in lex.operadores_logicos_key):
                    error(l_tokens[i], l_tokens[i+1])

    elif(l_tokens[i] in lex.pontuacao_key):
        if(l_tokens[i] == '('):
            if(l_tokens[i+1] != ')'):
                if(l_tokens[i+1] not in lex.pontuacao_open_key):
                    if(l_tokens[i+1] not in lex.tipo_variavel_key):
                        if(l_tokens[i+1] not in lex.operadores_mudanca_key):
                            if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                                if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                                    if not(re.findall(lex.t_literal, l_tokens[i+1])):
                                        error(l_tokens[i], l_tokens[i+1])
        elif(l_tokens[i] == '['):
            if(l_tokens[i+1] != ']'):
                if(l_tokens[i+1] not in lex.pontuacao_open_key):
                    if(l_tokens[i+1] not in lex.tipo_variavel_key):
                        if(l_tokens[i+1] not in lex.operadores_mudanca_key):
                            if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                                if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                                    error(l_tokens[i], l_tokens[i+1])
        elif(l_tokens[i] == '{'):
            if(l_tokens[i+1] != '}'):
                if(l_tokens[i+1] not in lex.reservadas_key):
                    if(l_tokens[i+1] not in lex.pontuacao_open_key):
                        if(l_tokens[i+1] not in lex.tipo_variavel_key):
                            if(l_tokens[i+1] not in lex.operadores_mudanca_key):
                                if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                                    if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                                        error(l_tokens[i], l_tokens[i+1])
                                        print()
        elif(l_tokens[i] == ':'):
            if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                error(l_tokens[i], l_tokens[i+1])
        elif(l_tokens[i] == '.'):
            if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                    error(l_tokens[i], l_tokens[i+1])
        elif(l_tokens[i] == ','):
            if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                    error(l_tokens[i], l_tokens[i+1])
        elif(l_tokens[i] == '}'):
            if(i == num_tokens - 1):
                print("Fim da Análise")
                break
            else:
                if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                    if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                        if(l_tokens[i+1] not in lex.reservadas_key):
                            if(l_tokens[i+1] not in lex.tipo_variavel_key):
                                if(l_tokens[i+1] not in lex.pontuacao_open_key):
                                    if(l_tokens[i+1] not in lex.pontuacao_close_key):
                                        error(l_tokens[i], l_tokens[i+1])

        elif(l_tokens[i] == ']'):
            if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                    if(l_tokens[i+1] not in lex.pontuacao_key):
                        if(l_tokens[i+1] not in lex.operadores_key):
                            if(l_tokens[i+1] not in lex.operadores_logicos_key):
                                error(l_tokens[i], l_tokens[i+1])

        elif(l_tokens[i] == ')'):
            if not(re.findall(lex.t_numeros, l_tokens[i+1])):
                if not(re.findall(lex.t_identificador, l_tokens[i+1])):
                    if(l_tokens[i+1] not in lex.pontuacao_key):
                        if(l_tokens[i+1] not in lex.operadores_key):
                            if(l_tokens[i+1] not in lex.operadores_logicos_key):
                                error(l_tokens[i], l_tokens[i+1])
