
from abc import ABC, abstractmethod

# Classe base abstrata
class VeiculoTransporte(ABC):
    """
    Classe abstrata que define a estrutura básica de um veículo de transporte.
    Não pode ser instanciada diretamente.
    """
    def __init__(self, placa, capacidade_passageiros):
        if not placa:
            raise ValueError("A placa do veículo não pode ser vazia.")
        if not isinstance(placa, str):
            raise TypeError("A placa deve ser uma string.")
        if capacidade_passageiros <= 0:
            raise ValueError("A capacidade de passageiros deve ser um número positivo.")
        
        self._placa = placa
        self._capacidade_passageiros = capacidade_passageiros
    
    @abstractmethod
    def calcularCustoOperacional(self):
        """Método abstrato que deve ser implementado pelas subclasses."""
        pass

    def __str__(self):
        return f"Placa: {self._placa} | Capacidade de Passageiros: {self._capacidade_passageiros}"

# Subclasse Ônibus
class Onibus(VeiculoTransporte):
    """
    Representa um ônibus, que utiliza diesel como combustível.
    Herda da classe VeiculoTransporte.
    """
    PRECO_DIESEL = 6.00  # R$ 6,00 por litro

    def __init__(self, placa, capacidade_passageiros, consumo_por_km):
        super().__init__(placa, capacidade_passageiros)
        if consumo_por_km <= 0:
            raise ValueError("O consumo por km deve ser um valor positivo.")
        self._consumo_por_km = consumo_por_km

    def calcularCustoOperacional(self):
        """Implementa o cálculo do custo por km para um ônibus."""
        return self._consumo_por_km * self.PRECO_DIESEL

# Subclasse Metrô
class Metro(VeiculoTransporte):
    """
    Representa um metrô, que utiliza energia elétrica.
    Herda da classe VeiculoTransporte.
    """
    PRECO_ENERGIA = 0.80  # R$ 0,80 por kWh

    def __init__(self, placa, capacidade_passageiros, consumo_energia_por_km):
        super().__init__(placa, capacidade_passageiros)
        if consumo_energia_por_km <= 0:
            raise ValueError("O consumo de energia por km deve ser um valor positivo.")
        self._consumo_energia_por_km = consumo_energia_por_km
    
    def calcularCustoOperacional(self):
        """Implementa o cálculo do custo por km para um metrô."""
        return self._consumo_energia_por_km * self.PRECO_ENERGIA