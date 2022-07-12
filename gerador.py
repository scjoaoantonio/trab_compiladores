import re

cod_variaveis = []
lex_variaveis = []
re_numeros = "^(0(,\d{0,2})?|-?[1-9]\d*(,\d{1,20})?|-0,(0[1-9]|[1-9]\d?))$"


def juntarcodigos():
    arq = open("gerado.txt", "w")
    arq1 = open("codigo.txt", "r")
    arq2 = open("codigo2.txt", "r")
    arq.write(arq1.read()+arq2.read())
    arq.close()


def gerardeclaracao(cont, variavel, valor):
    lex_variaveis.append(str(variavel))
    cod_variaveis.append("$r"+str(cont))
    variavel = "loadi $r" + str(cont)
    with open('codigo.txt', 'a') as codigo:
        codigo.write(variavel + ', ' + valor + '\n')


def gerarsoma(cont, num1, num2):
    if(lex_variaveis[cont] == str(num1)):
        num1 = cod_variaveis[cont]
    elif(lex_variaveis[cont] == str(num2)):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1" + ', ' + num1 + '\n')
        codigo.write("mov $t2" + ', ' + num2 + '\n')
        codigo.write("add " + cod_variaveis[cont] + ',' + '$t1, $t2' + '\n')


def gerarsub(cont, num1, num2):
    if(lex_variaveis[cont] == str(num1)):
        num1 = cod_variaveis[cont]
    elif(lex_variaveis[cont] == str(num2)):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1" + ', ' + num1 + '\n')
        codigo.write("mov $t2" + ', ' + num2 + '\n')
        codigo.write("sub " + cod_variaveis[cont] + ',' + '$t1, $t2' + '\n')


def gerardiv(cont, num1, num2):
    if(lex_variaveis[cont] == str(num1)):
        num1 = cod_variaveis[cont]
    elif(lex_variaveis[cont] == str(num2)):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1" + ', ' + num1 + '\n')
        codigo.write("mov $t2" + ', ' + num2 + '\n')
        codigo.write("div " + cod_variaveis[cont] + ',' + '$t1, $t2' + '\n')


def gerarmult(cont, num1, num2):
    if(lex_variaveis[cont] == str(num1)):
        num1 = cod_variaveis[cont]
    elif(lex_variaveis[cont] == str(num2)):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1" + ', ' + num1 + '\n')
        codigo.write("mov $t2" + ', ' + num2 + '\n')
        codigo.write("mul " + cod_variaveis[cont] + ',' + '$t1, $t2' + '\n')


def gerarigual(cont, num1, num2, cont_label):
    cont_label -= 1
    saida = 'saida' + str(cont_label)
    if(lex_variaveis[cont] == str(num1)):
        num1 = cod_variaveis[cont]
    elif(lex_variaveis[cont] == str(num2)):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1" + ', ' + num1 + '\n')
        codigo.write("mov $t2" + ', ' + num2 + '\n')
        codigo.write("beq " + '$t1, $t2, ' + saida + '\n')


def gerardiferente(cont, num1, num2, cont_label):
    cont_label -= 1
    saida = 'saida' + str(cont_label)
    if(lex_variaveis[cont] == str(num1)):
        num1 = cod_variaveis[cont]
    elif(lex_variaveis[cont] == str(num2)):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1" + ', ' + num1 + '\n')
        codigo.write("mov $t2" + ', ' + num2 + '\n')
        codigo.write("bne " + '$t1, $t2, ' + saida + '\n')


def gerarmenorque(cont, num1, num2, cont_label):
    cont_label -= 1
    saida = 'saida' + str(cont_label)
    if(lex_variaveis[cont] == str(num1)):
        num1 = cod_variaveis[cont]
    elif(lex_variaveis[cont] == str(num2)):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1" + ', ' + num1 + '\n')
        codigo.write("mov $t2" + ', ' + num2 + '\n')
        codigo.write("blt " + '$t1, $t2, ' + saida + '\n')


def gerarmaiorque(cont, num1, num2, cont_label):
    cont_label -= 1
    saida = 'saida' + str(cont_label)
    if(lex_variaveis[cont] == str(num1)):
        num1 = cod_variaveis[cont]
    elif(lex_variaveis[cont] == str(num2)):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1" + ', ' + num1 + '\n')
        codigo.write("mov $t2" + ', ' + num2 + '\n')
        codigo.write("bgt " + '$t1, $t2, ' + saida + '\n')


def gerarmenorigual(cont, num1, num2, cont_label):
    cont_label -= 1
    saida = 'saida' + str(cont_label)
    if(lex_variaveis[cont] == str(num1)):
        num1 = cod_variaveis[cont]
    elif(lex_variaveis[cont] == str(num2)):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1" + ', ' + num1 + '\n')
        codigo.write("mov $t2" + ', ' + num2 + '\n')
        codigo.write("ble " + '$t1, $t2, ' + saida + '\n')


def gerarmaiorigual(cont, num1, num2, cont_label):
    cont_label -= 1
    saida = 'saida' + str(cont_label)
    if(lex_variaveis[cont] == str(num1)):
        num1 = cod_variaveis[cont]
    elif(lex_variaveis[cont] == str(num2)):
        num2 = cod_variaveis[cont]
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("mov $t1" + ', ' + num1 + '\n')
        codigo.write("mov $t2" + ', ' + num2 + '\n')
        codigo.write("bge " + '$t1, $t2, ' + saida + '\n')


def gerarfim():
    with open('codigo2.txt', 'a') as codigo:
        codigo.write('\nli $v0, 10')


def gerarprint(texto, numtexto):
    p_token = ['"', "'"]
    literal = texto.translate(str.maketrans('', '', ''.join(p_token)))
    nometexto = "msg" + str(numtexto)
    if(re.findall(re_numeros, literal)):
        with open('codigo.txt', 'a') as codigo:
            codigo.write(nometexto + ':' + ' .word ' + '"' + literal + '"\n')
        with open('codigo2.txt', 'a') as codigo:
            codigo.write('li $v0, 1' + '\n')
            codigo.write('la $a' + numtexto + ', ' + nometexto + '\n')
            codigo.write('syscall\n')
    else:
        if(len(literal) > 1):
            with open('codigo.txt', 'a') as codigo:
                codigo.write(nometexto + ':' + ' .asciiz ' +
                             '"' + literal + '"\n')
        elif(len(literal) <= 1):
            with open('codigo.txt', 'a') as codigo:
                codigo.write(nometexto + ':' + ' .byte ' +
                             '"' + literal + '"\n')

    with open('codigo2.txt', 'a') as codigo:
        codigo.write('li $v0, 4' + '\n')
        codigo.write('la $a' + numtexto + ', ' + nometexto + '\n')
        codigo.write('syscall\n')


def gerarcomentario(texto):
    c_token = '//'
    comentario = texto.translate(str.maketrans('', '', c_token))
    with open('codigo2.txt', 'a') as codigo:
        codigo.write("#" + comentario + "\n")


def gerarfor(num):
    label = 'label' + str(num)
    with open('codigo2.txt', 'a') as codigo:
        codigo.write(str(label)+':\n')


def gerarwhile(num):
    label = 'label' + str(num)
    with open('codigo2.txt', 'a') as codigo:
        codigo.write(str(label)+':\n')


def gerarif(num):
    label = 'label' + str(num)
    with open('codigo2.txt', 'a') as codigo:
        codigo.write(str(label)+':\n')


def fecharlabel(num, fechar):
    saida = 'saida' + str(num)
    label = 'label' + str(num)
    if(fechar == 'sim'):
        with open('codigo2.txt', 'a') as codigo:
            codigo.write("jump "+label+':\n'+saida+':\n')
    else:
        with open('codigo2.txt', 'a') as codigo:
            codigo.write(saida+':\n')
