# Importação do REGEX para funções regulares
import re
# Importação de funções do gerador de código
from compiler import gerador
import sys

# Redirecionar a saída padrão para o arquivo 'saida.txt'
sys.stdout = open('./output/codetokens.txt', 'w')

# Abrir e ler o arquivo de entrada
arquivo = open("./input/lexico.txt")
entrada = arquivo.read()

# Declaração de listas vazias, tokens e colunas
l_token = []
col_token = []

# O programa assim que ser inicializado irá abir e limpar 2 arquivos diferentes para a geração do código na linguagem de máquina, um irá gerar os códigos referentes ao .data e o outro ao .text
with open('codigo1.txt', 'w') as codigo:
    codigo.write('.data\n')

with open('codigo2.txt', 'w') as codigo:
    codigo.write('\n\n.text\n')

# Expressão regular para identificar números, identificadores e literais
# São considerados numeros inteiros, positivos, negativos e separados por vírgula em até 20 casas decimais
# São considerados como identificadores, palavras não iniciadas por números ou caracteres especiais
# São considerados como literais, palavras seguidas de aspas
t_numeros = "^(0(,\d{0,2})?|-?[1-9]\d*(,\d{1,20})?|-0,(0[1-9]|[1-9]\d?))$"
t_identificador = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
t_literal = r"[\"]+[%\w\s]+[\"]*"

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
    'printf': 'Comando para escrever na tela'
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

operadores_mudanca = {
    '++': 'Operador de Incremento',
    '--': 'Operador de Decremento',
}
operadores_mudanca_key = operadores_mudanca.keys()

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
    'const': 'Constante',
    'void': 'Parâmetro Vazio'
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

# Tokens (comentário)
comentario = {
    '//': 'Comentário'
}
comentario_key = comentario.keys()


# Função para indicar erro no léxico do código
def erro():
    print("Erro encontrado na linha", contador_linha,
          "\nPalavra não identificada:", token)


# Função para adicionar o token na lista de tokens
def addtoken(token):
    l_token.append(token)


# Declaração de variáveis para a contagem de linhas, colunas, tokens
contador_linha = 0
contador_coluna = 0
count_token = 0
temp = 0

# O programa vai ler até o final da linha e identificar os tokens (separados por um "espaço")
# Vai ver todos os tokens e se não for identificado como palavra reservada irá ser considerado como erro léxico
# Se tiver um comentário, irá ignorar a linha e considerá-la um comentário, além de mandá-la para o gerador transformar o comentário em C em um comentário em Assembly
# Se identificar uma palavra reservada, vai enviá-la como saída do programa
codigo = entrada.split("\n")
for linha in codigo:
    contador_linha = contador_linha + 1
    tokens = linha.split(' ')

    print("\n\n\nLinha", contador_linha, "->", linha, "\n")
    for token in tokens:
        if token in comentario_key:
            print("Token: [", token, "]-> Comentário ->", linha)
            gerador.gerarcomentario(linha)
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
                                            erro()
                                        else:
                                            temp = 1

    if (temp == 1):
        for token in tokens:
            if token in operadores_key:
                count_token = count_token + 1
                contador_coluna += len(token) + 1
                col_token = contador_coluna - len(token)
                print("[", contador_linha, col_token, "]"" Token: [",
                      token, "]-> Operador ->", operadores[token])
                addtoken(token)

            elif token in operadores_logicos_key:
                addtoken(token)
                count_token = count_token + 1
                contador_coluna += len(token) + 1
                col_token = contador_coluna - len(token)
                print("[", contador_linha, col_token, "]"" Token: [", token, "]-> Operador Lógico ->",
                      operadores_logicos[token])

            elif token in tipo_variavel_key:
                addtoken(token)
                count_token = count_token + 1
                contador_coluna += len(token) + 1
                col_token = contador_coluna - len(token)
                print("[", contador_linha, col_token, "]"" Token: [", token, "]-> Variavel ->",
                      tipo_variavel[token])

            elif token in pontuacao_key:
                addtoken(token)
                count_token = count_token + 1
                contador_coluna += len(token) + 1
                col_token = contador_coluna - len(token)
                print("[", contador_linha, col_token, "]"" Token: [",
                      token, "]-> Pontuacao ->", pontuacao[token])

            elif token in reservadas_key:
                addtoken(token)
                count_token = count_token + 1
                contador_coluna += len(token) + 1
                col_token = contador_coluna - len(token)
                print("[", contador_linha, col_token, "]"" Token: [", token, "]-> Palavra reservada ->",
                      reservadas[token])

            elif(re.findall(t_numeros, token)):
                addtoken(token)
                count_token = count_token + 1
                contador_coluna += len(token) + 1
                col_token = contador_coluna - len(token)
                print("[", contador_linha, col_token,
                      "]"" Token: [", token, "]-> Número")

            elif(re.findall(t_identificador, token)):
                addtoken(token)
                count_token = count_token + 1
                contador_coluna += len(token) + 1
                col_token = contador_coluna - len(token)
                print("[", contador_linha, col_token,
                      "]"" Token: [", token, "]-> Identificador")

            elif(re.findall(t_literal, token)):
                addtoken(token)
                count_token = count_token + 1
                contador_coluna += len(token) + 1
                col_token = contador_coluna - len(token)
                print("[", contador_linha, col_token,
                      "]"" Token: [", token, "]-> Literal")
        contador_coluna = 0


# Salvar os tokens em um arquivo separado
with open('tokens.txt', 'w') as temp_file:
    for item in l_token:
        temp_file.write("%s\n" % item)

# Fechar o arquivo de saída
sys.stdout.close()
sys.stdout = sys.__stdout__
