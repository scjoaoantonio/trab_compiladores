import re
#from parser import analisadorsintatico

arquivo = open("./input/lexico.txt")
#arquivo = open("./input/lexerror.txt")
entrada = arquivo.read()

l_token = []

t_numeros = "^(0(,\d{0,2})?|-?[1-9]\d*(,\d{1,20})?|-0,(0[1-9]|[1-9]\d?))$"
t_identificador = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
t_literal = r"[\"]+[%\w\s]+[\"]*"


reservadas = {
    'while': 'Comando de Laço',
    'for': 'Comando de Laço',
    'if': 'Comando de Condição',
    'else': 'Comando de Condição',
    'return': 'Comando de Retorno',
    'break': 'Comando de Parada',
    'continue': 'Comando de Continuação',
    'switch': 'Comando de Condição',
    'case': 'Comando de Condição',
    'printf': 'Comando para escrever na tela'
}
reservadas_key = reservadas.keys()


operadores = {
    '+': 'Operador de Soma',
    '-': 'Operador de Subtração',
    '*': 'Operador de Multiplicação',
    '/': 'Operador de Divisão',
    '%': 'Operador de Módulo',
    '=': 'Operador de Igualdade ou Atribuição',
    '==': 'Operdor de Igualdade',
    '!=': 'Operador de Diferença',
    '<': 'Operador "menor que.."',
    '>': 'Operador "maior que.."',
    '<=': 'Operador "menor ou igual"',
    '>=': 'Operador "maior ou igual"',
    '++': 'Operador de Incremento',
    '--': 'Operador de Decremento',
    '+=': 'Atribuição depois da soma',
    '-=': 'Atribuição depois da subtração',
    '*=': 'Atribuição depois do produto',
    '/=': 'Atribuição depois da divisão',
    '%=': 'Atribuição depois do módulo'
}
operadores_key = operadores.keys()

operadores_mudanca = {
    '++': 'Operador de Incremento',
    '--': 'Operador de Decremento',
}
operadores_mudanca_key = operadores_mudanca.keys()

operadores_logicos = {
    '&&': 'AND Lógico',
    '||': 'OR Lógico',
    '!': 'NOT Lógico'
}
operadores_logicos_key = operadores_logicos.keys()

tipo_variavel = {
    'int': 'Tipo Inteiro',
    'float': 'Tipo Float',
    'double': 'Tipo Double',
    'float': 'Tipo Float',
    'long': 'Tipo long',
    'char': 'Caractere',
    'const': 'Constante',
    'void': 'Parâmetro Vazio'
}
tipo_variavel_key = tipo_variavel.keys()

pontuacao = {
    ':': 'Dois pontos',
    ';': 'Ponto e Virgula',
    '.': 'Ponto',
    ',': 'Virgula',
    '(': 'Abre Parênteses',
    ')': 'Fecha Parênteses',
    '{': 'Abre Chave',
    '}': 'Fecha Chave',
    '[': 'Abre Colchete',
    ']': 'Fecha Colchete',
}
pontuacao_key = pontuacao.keys()

pontuacao_open = {
    '(': 'Abre Parênteses',
    '{': 'Abre Chave',
    '[': 'Abre Colchete'
}
pontuacao_open_key = pontuacao_open.keys()

pontuacao_close = {
    ')': 'Fecha Parênteses',
    '}': 'Fecha Chave',
    ']': 'Fecha Colchete'
}
pontuacao_close_key = pontuacao_close.keys()

comentario = {
    '//': 'Comentário'
}
comentario_key = comentario.keys()

aspas = {
    '"': 'Aspas duplas'
}
aspas_key = aspas.keys()
contador_linha = 0
contador_coluna = 0
count_token = 0
codigo = entrada.split("\n")
for linha in codigo:
    contador_linha = contador_linha + 1
    tokens = linha.split(' ')

    print("\n\n\nLinha", contador_linha, "->", linha, "\n")
    for token in tokens:
        if token in comentario_key:
            print("Token: [", token, "]-> Comentário ->", linha)
            tokens = " "
        elif (token not in operadores_key):
            if (token not in operadores_logicos_key):
                if (token not in tipo_variavel_key):
                    if (token not in pontuacao_key):
                        if (token not in reservadas_key):
                            if not(re.findall(t_identificador, token)):
                                if not(re.findall(t_numeros, token)):
                                    if not(re.findall(t_literal, token)):
                                        if(len(token) != 0):
                                            print(
                                                "Erro encontrado na linha", contador_linha, "e coluna", contador_coluna, "\nPalavra não identificada:", token)
    for token in tokens:
        if token in operadores_key:
            print("Token: [", token, "]-> Operador ->", operadores[token])
            l_token.append(token)
            count_token = count_token + 1
            contador_coluna += 1

        elif token in operadores_logicos_key:
            print("Token: [", token, "]-> Operador Lógico ->",
                  operadores_logicos[token])
            l_token.append(token)
            count_token = count_token + 1
            contador_coluna += 1

        elif token in tipo_variavel_key:
            print("Token: [", token, "]-> Variavel ->", tipo_variavel[token])
            l_token.append(token)
            count_token = count_token + 1
            contador_coluna += 1

        elif token in pontuacao_key:
            print("Token: [", token, "]-> Pontuacao ->", pontuacao[token])
            l_token.append(token)
            count_token = count_token + 1
            contador_coluna += 1

        elif token in reservadas_key:
            print("Token: [", token, "]-> Palavra reservada ->",
                  reservadas[token])
            l_token.append(token)
            count_token = count_token + 1
            contador_coluna += 1

        elif(re.findall(t_numeros, token)):
            print("Token: [", token, "]-> Número")
            l_token.append(token)
            count_token = count_token + 1
            contador_coluna += 1

        elif(re.findall(t_identificador, token)):
            print("Token: [", token, "]-> Identificador")
            l_token.append(token)
            count_token = count_token + 1
            contador_coluna += 1

        elif(re.findall(t_literal, token)):
            print("Token: [", token, "]-> Literal")
            l_token.append(token)
            count_token = count_token + 1
            contador_coluna += 1

    contador_coluna = 0

'''
             
"""Identifica Literal"""
   if estado is 3:
            if re.match(r"[%a-zA-z0-9\"\s]", k):
                token = token + k
                if re.match(r"[\"]", k):
                    lit = re.match(r"[\"]+[%\w\s]+[\"]*", token)
                    if lit is not None:
                        tabela_token[id_tabela] = ["Literal", lit.group(
                        ), add_linha_coluna(lit.group(), linha, coluna)]

                        token_geral.append(
                            ["Literal", lit.group(), id_tabela])
                        token = ""
                        estado = 0
'''

with open('tokens.txt', 'w') as temp_file:
    for item in l_token:
        temp_file.write("%s\n" % item)

print("\n\n\n")

# analisadorsintatico()
