# ======================================================== #
# Trabalho de Compiladores - Parte 1: Analisador Léxico    #
#                                                          #
#     Grupo:                                               #
#       - Arthur Lorenzetti da Rosa     19200621           #
#       - Jacqueline Correia Beber      19200634           #
# ======================================================== #

import sys
from lexer.analisador_lexico import AnalisadorLexico

def main():
    print("\n" + "=" * 60)
    print("O Analisador Léxico foi iniciado ...")
    print("=" * 60)

    if len(sys.argv) != 2:
        print("Uso correto:")
        print(f"python3 {sys.argv[0]} <caminho_do_arquivo.lsi>")
        print("\nExemplo:")
        print(f"python3 {sys.argv[0]} testes/programa_correto.lsi")
        print()
        sys.exit(1)

    caminho_arquivo = sys.argv[1]

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            codigo_fonte = arquivo.read()

        print(f"Arquivo lido: {caminho_arquivo}")
        print(f"Tamanho: {len(codigo_fonte)} caracteres\n")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado!")
        print("Verifique se o caminho está correto.\n")
        sys.exit(1)

    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}\n")
        sys.exit(1)

    lexer = AnalisadorLexico(codigo_fonte)

    try:
        print("Iniciando análise léxica...\n")
        tokens = lexer.analisar_codigo_fonte()

        print("Análise léxica concluída sem erros!\n")

        lexer.imprimir_tokens()

        lexer.tabela_de_simbolos.imprimir_tabela_de_simbolos()

        print("="*70 + "\n")
    
    except Exception as e:
        print("Erro encontrado!\n")
        print("="*70)
        print(f"Erro: {str(e)}")
        print("="*70 + "\n")
        sys.exit(1)

if __name__ == "__main__":
    main()