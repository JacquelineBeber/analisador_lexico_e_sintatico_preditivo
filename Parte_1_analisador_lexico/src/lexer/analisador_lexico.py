# ======================================================== #
# Trabalho de Compiladores - Parte 1: Analisador Léxico    #
#                                                          #
#     Grupo:                                               #
#       - Arthur Lorenzetti da Rosa     19200621           #
#       - Jacqueline Correia Beber      19200634           #
# ======================================================== #

from .tabela_simbolos import TabelaDeSimbolos
from .token import Token

class AnalisadorLexico:

    def __init__(self, codigo_fonte):
        self.codigo_fonte = codigo_fonte
        self.tamanho = len(codigo_fonte)
        self.posicao = 0
        self.linha_atual = 1
        self.coluna_atual = 1
        self.tabela_de_simbolos = TabelaDeSimbolos()
        self.tokens_encontrados = []
        self.erro = False
        self.mensagem_de_erro = ""
    
    def caracter_atual(self):
        if self.posicao < self.tamanho:
            return self.codigo_fonte[self.posicao]

        return None
    
    def proximo_caracter(self):
        proxima_posicao = self.posicao + 1

        if proxima_posicao + 1 < self.tamanho:
            return self.codigo_fonte[proxima_posicao]

        return None
    
    def avancar(self):
        if self.posicao >= self.tamanho:
            return None
        
        caracter = self.codigo_fonte[self.posicao]
        self.posicao += 1

        if caracter == '\n':
            self.linha_atual += 1
            self.coluna_atual = 1
        else:
            self.coluna_atual += 1
        
        return caracter
    
    def ignorar_espaco_em_branco(self):
        while self.caracter_atual() in [' ', '\t', '\n', '\r']:
            self.avancar()
    
    def reconhecer_numero(self):
        linha_inicial = self.linha_atual
        coluna_incial = self.coluna_atual
        
        lexema = ""

        while self.caracter_atual() and self.caracter_atual().isdigit():
            lexema += self.caracter_atual()
            self.avancar()
        
        valor_numerico = int(lexema)

        return Token("NUM", valor_numerico, linha_inicial, coluna_incial)
    
    def reconhecer_identificador_e_palavra_chave(self):
        linha_inicial = self.linha_atual
        coluna_incial = self.coluna_atual
        
        lexema = ""
        lexema += self.caracter_atual()
        
        self.avancar()

        while self.caracter_atual() and (self.caracter_atual().isalnum() or self.caracter_atual() == "_"):
            lexema += self.caracter_atual()
            self.avancar()
        
        if self.tabela_de_simbolos.eh_palavra_chave(lexema):
            return Token("PALAVRA_CHAVE", lexema, linha_inicial, coluna_incial)
        else:
            self.tabela_de_simbolos.inserir(lexema, "IDENTIFICADOR")
            return Token("IDENTIFICADOR", lexema, linha_inicial, coluna_incial)
    
    def reconhecer_operador_e_pontuacao(self):
        linha_inicial = self.linha_atual
        coluna_incial = self.coluna_atual

        caracter = self.caracter_atual()
        self.avancar()

        if caracter == '=':
            if self.caracter_atual() == '=':
                self.avancar()
                return Token("OPERACAO_IGUAL_A", "==", linha_inicial, coluna_incial)
            
            else:
                return Token("OPERACAO_DE_ATRIBUICAO", "=", linha_inicial, coluna_incial)
            
        elif caracter == '!':
            if self.caracter_atual() == '=':
                self.avancar()
                return Token("OPERACAO_DIFERENTE_DE", "!=", linha_inicial, coluna_incial)
            
            else:
                self.erro = True
                self.mensagem_de_erro = f"Erro Léxico encontrado! \n Linha: {linha_inicial} \n Coluna: {coluna_incial} \n Caractere inválido: '!'"
                raise Exception(self.mensagem_de_erro)
            
        elif caracter == '<':
            if self.caracter_atual() == '=':
                self.avancar()
                return Token("OPERACAO_MENOR_IGUAL_QUE", "<=", linha_inicial, coluna_incial)
            
            else:
                return Token("OPERACAO_MENOR_QUE", "<", linha_inicial, coluna_incial)
            
        elif caracter == '>':
            if self.caracter_atual() == '=':
                self.avancar()
                return Token("OPERACAO_MAIOR_IGUAL_QUE", ">=", linha_inicial, coluna_incial)
            
            else:
                return Token("OPERACAO_MAIOR_QUE", ">", linha_inicial, coluna_incial)

        elif caracter == '+':
            return Token("OPERACAO_MAIS", "+", linha_inicial, coluna_incial)
        
        elif caracter == '-':
            return Token("OPERACAO_MENOS", "-", linha_inicial, coluna_incial)
        
        elif caracter == '*':
            return Token("OPERACAO_MULTIPLICACAO", "*", linha_inicial, coluna_incial)
        
        elif caracter == '/':
            return Token("OPERACAO_DIVISAO", "/", linha_inicial, coluna_incial)
        
        elif caracter == '(':
            return Token("ABRE_PARENTESES", "(", linha_inicial, coluna_incial)

        elif caracter == ')':
            return Token("FECHA_PARENTESES", ")", linha_inicial, coluna_incial)

        elif caracter == '{':
            return Token("ABRE_CHAVES", "{", linha_inicial, coluna_incial)
        
        elif caracter == '}':
            return Token("FECHA_CHAVES", "}", linha_inicial, coluna_incial)
        
        elif caracter == ',':
            return Token("VIRGULA", ",", linha_inicial, coluna_incial)
        
        elif caracter == ';':
            return Token("PONTO_VIRGULA", ";", linha_inicial, coluna_incial)
        
        else:
            self.erro = True
            self.mensagem_de_erro = f"Erro Léxico encontrado! \n Linha: {linha_inicial} \n Coluna: {coluna_incial} \n Caractere inválido: '{caracter}'"
            raise Exception(self.mensagem_de_erro)

    def analisar_codigo_fonte(self):
        while self.posicao < self.tamanho:
            self.ignorar_espaco_em_branco()

            caracter = self.caracter_atual()

            if caracter is None:
                break

            if caracter.isdigit():
                token = self.reconhecer_numero()
                self.tokens_encontrados.append(token)
            
            elif caracter.isalpha() or caracter == '_':
                token = self.reconhecer_identificador_e_palavra_chave()
                self.tokens_encontrados.append(token)
            
            elif caracter in '=!<>+-*/(){},;':
                token = self.reconhecer_operador_e_pontuacao()
                self.tokens_encontrados.append(token)
            
            else:
                self.erro = True
                self.mensagem_de_erro = f"Erro Léxico encontrado! \n Linha: {self.linha_atual} \n Coluna: {self.coluna_atual} \n Caractere inválido: '{caracter}'"
                raise Exception(self.mensagem_de_erro)
        
        return self.tokens_encontrados

    def imprimir_tokens(self):
        print("\n" + "=" * 60)
        print("TOKENS")
        print("=" * 60)

        print(self.tokens_encontrados)

        print("=" * 60 + "\n")
        
        # print("\n" + "=" * 60)
        # print("TOKENS DETALHADOS")
        # print("=" * 60)

        # for i, token in enumerate(self.tokens_encontrados, 1):
        #     print(f"{i:3d}, {token.token_detalhado()}")