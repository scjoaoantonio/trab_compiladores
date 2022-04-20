import re

arquivo = open("lexico.t")

t_numeros = "^(\d+)$"
t_identificador = "^[a-zA-Z_]+[a-zA-Z0-9_]*"

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
    'void': 'Indicação de Parâmetro Vazio',
    'main': 'Indicação da Função Principal'
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
    'const': 'Constante'
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
    ']': 'Fecha Colchete'
}
pontuacao_key = pontuacao.keys()

comentario = {
    '//': 'Comentário'
}
comentario_key = comentario.keys()

numeros = {
    '0': 'Numero 0',
    '1': 'Numero 1',
    '2': 'Numero 2',
    '3': 'Numero 3',
    '4': 'Numero 4',
    '5': 'Numero 5',
    '6': 'Numero 6',
    '7': 'Numero 7',
    '8': 'Numero 8',
    '9': 'Numero 9'
}
numeros_key = numeros.keys()


entrada = arquivo.read()

count = 0
codigo = entrada.split("\n")
for linha in codigo:
    count = count + 1

    tokens = linha.split(' ')

    # for token in tokens:
    #     if(re.findall(t_Numerals, token)):
    #         print(token, "-------> Numeral")
    #     elif(re.findall(t_ID, token)):
    #         print(token, "-------> Identifiers")
    #     else:
    #         print("Unknown Value")

    print("\n\n\nLinha", count, "->", linha, "\n")
    print(tokens)
    for token in tokens:
        if token in comentario_key:
            print("Token: [", token, "]-> Comentário ->", linha)
        elif token in operadores_key:
            print("Token: [", token, "]-> Operador ->", operadores[token])
        elif token in operadores_logicos_key:
            print("Token: [", token, "]-> Operador Lógico ->",
                  operadores_logicos[token])
        elif token in tipo_variavel_key:
            print("Token: [", token, "]-> Variavel ->", tipo_variavel[token])
        elif token in pontuacao_key:
            print("Token: [", token, "]-> Pontuacao ->", pontuacao[token])
        elif token in reservadas_key:
            print("Token: [", token, "]-> Palavra reservada ->",
                  reservadas[token])
        elif(re.findall(t_numeros, token)):
            print("Token: [", token, "]-> Número")
        elif(re.findall(t_identificador, token)):
            print("Token: [", token, "]-> Identificador")


print("\n\n\n\n===============================================================\n\n\n")
