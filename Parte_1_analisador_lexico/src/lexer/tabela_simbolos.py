# ======================================================== #
# Trabalho de Compiladores - Parte 1: Analisador Léxico    #
#                                                          #
#     Grupo:                                               #
#       - Arthur Lorenzetti da Rosa     19200621           #
#       - Jacqueline Correia Beber      19200634           #
# ======================================================== #

class TabelaDeSimbolos:

    def __init__(self):
        self.simbolos = {}
        self._inserir_palavra_chave()

    def _inserir_palavra_chave(self):
        palavras_chave = ["def", "int", "if", "else", "print", "return"]

        for palavra in palavras_chave:
            self.simbolos[palavra] = "PALAVRA_CHAVE"
        
    def consultar(self, nome):
        return self.simbolos.get(nome)

    def inserir(self, nome, tipo):
        if nome not in self.simbolos:
            self.simbolos[nome] = tipo
            return True
        
        return False

    def eh_palavra_chave(self, nome):
        tipo = self.consultar(nome)
        
        return tipo == "PALAVRA_CHAVE"
    
    def imprimir_tabela_de_simbolos(self):
        print("\n" + "=" * 60)
        print("TABELA DE SÍMBOLOS")
        print("=" * 60)
        print(f"{'Nome':<20} {'Tipo':<20}")
        print("-" * 60)

        for nome, tipo in self.simbolos.items():
            if tipo == "PALAVRA_CHAVE":
                print(f"{nome:<20} {tipo:<20}")
        
        for nome, tipo in self.simbolos.items():
            if tipo == "IDENTIFICADOR":
                print(f"{nome:<20} {tipo:<20}")

        print("-" * 60)
        print("=" * 60 + "\n")