# =========================================================== #
#   Trabalho de Compiladores - Parte 3: Analisador Sintático  #
#                                                             #
#   Disciplina: INE5622 - Introdução a Compiladores           #
#                                                             #
#     Docente:                                                #
#         Daniel Santana de Freitas                           #
#                                                             #
#     Grupo:                                                  #
#       - Arthur Lorenzetti da Rosa     19200621              #
#       - Jacqueline Correia Beber      19200634              #
#                                                             #
#   Data: 24/11/2025                                          #
# =========================================================== #


Descrição do Trabalho:
    
    A terceira parte do trabalho implementa um Analisador Sintático com base na Tabela de Reconhecimento Sintático criada na Parte 2.
    
    A elaboração da tabela pode ser encontrada no pdf presente na pasta Parte_2_analisador_sintatico_PDF.
        
    Para uma melhor visualização criamos ela no GoogleSheets, no seguinte link:
        https://docs.google.com/spreadsheets/d/1cVK4ZIDSYa3Rqk-xt89RHHR0i-8UtqpUAtw74EK-S_U/edit?usp=sharing 

Requisitos do Sistema:

    Python3 instalado.

    Versão Testada: Python 3.12.3, utilizando o WSL:Ubuntu.

    Dependências: Nenhuma (usa apenas biblioteca padrão do Python).

Como Executar o Programa:

    Para executar o código você deve rodar o seguinte trecho, alterando caminho_do_arquivo.lsi para o caminho do arquivo correto:

            python3 Parte_3_analisador_sintatico/src/main.py caminho_do_arquivo.lsi
        
        Exemplo utilizando os testes criados:

            Arquivo de Teste Correto:

                python3 Parte_3_analisador_sintatico/src/main.py Parte_3_analisador_sintatico/src/testes/arquivo_de_entrada_correto.lsi
            
            Arquivos de Testes Incorretos:

                python3 Parte_3_analisador_sintatico/src/main.py Parte_3_analisador_sintatico/src/testes/arquivo_de_entrada_incorreto1.lsi
                python3 Parte_3_analisador_sintatico/src/main.py Parte_3_analisador_sintatico/src/testes/arquivo_de_entrada_incorreto2.lsi
                python3 Parte_3_analisador_sintatico/src/main.py Parte_3_analisador_sintatico/src/testes/arquivo_de_entrada_incorreto3.lsi
    
Saídas Esperadas:

    Para arquivos corretos:

        - Parser preditivo guiado por tabela;

        - Mensagem de sucesso.

     Para arquivos incorretos:

        - Mensagem de erro indicando o caractere esperado, o caractere que foi encontrado, a linha e a coluna do erro sintático capturado
          pelo analisador.