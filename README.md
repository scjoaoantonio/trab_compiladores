# Analisador Léxico

## Sobre o Trabalho

- Trabalho para a matéria de **Compiladores** do Curso de Ciências da Computação - UFSJ
- Analisador Léxico para uma linguagem descrita como "Mini-C" programada em Python
- Para compilar digite no terminal: python main.py
  - Requer instalado: Python

## Sobre o Programa

#### Regras:

1. O Analisador Léxico recebe como código-fonte o programa contido no arquivo "lexico.txt"
2. O programa enviado para o analisador deve seguir as seguintes especificações:

   - Tudo que estiver escrito deve ser separado por um espaço, até mesmo das pontuações.

   - O analisador verificará cada linha do código até a quebra de linha

   - Os comentários são identificados por // e devem ser escritos no início da linha do código

   - Qualquer palavra que não está na lista abaixo será considerada um erro léxico:
     1. Números
     2. Identificadores (palavras que não começam com caracteres especiais)
     3. Palavras reservadas em C (while, for, if, else, return, break, continue, switch, case, printf, scanf, void, main)
     4. Operadores matemáticos e lógicos
     5. Tipo de variável (int, float, double, float, long, char, "const")
     6. Pontuação
     7. Comentário
