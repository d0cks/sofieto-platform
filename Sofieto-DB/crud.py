from clientes import Cliente
from contatos import Contato
from aulas import Aula
from datetime import datetime
from modelo import Session

session = Session() 

# Clientes - Resgistra novos clientes e seus contatos; Consulta existentes.
def create_new_client(): # Cria um novo Cliente.
    nome = input("Digite o nome do novo cliente:")
    cliente = Cliente(nome= nome)
    session.add(cliente)
    session.commit()
    print(f"Cliente de ID: {cliente.id}, '{nome}' foi adicionado com sucesso!\n")
        
    resposta = input(f"Gostaria de adicionar um contato a {nome}? (s/n): ")
    while True:
        if resposta == 's':
            create_contato(cliente.id)  
            break    
        elif resposta == 'n':
            break
        else:
            print("Opção inválida")
            continue
    return cliente

def show_clients(): # Consulta os Clientes registrados no banco.
    cliente = session.query(Cliente).first()  
    if cliente:
        clientes = session.query(Cliente).all()
        print("Estes são os clientes registrados no banco:\n")
        for cliente in clientes:
                print(f"\nID: {cliente.id}, Nome: {cliente.nome}")
                if cliente.contato:
                    print(f"Contatos: Numero: {cliente.contato.celular} Email: {cliente.contato.email}")
    else:
        while True:
            resposta = input("Nenhum cliente registrado, gostaria de realizar um novo cadastro? (s/n): ")
            if resposta == 's':
                create_new_client()
                break
            elif resposta == 'n':
                return 0 
            else:
                print("Resposta Inválida!")
                continue

def create_contato(cliente_id): # Cria um contato baseado no id fornecido por atribuição
    cliente = session.query(Cliente).filter_by(id= cliente_id).first()

    if cliente:
        numero = input(f"Digite o numero de celular referente ao {cliente.nome}:")
        print(f"\nNumero de celular: {numero}, vinculado com sucesso ao cliente: {cliente.nome}\n")

        resposta = input("Gostaria de adicionar um email? (s/n): ")

        while True:
            if resposta == 's':
                email = input(f"Digite o email referente ao {cliente.nome}:")
                print(f"Email: {email}, vinculado com sucesso ao cliente: {cliente.nome}")

                novo_contato = Contato(celular= numero, email= email, cliente = cliente)
                session.add(novo_contato)
                session.commit()
                break
            elif resposta == 'n':
                novo_contato = Contato(celular= numero, cliente = cliente)
                session.add(novo_contato)
                session.commit()
                break
            else:
                print("Opção inválida")
                continue       
    else:
        resposta = input("Opção inválida, gostaria de criar um novo usuário? (s/n): ")
        while True:
            if resposta == 's':
                create_new_client()
                return 0 
            elif resposta == 'n':
                return 0 
            else:
                print("Opção inválida!")
                continue

def show_contatos(): # Consulta os Clientes e seus respectivos contatos.
    contato_list = session.query(Cliente, Contato).join(Contato).all()
    print("Estes são os contatos de clientes registrados no banco:\n")

    for cliente, contato in contato_list:
        print(f"Cliente: {cliente.id}, Nome: {cliente.nome}, Contatos: Numero: {contato.celular} Email: {contato.email}\n")
    return contato_list

def update_contato(): # Atualiza o contato de um Cliente já existente
    show_contatos()
    cliente_id = input("Selecione o 'ID' referente ao usuario que deseja atualizar o meio de contato: ")
    cliente = session.query(Cliente).filter_by(id= cliente_id).first()
    contato = session.query(Contato).filter_by(cliente_id = cliente_id).first()

    if cliente:
        resposta = input("Gostaria de atualizar o celular? (s/n): ")

        while True:
            if resposta == 's':
                numero = input(f"Digite o numero de celular referente ao {cliente.nome}:")
                print(f"Numero de celular: {numero}, vinculado com sucesso ao cliente: {cliente.nome}")
                contato.celular = numero
                resposta = input("Gostaria de atualizar o email? (s/n): ")

                if resposta == 's':
                    email = input(f"Digite o email referente ao {cliente.nome}:")
                    print(f"Email: {email}, vinculado com sucesso ao cliente: {cliente.nome}")
                    contato.email = email  
                    break
                elif resposta == 'n':
                    break
                else:
                    print("Opção inválida")
                    continue
                
            elif resposta == 'n':
                while True:
                    resposta = input("Gostaria de atualizar o email? (s/n): ")
                    if resposta == 's':
                        email = input(f"Digite o email referente ao {cliente.nome}:")
                        print(f"Email: {email}, vinculado com sucesso ao cliente: {cliente.nome}")
                        contato.email = email
                        break
                    elif resposta == 'n':
                        print("!O que você veio fazer aqui então!")
                        break
                    else:
                        print("Opção inválida")
                        continue    
            else:
                print("Opção inválida")
                continue       
    else:
        resposta = input("Opção inválida, gostaria de criar um novo usuário? (s/n)")
        while True:
            if resposta == 's':
                create_new_client()
                return 0 
            elif resposta == 'n':
                break 
            else:
                print("Opção inválida!")
                continue
    session.commit()     

def novo_contato():
    show_clients()
    cliente_id = input("Digite o 'ID' referente ao cliente a criar um novo contato: ")
    create_contato(cliente_id)
# Agenda de Aulas - Marcar, Desmarcar e Consultar.

def marcar_aula(): # Marca uma aula referente a um Cliente.
    cliente = session.query(Cliente).first()
    if cliente:
        print("Para marcar uma nova aula, é preciso selecionar um cliente já existente:\n")
        resposta = input("Gostaria de criar um novo? (s/n): ")        
        while True:
            if resposta == 's':
                cliente = create_new_client()
                break
            elif resposta == 'n':
                print("Clientes registrados: ")
                show_clients()
                cliente_id = input("Digite apenas o 'id' do cliente: ")
                cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
                break   
            else:
                print("Resposta inválida")
                continue 
    else:
        print("Nenhum cliente cadastrado, gerando novo...\n")
        cliente = create_new_client()
    print("Qual a data desejada da aula? \n")
    data_aula = get_date()
    resposta = input("Gostaria de adicionar descrição? (s/n): ")

    while True:
        if resposta == "s":
            desc = input("Descrição: ")
            aula = Aula(data = data_aula, desc = desc, cliente = cliente)
            break
        elif resposta == "n":
            aula = Aula(data = data_aula, cliente = cliente)
            break
        else:
            print("Resposta inválida")
            continue
    
    session.add(aula)
    session.commit()
    return aula

def get_date(): # Atribui uma data.     
    data_str = input("Digite a data da aula (formato YYYY-MM-DD HH:MM): ")
    try:  
        data_aula = datetime.strptime(data_str, "%Y-%m-%d %H:%M")
        return data_aula
    except ValueError:
        print("Formato de data inválido. Tente novamente.\n")
        return get_date()   

def show_aulas(): # Consulta.
    agenda = session.query(Cliente, Aula).join(Aula).all()
    if agenda:
        print("Agenda: ")  
        for cliente, aula in agenda:
            print(f"Aula: {aula.id}, Data: {aula.data}, Cliente: {cliente.id} Nome: {cliente.nome}")
            if aula.desc:
                print(f"Descrição: {aula.desc}\n")
    else:
        print("Nenhuma aula marcada até o momento...\n")

def desmarcar_aula(): # Desmarca uma aula
    show_aulas()
    aula_id = input("Digite o 'ID' da aula a ser desmarcada: ")
    aula = session.query(Aula).filter_by(id=aula_id).first()
    if aula:
        resposta = input(f"Tem certeza que deseja realizar o cancelamento da aula com id: {aula_id}? (s/n): ")
        while True:
            if resposta == 's':
                session.delete(aula)
                session.commit()
                print(f"Aula com ID {aula_id} deletada com sucesso.\n")
                break
            elif resposta == 'n':
                print("Nenhuma alteração foi realizada.\n")
                return 0 
            else:
                print("Opção Inválida!")
                continue
    else:
        print(f"Aula com ID {aula_id} não encontrada.")
        desmarcar_aula()

def remarcar_aula(): # Atualiza/Remarca uma aula
    show_aulas()
    aula_id = input("Digite o 'ID' da aula a ser remarcada: ")
    aula = session.query(Aula).filter_by(id=aula_id).first()
    if aula:
        data = get_date()
        
        resposta = input(f"Tem certeza que deseja realizar o reagendamento da aula com id: {aula_id}? (s/n): ")
        while True:
            if resposta == 's':
                aula.data = data
                session.commit()
                print(f"A aula de id: {aula_id}, foi remarcada para: {data}, com sucesso!\n")
                break
            elif resposta == 'n':
                print("Nenhuma alteração foi realizada.\n")
                return 0 
            else:
                print("Opção Inválida!\n")
                continue
    else:
        print(f"Aula com ID {aula_id} não encontrada.\n")
        remarcar_aula()