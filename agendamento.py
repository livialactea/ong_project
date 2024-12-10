from abc import ABC, abstractmethod

class ServicoStrategy(ABC):
    @abstractmethod
    def executar_servico(self, animal):
        pass

class VacinaçãoServico(ServicoStrategy):
    def executar_servico(self, animal):
        print(f"Vacinação realizada em {animal.nome}")

class CastracaoServico(ServicoStrategy):
    def executar_servico(self, animal):
        print(f"Castracão realizada em {animal.nome}")

class Agendamento:
    def __init__(self, animal, servico: ServicoStrategy):
        self.animal = animal
        self.servico = servico

    def agendar(self):
        print(f"Agendamento para o animal {self.animal.nome}:")
        self.servico.executar_servico(self.animal)