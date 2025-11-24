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

        Foram craidos três arquivos com erro, abaixo detalhamos cada um dos erros:

                No arquivo_de_entrada_incorreto1.lsi na linha 23 é esperado um ';', mas para criar o erro não colocamos.
                    Ele retorna que foi encontrado um 'print' pois é o próximo token no código, fazendo com que não dê match, causando
                    o erro. O código retorna uma lista com os possíveis tokens que deveriam estar no lugar de 'print' para que o código
                    faça parta da linguagem LSI-2025-2.

                No arquivo_de_entrada_incorreto2.lsi na linha 21 é esperado que seja '(', mas ele encontra um '=' na pilha.
                    O analisador sintático lê o id 'verificaValor' e espera que esse id receba uma atribuição '=', porém o que o código
                    escrito está tentando fazer é chamar uma função. Na linguagem LSI-2025-2 a única maneira de chamar funções é
                    determinando uma variável para receber uma função, como por exemplo:
                            result = verificaValor(a);
                
                No arquivo_de_entrada_incorreto3.lsi na linha 7 é esperado um '}', mas ele encontra um 'return' na pilha.
                    Ele retorna 