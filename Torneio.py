
from abc import ABC, abstractmethod

# Classe Abstrata Total
class Lutador(ABC):
    """
    Classe abstrata que define a estrutura de um lutador.
    Todos os métodos são abstratos, forçando as subclasses a implementá-los.
    """
    def __init__(self, nome, nivel_poder):
        if not nome:
            raise ValueError("O nome do lutador não pode ser vazio.")
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser uma string.")
        if not isinstance(nivel_poder, (int, float)) or nivel_poder <= 0:
            raise ValueError("O nível de poder deve ser um valor numérico positivo.")
        
        self._nome = nome
        self._nivel_poder = nivel_poder

    @abstractmethod
    def get_nome(self):
        """Retorna o nome do lutador."""
        pass

    @abstractmethod
    def get_nivel_poder(self):
        """Retorna o nível de poder do lutador."""
        pass

    @abstractmethod
    def atacar(self):
        """Método abstrato para o ataque do lutador."""
        pass

    def __str__(self):
        return f"{self.get_nome()} (Nível de Poder: {self.get_nivel_poder()})"

# Subclasse Saiyajin
class Saiyajin(Lutador):
    def __init__(self, nome, nivel_poder):
        super().__init__(nome, nivel_poder)
    
    def get_nome(self):
        return self._nome

    def get_nivel_poder(self):
        return self._nivel_poder

    def atacar(self):
        return f"O Saiyajin {self._nome} libera sua fúria e ataca com um Kamehameha!"

# Subclasse Androide
class Androide(Lutador):
    def __init__(self, nome, nivel_poder):
        super().__init__(nome, nivel_poder)
        
    def get_nome(self):
        return self._nome

    def get_nivel_poder(self):
        return self._nivel_poder

    def atacar(self):
        return f"O Androide {self._nome} dispara um canhão de energia com precisão cirúrgica!"

# Subclasse Namekuseijin
class Namekuseijin(Lutador):
    def __init__(self, nome, nivel_poder):
        super().__init__(nome, nivel_poder)
        
    def get_nome(self):
        return self._nome

    def get_nivel_poder(self):
        return self._nivel_poder

    def atacar(self):
        return f"O Namekuseijin {self._nome} se regenera e desfere um golpe estratégico!"


# Lista para armazenar os lutadores
inscritos = []

# --- Menu Interativo ---

def cadastrar_lutador():
    """Função para cadastrar um novo lutador."""
    print("\n--- Cadastro de Lutador ---")
    tipo = input("Selecione o tipo de lutador (1. Saiyajin / 2. Androide / 3. Namekuseijin): ")
    try:
        nome = input("Digite o nome do lutador: ")
        nivel_poder = float(input("Digite o nível de poder: "))

        if tipo == '1':
            lutador = Saiyajin(nome, nivel_poder)
            inscritos.append(lutador)
            print(f"Saiyajin '{nome}' inscrito no torneio!")
        elif tipo == '2':
            lutador = Androide(nome, nivel_poder)
            inscritos.append(lutador)
            print(f"Androide '{nome}' inscrito no torneio!")
        elif tipo == '3':
            lutador = Namekuseijin(nome, nivel_poder)
            inscritos.append(lutador)
            print(f"Namekuseijin '{nome}' inscrito no torneio!")
        else:
            print("Opção de lutador inválida.")
    except (ValueError, TypeError) as e:
        print(f"Erro: {e}. O cadastro falhou.")

def listar_lutadores():
    """Função para listar todos os lutadores inscritos."""
    if not inscritos:
        print("\nNenhum lutador inscrito no torneio.")
        return
    
    print("\n--- Lutadores Inscritos ---")
    for lutador in inscritos:
        print(lutador)
    print("-" * 30)

def simular_ataques():
    """Função para simular os ataques de cada lutador."""
    if not inscritos:
        print("\nNenhum lutador para simular ataques.")
        return
    
    print("\n--- Simulação de Ataques ---")
    for lutador in inscritos:
        # Polimorfismo em ação: a mesma chamada de método
        # executa o ataque específico para cada tipo de lutador.
        print(lutador.atacar())
    print("-" * 30)

def main():
    """Função principal que gerencia o menu."""
    while True:
        print("\n--- Torneio de Artes Marciais ---")
        print("1. Cadastrar novo lutador")
        print("2. Listar lutadores")
        print("3. Simular ataques")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_lutador()
        elif opcao == '2':
            listar_lutadores()
        elif opcao == '3':
            simular_ataques()
        elif opcao == '0':
            print("Torneio encerrado. Até a próxima!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()