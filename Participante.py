
# --- Classes do Sistema ---

class Participante:
    """Classe base para todos os participantes da plataforma."""
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def emitirCertificado(self):
        """Retorna uma mensagem genérica de emissão de certificado."""
        return f"O certificado para {self.nome} foi emitido."

class Aluno(Participante):
    """Subclasse para alunos, com atributo de curso."""
    def __init__(self, nome, email, curso):
        super().__init__(nome, email)
        self.curso = curso

    def emitirCertificado(self):
        """Sobrescreve o método para um certificado de conclusão de curso."""
        return f"O certificado de conclusão do curso '{self.curso}' foi emitido para o aluno {self.nome}."

class Instrutor(Participante):
    """Subclasse para instrutores, com atributo de especialidade."""
    def __init__(self, nome, email, especialidade):
        super().__init__(nome, email)
        self.especialidade = especialidade

    def emitirCertificado(self):
        """Sobrescreve o método para um certificado de palestrante."""
        return f"O certificado de participação como palestrante na área de '{self.especialidade}' foi emitido para o instrutor {self.nome}."


# --- Lógica do Programa ---

def cadastrar_participante(participantes):
    """Função para cadastrar um novo aluno ou instrutor."""
    print("\n--- Cadastro de Participante ---")
    tipo = input("Cadastrar (1) Aluno ou (2) Instrutor? ")
    nome = input("Nome: ")
    email = input("Email: ")

    if tipo == '1':
        curso = input("Curso: ")
        participante = Aluno(nome, email, curso)
        participantes.append(participante)
        print("Aluno cadastrado com sucesso!")
    elif tipo == '2':
        especialidade = input("Especialidade: ")
        participante = Instrutor(nome, email, especialidade)
        participantes.append(participante)
        print("Instrutor cadastrado com sucesso!")
    else:
        print("Opção inválida.")

def listar_participantes(participantes):
    """Função para listar todos os participantes cadastrados."""
    if not participantes:
        print("\nNenhum participante cadastrado.")
        return

    print("\n--- Lista de Participantes ---")
    for p in participantes:
        if isinstance(p, Aluno):
            print(f"Aluno: {p.nome} - Email: {p.email} - Curso: {p.curso}")
        elif isinstance(p, Instrutor):
            print(f"Instrutor: {p.nome} - Email: {p.email} - Especialidade: {p.especialidade}")
        else:
            print(f"Participante: {p.nome} - Email: {p.email}")

def emitir_certificados(participantes):
    """Função que emite o certificado para cada participante, demonstrando polimorfismo."""
    if not participantes:
        print("\nNenhum participante para emitir certificado.")
        return

    print("\n--- Emissão de Certificados ---")
    for p in participantes:
        # Polimorfismo: O Python chama o método emitirCertificado()
        # correto com base no tipo de objeto (Aluno ou Instrutor).
        print(p.emitirCertificado())


# --- Menu Principal ---
def menu():
    """Função que exibe o menu e gerencia as opções do usuário."""
    participantes = []
    
    while True:
        print("\n--- Menu Principal ---")
        print("1) Cadastrar participante")
        print("2) Listar participantes")
        print("3) Emitir certificados")
        print("0) Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_participante(participantes)
        elif opcao == '2':
            listar_participantes(participantes)
        elif opcao == '3':
            emitir_certificados(participantes)
        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    menu()