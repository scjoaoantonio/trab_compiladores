# Importação do REGEX
import re
import os

# Criação de listas para armazenamento de dados
cod_variaveis = []
lex_variaveis = []
re_numeros = "^(0(,\d{0,2})?|-?[1-9]\d*(,\d{1,20})?|-0,(0[1-9]|[1-9]\d?))$"

def remove_files():
    files_to_remove = ['codigo1.txt', 'codigo2.txt','tokens.txt']
    for file in files_to_remove:
        try:
            os.remove(file)
        except FileNotFoundError:
            print(f"{file} not found, skipping.")
        except Exception as e:
            print(f"Error removing {file}: {e}")
            
# Função para juntar os arquivos .data e .text
def juntarcodigos():
    with open("./output/codigo.txt", "w") as arq:
        with open("codigo1.txt", "r") as arq1:
            arq.write(arq1.read())
        with open("codigo2.txt", "r") as arq2:
            arq.write(arq2.read())
    remove_files()

# Função para gerar declaração / atribuição de variáveis
def gerardeclaracao(cont, variavel, valor):
    lex_variaveis.append(str(variavel))
    cod_variaveis.append("$r" + str(cont))
    variavel = "loadi $r" + str(cont)
    with open('codigo1.txt', 'a') as codigo:
        codigo.write(variavel + ', ' + valor + '\n')

# Função para adaptar a soma em C para soma em linguagem de máquina
def gerarsoma(cont, num1, num2):
    if lex_variaveis[cont] == str(num1):
        num1 = cod_variaveis[cont]
    elif lex_variaveis[cont] == str(num2):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1, " + num1 + '\n')
        codigo.write("mov $t2, " + num2 + '\n')
        codigo.write("add " + cod_variaveis[cont] + ', $t1, $t2\n')

# Função para adaptar a subtração em C para subtração em linguagem de máquina
def gerarsub(cont, num1, num2):
    if lex_variaveis[cont] == str(num1):
        num1 = cod_variaveis[cont]
    elif lex_variaveis[cont] == str(num2):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1, " + num1 + '\n')
        codigo.write("mov $t2, " + num2 + '\n')
        codigo.write("sub " + cod_variaveis[cont] + ', $t1, $t2\n')

# Função para adaptar a divisão em C para divisão em linguagem de máquina
def gerardiv(cont, num1, num2):
    if lex_variaveis[cont] == str(num1):
        num1 = cod_variaveis[cont]
    elif lex_variaveis[cont] == str(num2):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1, " + num1 + '\n')
        codigo.write("mov $t2, " + num2 + '\n')
        codigo.write("div " + cod_variaveis[cont] + ', $t1, $t2\n')

# Função para adaptar a multiplicação em C para multiplicação em linguagem de máquina
def gerarmult(cont, num1, num2):
    if lex_variaveis[cont] == str(num1):
        num1 = cod_variaveis[cont]
    elif lex_variaveis[cont] == str(num2):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1, " + num1 + '\n')
        codigo.write("mov $t2, " + num2 + '\n')
        codigo.write("mul " + cod_variaveis[cont] + ', $t1, $t2\n')

# Função para adaptar a comparação 'se é igual' em C para comparação em linguagem de máquina
def gerarigual(cont, num1, num2, cont_label):
    cont_label -= 1
    saida = 'saida' + str(cont_label)
    if lex_variaveis[cont] == str(num1):
        num1 = cod_variaveis[cont]
    elif lex_variaveis[cont] == str(num2):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1, " + num1 + '\n')
        codigo.write("mov $t2, " + num2 + '\n')
        codigo.write("beq $t1, $t2, " + saida + '\n')

# Função para adaptar a comparação 'se é diferente' em C para comparação em linguagem de máquina
def gerardiferente(cont, num1, num2, cont_label):
    cont_label -= 1
    saida = 'saida' + str(cont_label)
    if lex_variaveis[cont] == str(num1):
        num1 = cod_variaveis[cont]
    elif lex_variaveis[cont] == str(num2):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1, " + num1 + '\n')
        codigo.write("mov $t2, " + num2 + '\n')
        codigo.write("bne $t1, $t2, " + saida + '\n')

# Função para adaptar a comparação 'se é menor que' em C para comparação em linguagem de máquina
def gerarmenorque(cont, num1, num2, cont_label):
    cont_label -= 1
    saida = 'saida' + str(cont_label)
    if lex_variaveis[cont] == str(num1):
        num1 = cod_variaveis[cont]
    elif lex_variaveis[cont] == str(num2):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1, " + num1 + '\n')
        codigo.write("mov $t2, " + num2 + '\n')
        codigo.write("blt $t1, $t2, " + saida + '\n')

# Função para adaptar a comparação 'se é maior que' em C para comparação em linguagem de máquina
def gerarmaiorque(cont, num1, num2, cont_label):
    cont_label -= 1
    saida = 'saida' + str(cont_label)
    if lex_variaveis[cont] == str(num1):
        num1 = cod_variaveis[cont]
    elif lex_variaveis[cont] == str(num2):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1, " + num1 + '\n')
        codigo.write("mov $t2, " + num2 + '\n')
        codigo.write("bgt $t1, $t2, " + saida + '\n')

# Função para adaptar a comparação 'se é menor ou igual que' em C para comparação em linguagem de máquina
def gerarmenorigual(cont, num1, num2, cont_label):
    cont_label -= 1
    saida = 'saida' + str(cont_label)
    if lex_variaveis[cont] == str(num1):
        num1 = cod_variaveis[cont]
    elif lex_variaveis[cont] == str(num2):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1, " + num1 + '\n')
        codigo.write("mov $t2, " + num2 + '\n')
        codigo.write("ble $t1, $t2, " + saida + '\n')

# Função para adaptar a comparação 'se é maior ou igual que' em C para comparação em linguagem de máquina
def gerarmaiorigual(cont, num1, num2, cont_label):
    cont_label -= 1
    saida = 'saida' + str(cont_label)
    if lex_variaveis[cont] == str(num1):
        num1 = cod_variaveis[cont]
    elif lex_variaveis[cont] == str(num2):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1, " + num1 + '\n')
        codigo.write("mov $t2, " + num2 + '\n')
        codigo.write("bge $t1, $t2, " + saida + '\n')

# Função que irá gerar o finalizador do programa
def gerarfim():
    with open('codigo2.txt', 'a') as codigo:
        codigo.write('\nli $v0, 10\nsyscall\n')

# Função para converter a função de escrever na tela, de C para linguagem de máquina
# é possível escrever na tela: palavras, números ou caracteres
def gerarprint(texto, numtexto):
    p_token = ['"', "'"]
    literal = texto.translate(str.maketrans('', '', ''.join(p_token)))
    nometexto = "msg" + str(numtexto)
    if re.findall(re_numeros, literal):
        with open('codigo1.txt', 'a') as codigo:
            codigo.write(nometexto + ': .word "' + literal + '"\n')
        with open('codigo2.txt', 'a') as codigo:
            codigo.write('li $v0, 1\n')
            codigo.write('la $a' + str(numtexto) + ', ' + nometexto + '\n')
            codigo.write('syscall\n')
    else:
        if len(literal) > 1:
            with open('codigo1.txt', 'a') as codigo:
                codigo.write(nometexto + ': .asciiz "' + literal + '"\n')
        elif len(literal) <= 1:
            with open('codigo1.txt', 'a') as codigo:
                codigo.write(nometexto + ': .byte "' + literal + '"\n')
        with open('codigo2.txt', 'a') as codigo:
            codigo.write('li $v0, 4\n')
            codigo.write('la $a' + str(numtexto) + ', ' + nometexto + '\n')
            codigo.write('syscall\n')

# Função para converter um comentário em C para comentário em assembly
def gerarcomentario(texto):
    c_token = '//'
    comentario = texto.translate(str.maketrans('', '', c_token))
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("#" + comentario + "\n")

# Função para gerar laço de repetição for
def gerarfor(num):
    label = 'label' + str(num)
    with open('codigo2.txt', 'a') as codigo:
        codigo.write(label + ':\n')

# Função para gerar laço de repetição while
def gerarwhile(num):
    label = 'label' + str(num)
    with open('codigo2.txt', 'a') as codigo:
        codigo.write(label + ':\n')

# Função para gerar condição if
def gerarif(num):
    label = 'label' + str(num)
    with open('codigo2.txt', 'a') as codigo:
        codigo.write(label + ':\n')

# Função para finalizar os labels (laços de repetição)
def fecharlabel(num, fechar):
    saida = 'saida' + str(num)
    label = 'label' + str(num)
    with open('codigo2.txt', 'a') as codigo:
        if fechar == 'sim':
            codigo.write("jump " + label + '\n' + saida + ':\n')
        else:
            codigo.write(saida + ':\n')
