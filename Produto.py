
class Produto:
    """
    Representa um produto com atributos privados para nome, preço e quantidade,
    garantindo o encapsulamento.
    """
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    # Getters: Métodos para acessar os atributos privados
    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__quantidade

    # Setters: Métodos para modificar os atributos privados com validação
    def set_nome(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip():
            self.__nome = novo_nome
        else:
            print("Erro: O nome do produto deve ser uma string válida.")

    def set_preco(self, novo_preco):
        if isinstance(novo_preco, (int, float)) and novo_preco >= 0:
            self.__preco = novo_preco
        else:
            print("Erro: O preço do produto deve ser um número não-negativo.")

    def set_quantidade(self, nova_quantidade):
        if isinstance(nova_quantidade, int) and nova_quantidade >= 0:
            self.__quantidade = nova_quantidade
        else:
            print("Erro: A quantidade do produto deve ser um número inteiro não-negativo.")

    def __str__(self):
        """Método para representação de string do objeto."""
        return f"Produto: {self.get_nome()} | Preço: R${self.get_preco():.2f} | Quantidade: {self.get_quantidade()}"

class CarrinhoDeCompras:
    """
    Gerencia uma lista de objetos Produto, permitindo adicionar, remover,
    calcular o total e listar os produtos.
    """
    def __init__(self):
        self.__produtos = []  # Lista privada para armazenar os objetos Produto

    def adicionar_produto(self, produto):
        """Adiciona um produto à lista do carrinho."""
        if isinstance(produto, Produto):
            self.__produtos.append(produto)
            print(f"'{produto.get_nome()}' foi adicionado ao carrinho.")
        else:
            print("Erro: Apenas objetos da classe Produto podem ser adicionados.")

    def remover_produto(self, nome_produto):
        """Remove um produto do carrinho pelo seu nome."""
        produto_encontrado = None
        for produto in self.__produtos:
            if produto.get_nome().lower() == nome_produto.lower():
                produto_encontrado = produto
                break
        
        if produto_encontrado:
            self.__produtos.remove(produto_encontrado)
            print(f"'{produto_encontrado.get_nome()}' foi removido do carrinho.")
        else:
            print(f"Erro: O produto '{nome_produto}' não foi encontrado no carrinho.")

    def calcular_total(self):
        """Calcula e retorna o valor total de todos os produtos no carrinho."""
        total = sum(p.get_preco() * p.get_quantidade() for p in self.__produtos)
        return total

    def listar_produtos(self):
        """Imprime a lista de todos os produtos no carrinho."""
        if not self.__produtos:
            print("O carrinho de compras está vazio.")
        else:
            print("\n--- Conteúdo do Carrinho ---")
            for produto in self.__produtos:
                print(produto)
            print("---------------------------")

# --- Programa Principal ---
def menu():
    """Exibe o menu de opções para o usuário."""
    print("\n--- Menu do Carrinho de Compras ---")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Visualizar carrinho")
    print("4. Calcular total da compra")
    print("5. Sair")
    return input("Escolha uma opção: ")

def main():
    """Função principal que gerencia a interação do usuário."""
    carrinho = CarrinhoDeCompras()
    
    while True:
        opcao = menu()
        
        if opcao == '1':
            nome = input("Digite o nome do produto: ")
            try:
                preco = float(input("Digite o preço do produto: R$"))
                quantidade = int(input("Digite a quantidade: "))
                produto = Produto(nome, preco, quantidade)
                carrinho.adicionar_produto(produto)
            except ValueError:
                print("Entrada inválida. Certifique-se de digitar números para preço e quantidade.")
                
        elif opcao == '2':
            nome = input("Digite o nome do produto a ser removido: ")
            carrinho.remover_produto(nome)
            
        elif opcao == '3':
            carrinho.listar_produtos()
            
        elif opcao == '4':
            total = carrinho.calcular_total()
            print(f"\nO valor total da compra é: R${total:.2f}")
            
        elif opcao == '5':
            print("Saindo do programa. Obrigado!")
            break
            
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 5.")

if __name__ == "__main__":
    main()