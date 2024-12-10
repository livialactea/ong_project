from database import Database  # Adicionando a importação da classe Database

class Funcionario:
    def __init__(self, id, nome, tipo):
        self.id = id
        self.nome = nome
        self.tipo = tipo

    def salvar(self):
        conn = Database.get_instance()
        c = conn.cursor()
        c.execute('INSERT INTO Funcionarios (nome, tipo) VALUES (?, ?)', (self.nome, self.tipo))
        conn.commit()

class Animal:
    def __init__(self, id, nome, especie, status):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.status = status

    def salvar(self):
        conn = Database.get_instance()
        c = conn.cursor()
        c.execute('INSERT INTO Animais (nome, especie, status) VALUES (?, ?, ?)', (self.nome, self.especie, self.status))
        conn.commit()

class Padrinho:
    def __init__(self, id, nome, animal_id=None):
        self.id = id
        self.nome = nome
        self.animal_id = animal_id

    def salvar(self):
        conn = Database.get_instance()
        c = conn.cursor()
        c.execute('INSERT INTO Padrinhos (nome, animal_id) VALUES (?, ?)', (self.nome, self.animal_id))
        conn.commit()
