
class ProgressaoAritmetica:
    """
    Uma classe para calcular e exibir os termos e a soma de uma Progressão Aritmética.
    """

    def __init__(self, n, a1, r):
        """
        Construtor da classe.
        Recebe e armazena o número de termos (n), o primeiro termo (a1) e a razão (r).
        """
        self.n = n
        self.a1 = a1
        self.r = r
        self.termos = []
        self.soma = 0

    def calcular_termos(self):
        """
        Calcula e armazena todos os termos da progressão.
        """
        self.termos.append(self.a1)  # Adiciona o primeiro termo à lista
        termo_atual = self.a1
        for _ in range(1, self.n):
            termo_atual += self.r
            self.termos.append(termo_atual)
        return self.termos

    def calcular_soma(self):
        """
        Calcula a soma de todos os termos da progressão usando a fórmula.
        """
        # an = a1 + r * (n - 1)
        an = self.a1 + self.r * (self.n - 1)
        # S = n * (a1 + an) / 2
        self.soma = self.n * (self.a1 + an) / 2
        return self.soma

    def exibir_resultados(self):
        """
        Exibe todos os resultados calculados: termos e soma.
        """
        print(f"Os termos da P.A. são: {self.termos}")
        print(f"A soma dos termos é: {self.soma}")

# --- Execução do Programa ---

# 1. Obtenção das entradas do usuário
try:
    n = int(input("Digite o número de termos (n): "))
    a1 = float(input("Digite o primeiro termo (a1): "))
    r = float(input("Digite a razão (r): "))

    # 2. Criação de um objeto da classe ProgressaoAritmetica
    pa = ProgressaoAritmetica(n, a1, r)

    # 3. Execução dos métodos para calcular e exibir os resultados
    pa.calcular_termos()
    pa.calcular_soma()
    pa.exibir_resultados()

except ValueError:
    print("Entrada inválida. Por favor, digite números.")