
class Documento:
    """
    Representa um documento com título e conteúdo.
    """
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

class Impressora:
    """
    Representa uma impressora que pode imprimir documentos.
    Possui uma relação de dependência com a classe Documento,
    pois o método imprimir(Documento d) utiliza um documento
    apenas para a sua execução, sem armazenar uma referência a ele.
    """
    def imprimir(self, documento):
        """
        Imprime as informações de um objeto Documento.
        """
        print("\n--- INICIANDO IMPRESSÃO ---")
        print(f"Título: {documento.titulo}")
        print("-" * 20)
        print(f"Conteúdo:\n{documento.conteudo}")
        print("--- FIM DA IMPRESSÃO ---\n")

def menu_interativo():
    """
    Função principal que gerencia o menu e a interação do usuário.
    """
    impressora = Impressora()
    documentos_criados = []

    while True:
        print("\n--- Menu Principal ---")
        print("1. Criar novo documento")
        print("2. Imprimir documento existente")
        print("3. Visualizar lista de documentos")
        print("4. Sair")
        
        escolha = input("Digite sua opção: ")

        if escolha == '1':
            print("\n--- Criar Documento ---")
            titulo = input("Digite o título do documento: ")
            conteudo = input("Digite o conteúdo do documento (pode ser multilinha, use Enter para terminar): \n")
            
            # Criação do objeto Documento
            novo_documento = Documento(titulo, conteudo)
            documentos_criados.append(novo_documento)
            print("Documento criado com sucesso!")

        elif escolha == '2':
            print("\n--- Imprimir Documento ---")
            if not documentos_criados:
                print("Nenhum documento foi criado ainda.")
                continue

            print("Documentos disponíveis:")
            for i, doc in enumerate(documentos_criados):
                print(f"{i+1}. {doc.titulo}")
            
            try:
                indice = int(input("Digite o número do documento que deseja imprimir: ")) - 1
                if 0 <= indice < len(documentos_criados):
                    # Relacionamento de dependência: a Impressora utiliza o Documento
                    # apenas no momento da chamada do método.
                    impressora.imprimir(documentos_criados[indice])
                else:
                    print("Número de documento inválido.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        elif escolha == '3':
            print("\n--- Lista de Documentos ---")
            if not documentos_criados:
                print("Nenhum documento foi criado ainda.")
            else:
                for i, doc in enumerate(documentos_criados):
                    print(f"{i+1}. Título: {doc.titulo}")
        
        elif escolha == '4':
            print("Encerrando o programa. Até logo!")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")

# Executa o programa principal
if __name__ == "__main__":
    menu_interativo()