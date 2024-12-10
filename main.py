from database import Database
from models import Funcionario, Animal, Padrinho
from agendamento import Agendamento, VacinaçãoServico, CastracaoServico, ServicoStrategy
from entity_factory import EntityFactory

# Função para adicionar um novo funcionário
def adicionar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    tipo = input("Digite o tipo de funcionário (administrador/voluntário): ")
    funcionario = Funcionario(None, nome, tipo)
    funcionario.salvar()
    print(f"Funcionário {nome} adicionado com sucesso!")

# Função para adicionar um novo animal
def adicionar_animal():
    nome = input("Digite o nome do animal: ")
    especie = input("Digite a espécie do animal: ")
    status = input("Digite o status do animal (abrigado/adoção): ")
    animal = Animal(None, nome, especie, status)
    animal.salvar()
    print(f"Animal {nome} adicionado com sucesso!")

# Função para adicionar um novo padrinho
def adicionar_padrinho():
    nome = input("Digite o nome do padrinho: ")
    animal_id = int(input("Digite o ID do animal que será apadrinhado: "))
    padrinho = Padrinho(None, nome, animal_id)
    padrinho.salvar()
    print(f"Padrinho {nome} adicionado com sucesso!")

# Função para listar todos os animais
def listar_animais():
    conn = Database.get_instance()
    c = conn.cursor()
    c.execute("SELECT id, nome, especie, status FROM Animais")
    animais = c.fetchall()

    if animais:
        print("Lista de Animais:")
        for animal in animais:
            print(f"ID: {animal[0]} | Nome: {animal[1]} | Espécie: {animal[2]} | Status: {animal[3]}")
    else:
        print("Nenhum animal encontrado.")

# Função para listar todos os padrinhos
def listar_padrinhos():
    conn = Database.get_instance()
    c = conn.cursor()
    c.execute('''
        SELECT Padrinhos.id, Padrinhos.nome, Animais.nome 
        FROM Padrinhos
        LEFT JOIN Animais ON Padrinhos.animal_id = Animais.id
    ''')
    padrinhos = c.fetchall()

    if padrinhos:
        print("Lista de Padrinhos:")
        for padrinho in padrinhos:
            print(f"ID: {padrinho[0]} | Nome: {padrinho[1]} | Animal Apadrinhado: {padrinho[2]}")
    else:
        print("Nenhum padrinho encontrado.")

# Função para registrar o pagamento de um padrinho
def registrar_pagamento():
    animal_id = int(input("Informe o ID do animal que o padrinho está apadrinhando: "))
    valor_pago = float(input("Informe o valor do pagamento: "))
    
    conn = Database.get_instance()
    c = conn.cursor()
    
    # Vamos registrar o pagamento de forma simples, associando ao animal
    c.execute('''
        INSERT INTO Pagamentos (animal_id, valor_pago) VALUES (?, ?)
    ''', (animal_id, valor_pago))
    
    conn.commit()
    print("Pagamento registrado com sucesso!")

# Função para exibir o menu e capturar a opção escolhida
def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar Funcionário")
        print("2. Adicionar Animal")
        print("3. Adicionar Padrinho")
        print("4. Listar Animais")
        print("5. Listar Padrinhos")
        print("6. Agendar Serviço")
        print("7. Registrar Pagamento")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_funcionario()
        elif opcao == '2':
            adicionar_animal()
        elif opcao == '3':
            adicionar_padrinho()
        elif opcao == '4':
            listar_animais()  # Chama a função para listar animais
        elif opcao == '5':
            listar_padrinhos()  # Chama a função para listar padrinhos
        elif opcao == '6':
            print("Função de agendamento de serviço ainda não implementada.")
        elif opcao == '7':
            registrar_pagamento()  # Chama a função para registrar pagamento
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chama o menu para rodar o programa
if __name__ == "__main__":
    menu()