import sqlite3

class Database:
    _instance = None

    @staticmethod
    def get_instance():
        """Retorna a instância única da conexão com o banco de dados."""
        if Database._instance is None:
            Database._instance = sqlite3.connect('ong.db')
            Database.criar_tabelas()  # Cria as tabelas no banco de dados ao obter a instância pela primeira vez
        return Database._instance

    @staticmethod
    def close():
        """Fecha a conexão com o banco de dados."""
        if Database._instance is not None:
            Database._instance.close()
            Database._instance = None

    @staticmethod
    def criar_tabelas():
        """Cria as tabelas necessárias no banco de dados, se não existirem."""
        conn = Database.get_instance()
        c = conn.cursor()

        # Criar tabela de Funcionários
        c.execute('''
            CREATE TABLE IF NOT EXISTS Funcionarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                tipo TEXT NOT NULL
            )
        ''')

        # Criar tabela de Animais
        c.execute('''
            CREATE TABLE IF NOT EXISTS Animais (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                especie TEXT NOT NULL,
                status TEXT NOT NULL
            )
        ''')

        # Criar tabela de Padrinhos
        c.execute('''
            CREATE TABLE IF NOT EXISTS Padrinhos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                animal_id INTEGER,
                FOREIGN KEY (animal_id) REFERENCES Animais (id)
            )
        ''')

        # Criar tabela de Agendamentos
        c.execute('''
            CREATE TABLE IF NOT EXISTS Agendamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                animal_id INTEGER NOT NULL,
                data TEXT NOT NULL,
                tipo_servico TEXT NOT NULL,
                FOREIGN KEY (animal_id) REFERENCES Animais (id)
            )
        ''')

        # Criar tabela de Pagamentos
        c.execute('''
            CREATE TABLE IF NOT EXISTS Pagamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                animal_id INTEGER NOT NULL,
                valor_pago REAL NOT NULL,
                FOREIGN KEY (animal_id) REFERENCES Animais (id)
            )
        ''')

        conn.commit()
