from abc import ABC, abstractmethod

# Preços fictícios para o cálculo
PRECO_DIESEL = 6.00  # R$ por litro
PRECO_ENERGIA = 0.80  # R$ por kWh

class VeiculoTransporte(ABC):
    """
    Classe base abstrata para veículos de transporte.
    Define a estrutura e o método abstrato para calcular o custo.
    """
    def __init__(self, placa, capacidade_passageiros):
        if not placa:
            raise ValueError("A placa do veículo não pode ser vazia.")
        if not isinstance(capacidade_passageiros, (int, float)) or capacidade_passageiros <= 0:
            raise ValueError("A capacidade de passageiros deve ser um número positivo.")
        
        self.placa = placa
        self.capacidade_passageiros = capacidade_passageiros

    @abstractmethod
    def calcularCustoOperacional(self):
        """Método abstrato para calcular o custo operacional por quilômetro."""
        pass

class Onibus(VeiculoTransporte):
    """
    Subclasse para ônibus, calcula o custo com base no consumo de diesel.
    """
    def __init__(self, placa, capacidade_passageiros, consumo_por_km):
        if not isinstance(consumo_por_km, (int, float)) or consumo_por_km <= 0:
            raise ValueError("O consumo por km do ônibus deve ser um número positivo.")
        
        super().__init__(placa, capacidade_passageiros)
        self.consumo_por_km = consumo_por_km

    def calcularCustoOperacional(self):
        """Implementa o cálculo do custo para um ônibus."""
        return self.consumo_por_km * PRECO_DIESEL

class Metro(VeiculoTransporte):
    """
    Subclasse para metrô, calcula o custo com base no consumo de energia.
    """
    def __init__(self, placa, capacidade_passageiros, consumo_energia_por_km):
        if not isinstance(consumo_energia_por_km, (int, float)) or consumo_energia_por_km <= 0:
            raise ValueError("O consumo de energia por km do metrô deve ser um número positivo.")
        
        super().__init__(placa, capacidade_passageiros)
        self.consumo_energia_por_km = consumo_energia_por_km

    def calcularCustoOperacional(self):
        """Implementa o cálculo do custo para um metrô."""
        return self.consumo_energia_por_km * PRECO_ENERGIA

# --- Função Principal e Demonstração ---

def main():
    """Função principal para demonstrar a criação de veículos e o cálculo de custos."""
    veiculos = []

    # Exemplo de criação de objetos com tratamento de exceções
    try:
        onibus_a = Onibus("ABC-1234", 50, 0.4)
        metro_a = Metro("MET-5678", 300, 15)
        veiculos.append(onibus_a)
        veiculos.append(metro_a)

        # Exemplo de entrada inválida para demonstração
        # onibus_invalido = Onibus("", 60, 0.5)  # Levanta ValueError
        # metro_invalido = Metro("MET-9999", 200, -10) # Levanta ValueError
    except ValueError as e:
        print(f"Erro ao criar veículo: {e}")

    print("\n--- Relatório de Custos Operacionais por Quilômetro ---")
    
    for veiculo in veiculos:
        try:
            # Polimorfismo: o mesmo método é chamado, mas a
            # implementação é específica para cada classe.
            custo = veiculo.calcularCustoOperacional()
            
            # Exibe os dados do veículo
            if isinstance(veiculo, Onibus):
                print(f"Ônibus (Placa: {veiculo.placa}): R$ {custo:.2f}/km")
            elif isinstance(veiculo, Metro):
                print(f"Metrô (Placa: {veiculo.placa}): R$ {custo:.2f}/km")
        except Exception as e:
            print(f"Erro ao calcular custo para o veículo {veiculo.placa}: {e}")

if __name__ == "__main__":
    main()
