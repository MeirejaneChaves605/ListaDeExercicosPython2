
class Funcionario:
    """
    Representa um funcionário com nome e salário.
    Funciona de forma independente, permitindo a agregação.
    """
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def __str__(self):
        return f"Nome: {self.nome} | Salário: R${self.salario:,.2f}"

class Departamento:
    """
    Representa um departamento com nome e uma lista de funcionários.
    A relação de agregação permite que funcionários existam
    independentemente do departamento.
    """
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = [] # Vetor (lista) de objetos Funcionario

    def adicionar_funcionario(self, funcionario):
        """Adiciona um objeto Funcionario ao departamento."""
        if isinstance(funcionario, Funcionario):
            self.funcionarios.append(funcionario)
            print(f"'{funcionario.nome}' adicionado ao departamento de '{self.nome}'.")
        else:
            print("Erro: Apenas objetos da classe Funcionario podem ser adicionados.")

    def listar_funcionarios(self):
        """Lista todos os funcionários do departamento."""
        if not self.funcionarios:
            print(f"O departamento de '{self.nome}' não possui funcionários.")
            return

        print(f"\n--- Funcionários do Departamento de '{self.nome}' ---")
        for func in self.funcionarios:
            print(f" - {func}")
        print("-" * 40)
    
    def calcular_media_salarial(self):
        """Calcula e retorna a média salarial do departamento."""
        if not self.funcionarios:
            return 0
        
        total_salarios = sum(func.salario for func in self.funcionarios)
        return total_salarios / len(self.funcionarios)

# --- Programa Principal e Menu Interativo ---

def menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- Gerenciamento de Departamentos e Funcionários ---")
    print("1. Criar novo departamento")
    print("2. Criar novo funcionário")
    print("3. Adicionar funcionário a um departamento")
    print("4. Listar funcionários de um departamento")
    print("5. Calcular média salarial de um departamento")
    print("6. Sair")

def main():
    """Função principal que gerencia o fluxo do programa."""
    departamentos = {}  # Dicionário para armazenar os objetos Departamento
    funcionarios = {}   # Dicionário para armazenar os objetos Funcionario

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome_dep = input("Digite o nome do novo departamento: ")
            if nome_dep in departamentos:
                print("Erro: Departamento já existe.")
            else:
                departamentos[nome_dep] = Departamento(nome_dep)
                print(f"Departamento '{nome_dep}' criado com sucesso!")

        elif opcao == '2':
            nome_func = input("Digite o nome do novo funcionário: ")
            try:
                salario = float(input("Digite o salário: "))
                if nome_func in funcionarios:
                    print("Erro: Funcionário com este nome já existe.")
                else:
                    funcionarios[nome_func] = Funcionario(nome_func, salario)
                    print(f"Funcionário '{nome_func}' criado com sucesso!")
            except ValueError:
                print("Erro: Salário inválido. Por favor, digite um número.")

        elif opcao == '3':
            if not departamentos or not funcionarios:
                print("Crie pelo menos um departamento e um funcionário primeiro.")
                continue
            
            print("\nDepartamentos disponíveis:", list(departamentos.keys()))
            nome_dep = input("Digite o nome do departamento: ")
            
            if nome_dep in departamentos:
                print("Funcionários disponíveis:", list(funcionarios.keys()))
                nome_func = input("Digite o nome do funcionário para adicionar: ")
                
                if nome_func in funcionarios:
                    # Relação de agregação: passa o objeto Funcionario para o Departamento
                    departamentos[nome_dep].adicionar_funcionario(funcionarios[nome_func])
                else:
                    print("Erro: Funcionário não encontrado.")
            else:
                print("Erro: Departamento não encontrado.")

        elif opcao == '4':
            if not departamentos:
                print("Nenhum departamento foi criado ainda.")
                continue

            print("\nDepartamentos disponíveis:", list(departamentos.keys()))
            nome_dep = input("Digite o nome do departamento para listar funcionários: ")
            
            if nome_dep in departamentos:
                departamentos[nome_dep].listar_funcionarios()
            else:
                print("Erro: Departamento não encontrado.")

        elif opcao == '5':
            if not departamentos:
                print("Nenhum departamento foi criado ainda.")
                continue

            print("\nDepartamentos disponíveis:", list(departamentos.keys()))
            nome_dep = input("Digite o nome do departamento para calcular a média salarial: ")
            
            if nome_dep in departamentos:
                media = departamentos[nome_dep].calcular_media_salarial()
                if media > 0:
                    print(f"A média salarial do departamento de '{nome_dep}' é: R${media:,.2f}")
                else:
                    print(f"O departamento de '{nome_dep}' não possui funcionários para calcular a média.")
            else:
                print("Erro: Departamento não encontrado.")

        elif opcao == '6':
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 6.")

if __name__ == "__main__":
    main()