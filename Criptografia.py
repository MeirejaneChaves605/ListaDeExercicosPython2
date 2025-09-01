
class CriptografadorDeFrase:
    """
    Uma classe para criptografar uma frase, substituindo vogais por números.
    """

    def __init__(self, frase):
        """
        Construtor da classe.
        Recebe e armazena a frase a ser criptografada.
        """
        self.frase = frase.upper()  # Convertendo para maiúsculas para facilitar a substituição.
        self.mapa_criptografia = {
            'A': '4',
            'E': '3',
            'I': '1',
            'O': '0',
            'U': '8'
        }

    def criptografar(self):
        """
        Criptografa a frase, substituindo cada vogal pelo seu número correspondente.
        """
        frase_criptografada = ""
        for caractere in self.frase:
            # Verifica se o caractere é uma vogal e está no mapa de criptografia
            if caractere in self.mapa_criptografia:
                # Se for, adiciona o número correspondente à nova frase
                frase_criptografada += self.mapa_criptografia[caractere]
            else:
                # Se não for uma vogal, adiciona o caractere original
                frase_criptografada += caractere
        return frase_criptografada

# --- Execução do Programa ---

# 1. Obtenção da entrada do usuário
frase_original = input("Digite uma frase para criptografar: ")

# 2. Criação de um objeto da classe CriptografadorDeFrase
criptografador = CriptografadorDeFrase(frase_original)

# 3. Execução do método de criptografia
frase_criptografada = criptografador.criptografar()

# 4. Exibição dos resultados
print(f"Frase original: {frase_original}")
print(f"Frase criptografada: {frase_criptografada}")