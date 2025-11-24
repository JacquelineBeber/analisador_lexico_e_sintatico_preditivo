# ======================================================== #
#   Trabalho de Compiladores - Parte 1: Analisador Léxico  #
#                                                          #
#   Disciplina: INE5622 - Introdução a Compiladores        #
#                                                          #
#     Docente:                                             #
#         Daniel Santana de Freitas                        #
#                                                          #
#     Grupo:                                               #
#       - Arthur Lorenzetti da Rosa     19200621           #
#       - Jacqueline Correia Beber      19200634           #
#                                                          #
#   Data: 24/11/2025                                       #
# ======================================================== #

Descrição do Trabalho:
    
    A primeira parte do trabalho implementa um Analisador Léxico para a linguagem LSI-2025-2.

Requisitos do Sistema:

    Python3 instalado.

    Versão Testada: Python 3.12.3, utilizando o WSL:Ubuntu.

    Dependências: Nenhuma (usa apenas biblioteca padrão do Python).

Como Executar o Programa:

    Para executar o código você rodar o seguinte trecho, alterando caminho_do_arquivo.lsi para o caminho do arquivo correto:

            python3 Parte_1_analisador_lexico/src/main.py caminho_do_arquivo.lsi
        
        Exemplo utilizando os testes criados:

            Arquivo de Teste Correto:

                python3 Parte_1_analisador_lexico/src/main.py Parte_1_analisador_lexico/src/testes/arquivo_de_entrada_correto.lsi
            
            Arquivo de Teste Incorreto:

                python3 Parte_1_analisador_lexico/src/main.py Parte_1_analisador_lexico/src/testes/arquivo_de_entrada_incorreto.lsi
    
Saídas Esperadas:

    Para arquivos corretos:

        - Lista de tokens encontrados

        - Tabela de símbolos com palavras-chave e identificadores

        - Mensagem de sucesso
    
        * É possível verificar uma lista de tokens mais detalhada, para isso descomente as linhas 204 a 209 do arquivo analisador_lexico,
        ele pode ser encontrado dentro de src/lexer/analisador_lexico.py

     Para arquivos incorretos:

        - Mensagem de erro indicando a linha e coluna do erro léxico, assim como o caracter inválido

