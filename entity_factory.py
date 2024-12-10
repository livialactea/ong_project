from models import Funcionario, Animal, Padrinho

class EntityFactory:
    @staticmethod
    def create_funcionario(id, nome, tipo):
        return Funcionario(id, nome, tipo)

    @staticmethod
    def create_animal(id, nome, especie, status):
        return Animal(id, nome, especie, status)

    @staticmethod
    def create_padrinho(id, nome, animal_id=None):
        return Padrinho(id, nome, animal_id)