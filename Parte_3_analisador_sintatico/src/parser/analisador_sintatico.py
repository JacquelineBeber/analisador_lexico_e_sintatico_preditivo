# ======================================================== #
# Trabalho de Compiladores - Parte 3: Analisador Sintático #
#                                                          #
#     Grupo:                                               #
#       - Arthur Lorenzetti da Rosa     19200621           #
#       - Jacqueline Correia Beber      19200634           #
# ======================================================== #

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from Parte_1_analisador_lexico.src.lexer.token import Token

class AnalisadorSintatico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokens.append(Token("FIM_DO_ARQUIVO", "$", 0, 0))
        self.posicao = 0
        self.token_atual = self.tokens[self.posicao]
        self.pilha = ['$']
        self.pilha.insert(0, 'MAIN')
        self.tabela = {
            'MAIN': {
                'int': ['STMT'],
                'id': ['STMT'],
                'print': ['STMT'],
                'return': ['STMT'], 
                'if': ['STMT'],
                '{': ['STMT'],
                ';': ['STMT'],
                'def': ['FLIST'],
                '$': []
            },
            'STMT': {
                'int': ['int', 'VARLIST', ';'],
                'id': ['ATRIBST', ';'],
                'print': ['PRINTST', ';'],
                'return': ['RETURNST', ';'],
                'if': ['IFSTMT'],
                '{': ['{', 'STMTLIST', '}'],
                ';': [';']
            },
            'FLIST': {
                'def': ['FDEF', "FLIST'"]
            },
            "FLIST'": {
                'def': ['FLIST'],
                '$': []
            },
            'FDEF': {
                'def': ['def', 'id', '(', 'PARLIST', ')', '{', 'STMTLIST', '}']
            },
            'PARLIST': {
                'int': ['int', 'id', "PARLIST'"],
                ')': []
            },
            "PARLIST'": {
                ',': [',', 'PARLIST'],
                ')': []
            },
             'STMTLIST': {
                'int': ['STMT', "STMTLIST'"],
                'id': ['STMT', "STMTLIST'"], 
                'print': ['STMT', "STMTLIST'"],
                'return': ['STMT', "STMTLIST'"],
                'if': ['STMT', "STMTLIST'"],
                '{': ['STMT', "STMTLIST'"],
                ';': ['STMT', "STMTLIST'"]
            },
            "STMTLIST'": {
                'int': ['STMTLIST'],
                'id': ['STMTLIST'],
                'print': ['STMTLIST'], 
                'return': ['STMTLIST'],
                'if': ['STMTLIST'], '{': ['STMTLIST'], 
                ';': ['STMTLIST'],
                '}': []
            },
            'VARLIST': {
                'id': ['id', "VARLIST'"]
            },
            "VARLIST'": {
                ';': [],
                ',': [',', 'VARLIST']
            },
            'ATRIBST': {
                'id': ['id', '=', 'EXPR']
            },
            'PRINTST': {
                'print': ['print', 'EXPR']
            },
            'RETURNST': {
                'return': ['return', "RETURNST'"]
            },
            "RETURNST'": {
                'id': ['id'],
                ';': []
            },
            'IFSTMT': {
                'if': ['if', '(', 'EXPR', ')', '{', 'STMT', '}', "IFSTMT'"]
            },
            "IFSTMT'": {
                'int': [],
                'id': [],
                'print': [],
                'return': [],
                'if': [],
                'else': ['else', '{', 'STMT', '}'],
                '{': [],
                '}': [],
                ';': [],
                '$': []
            },
            'EXPR': {
                'id': ['NUMEXPR', "EXPR'"],
                'num': ['NUMEXPR', "EXPR'"],
                '(': ['NUMEXPR', "EXPR'"]
            },
            "EXPR'": {
                ';': [],
                ')': [],
                '<': ['OP', 'NUMEXPR'],
                '>': ['OP', 'NUMEXPR'], 
                '==': ['OP', 'NUMEXPR'],
                '!=': ['OP', 'NUMEXPR'],
                '<=': ['OP', 'NUMEXPR'], 
                '>=': ['OP', 'NUMEXPR'],
            },
             'PARLISTCALL': {
                'id': ['id', "PARLISTCALL'"],
                ')': []
            },
            "PARLISTCALL'": {
                ',': [',', 'PARLISTCALL'],
                ')': []
            },
             'NUMEXPR': {
                'id': ['TERM', "NUMEXPR'"],
                'num': ['TERM', "NUMEXPR'"],
                '(': ['TERM', "NUMEXPR'"]
            },
            "NUMEXPR'": {
                ';': [],
                ')': [],
                '<': [],
                '>': [],
                '==': [],
                '!=': [],
                '<=': [],
                '>=': [],
                '+': ['+', 'TERM', "NUMEXPR'"],
                '-': ['-', 'TERM', "NUMEXPR'"]
            },
            'OP': {
                '<': ['<'],
                '>': ['>'],
                '==': ['=='],
                '!=': ['!='],
                '<=': ['<='],
                '>=': ['>=']
            },
            'TERM': {
                'id': ['FACTOR', "TERM'"],
                'num': ['FACTOR', "TERM'"],
                '(': ['FACTOR', "TERM'"]
            },
            "TERM'": {
                ';': [],
                ')': [],
                '<': [],
                '>': [],
                '==': [],
                '!=': [],
                '<=': [], 
                '>=': [],
                '+': [],
                '-': [],
                '*': ['*', 'FACTOR', "TERM'"],
                '/': ['/', 'FACTOR', "TERM'"]
            },
            'FACTOR': {
                'id': ['id', "FACTOR'"],
                'num': ['num'],
                '(': ['(', 'NUMEXPR', ')']
            },
            "FACTOR'": {
                ';': [],
                '(': ['(', 'PARLISTCALL', ')'],
                ')': [],
                '<': [],
                '>': [],
                '==': [],
                '!=': [],
                '<=': [],
                '>=': [],
                '+': [],
                '-': [],
                '*': [],
                '/': []
            },
        }

    def obter_valor_token(self, token):
        """Mapeia o token atual para a coluna correspondente na tabela."""
        if token.tipo == "IDENTIFICADOR":
            return "id"
        elif token.tipo == "NUM":
            return "num"
        else:
            return token.valor

    def erro_sintatico(self, esperado, encontrado):
        raise Exception(f"Erro Sintático! \n Encontrado: '{encontrado}' \n Esperado: '{esperado}' \n Linha: {self.token_atual.linha} \n Coluna: {self.token_atual.coluna}")

    def analisar_sintaticamente(self):
        print(f"{'PILHA':<90} {'ENTRADA':<25} {'AÇÃO'}")
        print("-" * 150)

        while len(self.pilha) > 0:
            topo = self.pilha[0]
            token = self.obter_valor_token(self.token_atual)

            pilha_str = " ".join(self.pilha)
            print(f"{pilha_str:<90} {self.token_atual.valor:<20}", end="")
            
            # Topo é Terminal ou $
            if topo == token:
                print(f"Match '{topo}'")
                self.pilha.pop(0)
                
                if (len(self.pilha) > 0):
                    self.posicao += 1
                    self.token_atual = self.tokens[self.posicao]                
            
            # Topo é terminal mas não dá match (Erro)
            elif topo not in self.tabela: 
                self.erro_sintatico(topo, token)

            # Topo é Não-Terminal (Derivação)
            else:
                linha_tabela = self.tabela[topo]
                
                if token in linha_tabela:
                    producao = linha_tabela[token]
                    print(f"Deriva {topo} -> {' '.join(producao) if producao else 'ε'}")
                    self.pilha.pop(0)
                    
                    # Empilha a produção em ordem inversa (para o primeiro símbolo ficar no topo)
                    if producao:
                        for simbolo in reversed(producao):
                            self.pilha.insert(0, simbolo)
                else:
                    self.erro_sintatico(self.tabela[topo], token)

        print("-" * 150)
        print("\n Análise Sintática Concluída com Sucesso!")