
class Comodo:
    """
    Representa um cômodo de uma casa.
    Seus atributos são privados e só existem se a Casa existir,
    caracterizando uma relação de composição.
    """
    def __init__(self, nome, area):
        self.__nome = nome
        self.__area = area

    # Getters para permitir o acesso aos atributos, mas não a manipulação direta
    def get_nome(self):
        return self.__nome

    def get_area(self):
        return self.__area

class Casa:
    """
    Representa uma casa que contém vários cômodos.
    A relação de composição é garantida pela forma como os cômodos
    são criados e gerenciados internamente por esta classe.
    """
    def __init__(self):
        # A lista de cômodos só existe dentro da Casa
        self.__comodos = []

    def adicionar_comodo(self, nome, area):
        """
        Cria um novo objeto Comodo e o adiciona à casa.
        A criação do cômodo é gerenciada inteiramente pela Casa.
        """
        novo_comodo = Comodo(nome, area)
        self.__comodos.append(novo_comodo)
        print(f"O cômodo '{nome}' foi adicionado à casa.")

    def calcular_area_total(self):
        """
        Calcula a soma das áreas de todos os cômodos da casa.
        """
        area_total = sum(c.get_area() for c in self.__comodos)
        return area_total

    def listar_comodos(self):
        """
        Exibe a lista de todos os cômodos da casa.
        """
        if not self.__comodos:
            print("A casa não possui cômodos ainda.")
            return

        print("\n--- Cômodos da Casa ---")
        for comodo in self.__comodos:
            print(f"- Nome: {comodo.get_nome()}, Área: {comodo.get_area():.2f} m²")
        print("-----------------------")


# --- Programa Principal e Menu Interativo ---

def menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- Gerenciamento da Casa ---")
    print("1. Criar casa")
    print("2. Adicionar um cômodo")
    print("3. Listar cômodos")
    print("4. Calcular área total")
    print("5. Sair")

def main():
    """Função principal que gerencia o fluxo do programa."""
    casa = None  # A casa é inicializada como None

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            if casa:
                print("Uma casa já foi criada.")
            else:
                casa = Casa()
                print("Casa criada com sucesso!")

        elif opcao == '2':
            if not casa:
                print("Crie uma casa primeiro (Opção 1).")
                continue
            
            nome = input("Digite o nome do cômodo: ")
            try:
                area = float(input("Digite a área em m²: "))
                casa.adicionar_comodo(nome, area)
            except ValueError:
                print("Entrada inválida. A área deve ser um número.")

        elif opcao == '3':
            if not casa:
                print("Crie uma casa primeiro (Opção 1).")
                continue
            casa.listar_comodos()
        
        elif opcao == '4':
            if not casa:
                print("Crie uma casa primeiro (Opção 1).")
                continue
            
            area_total = casa.calcular_area_total()
            print(f"\nA área total da casa é: {area_total:.2f} m²")

        elif opcao == '5':
            print("Encerrando o programa. Até mais!")
            break

        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 5.")

if __name__ == "__main__":
    main()