# ==== #
# Trabalho de Compiladores - Parte 3: Integração Lexer + Parser
# ==== #

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from Parte_1_analisador_lexico.src.lexer.analisador_lexico import AnalisadorLexico
from parser.analisador_sintatico import AnalisadorSintatico


def main():
    print("\n" + "=" * 60)
    print("Compilador LSI-2025-2 - Analisador Léxico e Sintático")
    print("=" * 60)

    if len(sys.argv) != 2:
        print("Uso correto: python3 main_part3.py <arquivo.lsi>")
        sys.exit(1)

    caminho_arquivo = sys.argv[1]

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            codigo_fonte = arquivo.read()
    except Exception as e:
        print(f"Erro ao ler arquivo: {e}")
        sys.exit(1)

    # 1. Análise Léxica
    print(f"1. Iniciando Análise Léxica em '{caminho_arquivo}'...")
    lexer = AnalisadorLexico(codigo_fonte)
    try:
        tokens = lexer.analisar_codigo_fonte()
        print("   -> Sucesso Léxico! Tokens gerados.")
    except Exception as e:
        print(f"   -> {e}")
        sys.exit(1)

    # 2. Análise Sintática
    print("\n2. Iniciando Análise Sintática...")
    parser = AnalisadorSintatico(tokens)
    try:
        parser.analisar()
        print("\n   -> O código fonte pertence à linguagem LSI-2025-2.")
    except Exception as e:
        print(f"\n   -> {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()