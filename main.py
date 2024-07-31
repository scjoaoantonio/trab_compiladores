import sys
import sintatico

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    
    arquivo_tokens = sys.argv[1]
    sintatico.main(arquivo_tokens)

if __name__ == '__main__':
    main()
