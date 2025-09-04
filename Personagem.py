# Classe base Personagem
class Personagem:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

    def atacar(self):
        """Método de ataque genérico."""
        print(f"{self.nome} ataca o inimigo!")

# Subclasse Guerreiro
class Guerreiro(Personagem):
    def __init__(self, nome, nivel, forca):
        super().__init__(nome, nivel)
        self.forca = forca

    def atacar(self):
        """Sobrescreve o método de ataque para um ataque físico."""
        print(f"O guerreiro {self.nome} ataca com a sua espada! (Dano Físico: {self.forca})")

# Subclasse Mago
class Mago(Personagem):
    def __init__(self, nome, nivel, mana):
        super().__init__(nome, nivel)
        self.mana = mana

    def atacar(self):
        """Sobrescreve o método de ataque para um ataque mágico."""
        print(f"O mago {self.nome} conjura uma poderosa magia! (Dano Mágico: {self.mana})")

# --- Demonstração do uso ---
if __name__ == "__main__":
    # Cria instâncias das classes
    heroi = Personagem("Herói Genérico", 5)
    gandalf = Mago("Gandalf", 20, 150)
    conan = Guerreiro("Conan", 15, 95)

    # Invoca o método atacar() para cada personagem
    print("--- Chamando o método atacar() ---")
    heroi.atacar()
    gandalf.atacar()
    conan.atacar()

    # Demonstração de polimorfismo em tempo de execução
    print("\n--- Demonstração de polimorfismo ---")
    personagens = [heroi, gandalf, conan]

    for p in personagens:
        p.atacar()
