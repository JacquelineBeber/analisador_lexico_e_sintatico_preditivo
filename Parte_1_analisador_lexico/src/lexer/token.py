# ======================================================== #
# Trabalho de Compiladores - Parte 1: Analisador Léxico    #
#                                                          #
#     Grupo:                                               #
#       - Arthur Lorenzetti da Rosa     19200621           #
#       - Jacqueline Correia Beber      19200634           #
# ======================================================== #


class Token:

    def __init__(self, tipo, valor, linha, coluna):
        self.tipo = tipo
        self.valor = valor
        self.linha = linha
        self.coluna = coluna

    def __repr__(self):
        if self.tipo == "IDENTIFICADOR":
            return "id"
        elif self.tipo == "NUM":
            return "num"
        else:
            return self.valor
    
    def token_detalhado(self):
        return f"<< {self.tipo} -- '{self.valor}', linha: {self.linha}, coluna: {self.coluna} >>"