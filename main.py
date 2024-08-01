# ----------------------------------------------------------------------------
# Compiladores - UFSJ
# Created Date: 04 / 2022
# Updated 2.0 Date: 06 / 2022
# Updated 3.0 Date: 07 / 2022
# Updated 4.0 Date: 08 / 2024
# Language: Python
# Version = '4.0'
# Created By  : João Antônio Santos Carvalho (@scjoaoantonio)
# ----------------------------------------------------------------------------

import sys
from compiler import sintatico

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    
    arquivo_tokens = sys.argv[1]
    sintatico.main(arquivo_tokens)

if __name__ == '__main__':
    main()
