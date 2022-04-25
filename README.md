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
     a). Números
     b). Identificadores (palavras que não começam com caracteres especiais)
     c). Palavras reservadas em C (while, for, if, else, return, break, continue, switch, case, printf, scanf, void, main)
     d). Operadores matemáticos e lógicos
     e). Tipo de variável (int, float, double, float, long, char, "const")
     f). Pontuação
     g). Comentário

## Exemplo
### Entrada do Programa

![WhatsApp Image 2022-04-25 at 18 02 39](https://user-images.githubusercontent.com/65183458/165174914-a50ef26f-28be-4fb0-be3b-c111600283bc.jpeg)

### Saída do Programa

![WhatsApp Image 2022-04-25 at 18 01 45](https://user-images.githubusercontent.com/65183458/165174908-e3656f09-47b3-4d40-bc70-a3b3d60532c1.jpeg)
![WhatsApp Image 2022-04-25 at 18 02 02](https://user-images.githubusercontent.com/65183458/165174911-f0ea21ae-dd85-4f37-8484-8cd16eafc5d4.jpeg)
![WhatsApp Image 2022-04-25 at 18 02 18](https://user-images.githubusercontent.com/65183458/165174913-8b1672c6-f2a0-4ddd-878a-e8cbf99656a3.jpeg)
