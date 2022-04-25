# ----------------------------------------------------------------------------
# Analisador Léxico - Compiladores - UFSJ
# Created By  : João Antônio Santos Carvalho
# Created Date: 04 / 2022
# Version = '1.0'
# Language: Python
# ----------------------------------------------------------------------------

# Importação do REGEX para funções regulares
import re

# Abrir o arquivo de entrada
arquivo = open("./input/lexico.txt")

# Expressão regular para identificar números e identificadores
# São considerados numeros inteiros, positivos, negativos e separados por vírgula em até 20 casas decimais
# São considerados como identificadores, palavras não iniciadas por números ou caracteres especiais
t_numeros = "^(0(,\d{0,2})?|-?[1-9]\d*(,\d{1,20})?|-0,(0[1-9]|[1-9]\d?))$"
t_identificador = "^[a-zA-Z_]+[a-zA-Z0-9_]*"

# Tokens (palavras reservadas)
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
    'printf': 'Comando para escrever na tela',
    'void': 'Indicação de Parâmetro Vazio',
    'main': 'Indicação da Função Principal'
}
reservadas_key = reservadas.keys()

# Tokens (operadores)
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

# Tokens (operadores lógicos)
operadores_logicos = {
    '&&': 'AND Lógico',
    '||': 'OR Lógico',
    '!': 'NOT Lógico'
}
operadores_logicos_key = operadores_logicos.keys()

# Tokens (tipos de variáveis)
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

# Tokens (pontuação)
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

# Tokens (comentário)
comentario = {
    '//': 'Comentário'
}
comentario_key = comentario.keys()

# Leitura do arquivo de entrada
entrada = arquivo.read()

# Contador de linhas, cada linha vai até o \n
count = 0
codigo = entrada.split("\n")
for linha in codigo:
    count = count + 1

    # O programa vai ler até o final da linha e identificar os tokens (separados por um "espaço")
    # Vai ver todos os tokens e se não for identificado como palavra reservada irá ser considerado como erro léxico
    # Se tiver um comentário, irá ignorar a linha e considerá-la um comentário.
    # Se identificar uma palavra reservada, vai enviá-la como saída do programa
    tokens = linha.split(' ')

    print("\n\n\nLinha", count, "->", linha, "\n")
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
                                    if(len(token) != 0):
                                        print(
                                            "Erro encontrado na linha", count, "\nPalavra não identificada:", token)
    for token in tokens:
        if token in operadores_key:
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

print("\n\n\n")
