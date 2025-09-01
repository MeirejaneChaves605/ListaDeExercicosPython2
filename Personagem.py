
# Classe base (superclasse)
class Participante:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    def emitirCertificado(self):
        """Método genérico para emitir um certificado."""
        return f"O certificado de {self.nome} foi emitido."

# Subclasse Aluno, herda de Participante
class Aluno(Participante):
    def __init__(self, nome, email, curso):
        # Chama o construtor da classe base
        super().__init__(nome, email)
        self.curso = curso
    
    def emitirCertificado(self):
        """Sobrescreve o método da classe base para um comportamento específico."""
        return f"O aluno {self.nome} recebeu um certificado de conclusão do curso de {self.curso}."

# Subclasse Instrutor, herda de Participante
class Instrutor(Participante):
    def __init__(self, nome, email, especialidade):
        # Chama o construtor da classe base
        super().__init__(nome, email)
        self.especialidade = especialidade
    
    def emitirCertificado(self):
        """Sobrescreve o método da classe base para um comportamento específico."""
        return f"O instrutor {self.nome} recebeu um certificado de participação como palestrante em {self.especialidade}."