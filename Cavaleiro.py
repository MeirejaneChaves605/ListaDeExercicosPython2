
class Personagem:
    """Classe base para qualquer personagem, com atributos comuns."""
    def __init__(self, nome, constelacao):
        self.nome = nome
        self.constelacao = constelacao

    def apresentar(self):
        """Método genérico para a apresentação do personagem."""
        return f"Meu nome é {self.nome} e minha constelação é {self.constelacao}."

class CavaleiroDeBronze:
    """Classe auxiliar que define os atributos e comportamentos de um Cavaleiro de Bronze."""
    def __init__(self, poder_de_luta):
        self.poder_de_luta = poder_de_luta
    
    def golpe_especial(self):
        """Método que representa um golpe especial."""
        return f"Executando meu golpe especial com um poder de luta de {self.poder_de_luta}!"

class CavaleiroDeOuro:
    """Classe auxiliar que define os atributos e comportamentos de um Cavaleiro de Ouro."""
    def __init__(self, casa_do_zodiaco):
        self.casa_do_zodiaco = casa_do_zodiaco
    
    def defender_casa(self):
        """Método que representa a defesa da casa do zodíaco."""
        return f"Defendendo a casa de {self.casa_do_zodiaco} com todo o meu cosmo!"

class CavaleiroHibrido(CavaleiroDeBronze, CavaleiroDeOuro, Personagem):
    """
    Esta classe herda de CavaleiroDeBronze e CavaleiroDeOuro,
    além da classe base Personagem, combinando todos os seus atributos e métodos.
    """
    def __init__(self, nome, constelacao, poder_de_luta, casa_do_zodiaco):
        # Chamada aos construtores das classes-mãe.
        Personagem.__init__(self, nome, constelacao)
        CavaleiroDeBronze.__init__(self, poder_de_luta)
        CavaleiroDeOuro.__init__(self, casa_do_zodiaco)
    
    def apresentar(self):
        """Sobrescrevendo o método para incluir mais detalhes."""
        return f"Eu sou {self.nome}, o Cavaleiro Híbrido da constelação de {self.constelacao}, da casa de {self.casa_do_zodiaco}."