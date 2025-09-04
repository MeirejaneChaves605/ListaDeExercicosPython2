# --- Classes do Sistema ---

class Personagem:
    """Classe base para todos os personagens."""
    def __init__(self, nome, constelacao):
        self.nome = nome
        self.constelacao = constelacao

    def apresentar(self):
        """Método de apresentação genérica."""
        print(f"Eu sou {self.nome}, o Cavaleiro de {self.constelacao}.")

class CavaleiroDeBronze:
    """Classe auxiliar para representar um Cavaleiro de Bronze."""
    def __init__(self, poder_de_luta):
        self.poder_de_luta = poder_de_luta

    def golpe_especial(self):
        """Executa o golpe especial de um Cavaleiro de Bronze."""
        print(f"O Cavaleiro de Bronze dispara seu golpe especial! (Poder: {self.poder_de_luta})")

class CavaleiroDeOuro:
    """Classe auxiliar para representar um Cavaleiro de Ouro."""
    def __init__(self, casa_do_zodiaco):
        self.casa_do_zodiaco = casa_do_zodiaco

    def defender_casa(self):
        """Defende a casa do zodíaco."""
        print(f"O Cavaleiro de Ouro defende a Casa de {self.casa_do_zodiaco}!")


class CavaleiroHibrido(CavaleiroDeBronze, CavaleiroDeOuro, Personagem):
    """
    Classe que herda de CavaleiroDeBronze, CavaleiroDeOuro e Personagem.
    Combina as habilidades de um cavaleiro de bronze e de ouro.
    """
    def __init__(self, nome, constelacao, poder_de_luta, casa_do_zodiaco):
        Personagem.__init__(self, nome, constelacao)
        CavaleiroDeBronze.__init__(self, poder_de_luta)
        CavaleiroDeOuro.__init__(self, casa_do_zodiaco)
        
    def apresentar_hibrido(self):
        print(f"Eu sou {self.nome}, um Cavaleiro Híbrido! Eu combino o poder de {self.constelacao} com a força da Casa de {self.casa_do_zodiaco}.")


# --- Funções do Menu Interativo ---

def cadastrar_personagem(cavaleiros):
    """Permite ao usuário cadastrar um novo cavaleiro."""
    print("\n--- Cadastro de Cavaleiro ---")
    nome = input("Nome do cavaleiro: ")
    tipo = input("Tipo (1) Bronze ou (2) Ouro? ")

    if tipo == '1':
        constelacao = input("Constelação: ")
        poder_de_luta = input("Poder de luta: ")
        try:
            cavaleiro = CavaleiroHibrido(nome, constelacao, poder_de_luta, "N/A")
            print("Cavaleiro de Bronze cadastrado!")
        except Exception as e:
            print(f"Erro ao cadastrar: {e}")
    elif tipo == '2':
        constelacao = input("Constelação: ")
        casa = input("Casa do Zodíaco: ")
        try:
            cavaleiro = CavaleiroHibrido(nome, constelacao, "N/A", casa)
            print("Cavaleiro de Ouro cadastrado!")
        except Exception as e:
            print(f"Erro ao cadastrar: {e}")
    else:
        print("Opção inválida.")
        return

    cavaleiros.append(cavaleiro)

def listar_personagens(cavaleiros):
    """Lista todos os cavaleiros cadastrados."""
    if not cavaleiros:
        print("\nNenhum cavaleiro cadastrado.")
        return
    
    print("\n--- Lista de Cavaleiros ---")
    for cav in cavaleiros:
        cav.apresentar()
        if hasattr(cav, 'poder_de_luta') and cav.poder_de_luta != "N/A":
            print(f"  Poder de Luta: {cav.poder_de_luta}")
        if hasattr(cav, 'casa_do_zodiaco') and cav.casa_do_zodiaco != "N/A":
            print(f"  Casa: {cav.casa_do_zodiaco}")

def executar_acoes(cavaleiros):
    """Permite executar ações específicas para cada tipo de cavaleiro."""
    if not cavaleiros:
        print("\nNenhum cavaleiro para executar ações.")
        return
        
    print("\n--- Executando Ações dos Cavaleiros ---")
    for cav in cavaleiros:
        print("-" * 20)
        cav.apresentar()
        
        # Polimorfismo: o tipo do objeto determina qual método é chamado.
        if isinstance(cav, CavaleiroDeBronze) and cav.poder_de_luta != "N/A":
            cav.golpe_especial()
        
        if isinstance(cav, CavaleiroDeOuro) and cav.casa_do_zodiaco != "N/A":
            cav.defender_casa()

# --- Menu Principal ---

def main():
    cavaleiros_cadastrados = []
    
    while True:
        print("\n--- Menu Principal ---")
        print("1) Cadastrar Cavaleiro")
        print("2) Listar Cavaleiros")
        print("3) Executar Golpes/Defesas")
        print("0) Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_personagem(cavaleiros_cadastrados)
        elif escolha == '2':
            listar_personagens(cavaleiros_cadastrados)
        elif escolha == '3':
            executar_acoes(cavaleiros_cadastrados)
        elif escolha == '0':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
