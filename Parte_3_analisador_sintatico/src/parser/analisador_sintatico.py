# ==== #
# Trabalho de Compiladores - Parte 3: Analisador Sintático Preditivo
# ==== #
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from Parte_1_analisador_lexico.src.lexer.token import Token

class AnalisadorSintatico:
    def __init__(self, tokens):
        self.tokens = tokens
        # Adiciona o marcador de fim de cadeia ($) se não estiver presente
        self.tokens.append(Token("EOF", "$", 0, 0))
        self.posicao = 0
        self.token_atual = self.tokens[self.posicao]
        self.pilha = ['$'] # Pilha inicializada com $
        self.pilha.append('MAIN') # Símbolo inicial
        
        # Tabela de Análise Sintática (M)
        # Mapeia (Não-Terminal, Terminal) -> [Produção]
        # 'ε' é representado por uma lista vazia []
        self.tabela = {
            'MAIN': {
                'id': ['STMT'], 'int': ['STMT'], 'print': ['STMT'], 'return': ['STMT'], 
                'if': ['STMT'], '{': ['STMT'], ';': ['STMT'], 'def': ['FLIST'], '$': [] # ε
            },
            'FLIST': {
                'def': ['FDEF', "FLIST'"]
            },
            "FLIST'": {
                'def': ['FLIST'], '$': [] # ε
            },
            'FDEF': {
                'def': ['def', 'id', '(', 'PARLIST', ')', '{', 'STMTLIST', '}']
            },
            'PARLIST': {
                'int': ['int', 'id', "PARLIST'"], ')': [] # ε
            },
            "PARLIST'": {
                ',': [',', 'PARLIST'], ')': [] # ε
            },
            'VARLIST': {
                'id': ['id', "VARLIST'"]
            },
            "VARLIST'": {
                ',': [',', 'VARLIST'], ';': [] # ε
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
                'id': ['id'], ';': [] # ε
            },
            'IFSTMT': {
                'if': ['if', '(', 'EXPR', ')', '{', 'STMT', '}', "IFSTMT'"]
            },
            "IFSTMT'": {
                'else': ['else', '{', 'STMT', '}'],
                'int': [], 'id': [], 'print': [], 'return': [], 'if': [], '{': [], ';': [], '}': [], '$': [] # ε (FOLLOW)
            },
            'STMTLIST': {
                'int': ['STMT', "STMTLIST'"], 'id': ['STMT', "STMTLIST'"], 
                'print': ['STMT', "STMTLIST'"], 'return': ['STMT', "STMTLIST'"], 
                'if': ['STMT', "STMTLIST'"], '{': ['STMT', "STMTLIST'"], ';': ['STMT', "STMTLIST'"]
            },
            "STMTLIST'": {
                'int': ['STMTLIST'], 'id': ['STMTLIST'], 'print': ['STMTLIST'], 
                'return': ['STMTLIST'], 'if': ['STMTLIST'], '{': ['STMTLIST'], 
                ';': ['STMTLIST'], '}': [] # ε
            },
            'EXPR': {
                'num': ['NUMEXPR', "EXPR'"], '(': ['NUMEXPR', "EXPR'"], 'id': ['NUMEXPR', "EXPR'"]
            },
            "EXPR'": {
                '<': ['OP', 'NUMEXPR'], '>': ['OP', 'NUMEXPR'], '<=': ['OP', 'NUMEXPR'], 
                '>=': ['OP', 'NUMEXPR'], '==': ['OP', 'NUMEXPR'], '!=': ['OP', 'NUMEXPR'],
                ';': [], ')': [] # ε
            },
            'OP': {
                '<': ['<'], '>': ['>'], '<=': ['<='], '>=': ['>='], '==': ['=='], '!=': ['!=']
            },
            'NUMEXPR': {
                'num': ['TERM', "NUMEXPR'"], '(': ['TERM', "NUMEXPR'"], 'id': ['TERM', "NUMEXPR'"]
            },
            "NUMEXPR'": {
                '+': ['+', 'TERM', "NUMEXPR'"], '-': ['-', 'TERM', "NUMEXPR'"],
                '<': [], '>': [], '<=': [], '>=': [], '==': [], '!=': [], ';': [], ')': [] # ε
            },
            'TERM': {
                'num': ['FACTOR', "TERM'"], '(': ['FACTOR', "TERM'"], 'id': ['FACTOR', "TERM'"]
            },
            "TERM'": {
                '*': ['*', 'FACTOR', "TERM'"], '/': ['/', 'FACTOR', "TERM'"],
                '+': [], '-': [], '<': [], '>': [], '<=': [], '>=': [], '==': [], '!=': [], ';': [], ')': [] # ε
            },
            'FACTOR': {
                'num': ['num'], '(': ['(', 'NUMEXPR', ')'], 'id': ['id', "FACTOR'"]
            },
            "FACTOR'": {
                '(': ['(', 'PARLISTCALL', ')'],
                '*': [], '/': [], '+': [], '-': [], '<': [], '>': [], '<=': [], '>=': [], '==': [], '!=': [], ';': [], ')': [] # ε
            },
            'PARLISTCALL': {
                'id': ['id', "PARLISTCALL'"], ')': [] # ε
            },
            "PARLISTCALL'": {
                ',': [',', 'PARLISTCALL'], ')': [] # ε
            }
        }

    def obter_coluna_tabela(self, token):
        """Mapeia o token atual para a coluna correspondente na tabela."""
        if token.tipo == "IDENTIFICADOR":
            return "id"
        elif token.tipo == "NUM":
            return "num"
        elif token.tipo == "PALAVRA_CHAVE":
            return token.valor
        else:
            # Para operadores e pontuação, o valor é o próprio terminal
            return token.valor

    def erro_sintatico(self, esperado, encontrado):
        raise Exception(f"Erro Sintático! Esperado: '{esperado}', Encontrado: '{encontrado}' na linha {self.token_atual.linha}, coluna {self.token_atual.coluna}")

    def analisar(self):
        print(f"{'PILHA':<60} {'ENTRADA':<20} {'AÇÃO'}")
        print("-" * 100)

        while len(self.pilha) > 0:
            topo = self.pilha[-1] # Olha o topo sem desempilhar
            token_coluna = self.obter_coluna_tabela(self.token_atual)
            
            # Visualização do passo a passo (opcional, mas bom para debug e apresentação)
            pilha_str = " ".join(self.pilha)
            print(f"{pilha_str:<60} {self.token_atual.valor:<20}", end="")

            # Caso 1: Topo é terminal ou $
            if topo == token_coluna:
                print(f"Match '{topo}'")
                self.pilha.pop()
                self.posicao += 1
                self.token_atual = self.tokens[self.posicao]
            
            # Caso 2: Topo é terminal mas não casa (Erro)
            elif topo not in self.tabela: 
                # Se topo não é chave da tabela, ele é um terminal. Se não casou acima, é erro.
                self.erro_sintatico(topo, token_coluna)

            # Caso 3: Topo é Não-Terminal (Derivação)
            else:
                linha_tabela = self.tabela[topo]
                
                if token_coluna in linha_tabela:
                    producao = linha_tabela[token_coluna]
                    print(f"Deriva {topo} -> {' '.join(producao) if producao else 'ε'}")
                    self.pilha.pop()
                    
                    # Empilha a produção em ordem inversa (para o primeiro símbolo ficar no topo)
                    if producao: # Se não for ε
                        for simbolo in reversed(producao):
                            self.pilha.append(simbolo)
                else:
                    self.erro_sintatico(f"produção válida para {topo}", token_coluna)

        print("-" * 100)
        print("Análise Sintática Concluída com Sucesso!")