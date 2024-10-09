import os
import crud

# Menu de seleção #
def selecao():
    print("==============================")
    print("=== Banco de Dados Sofieto ===")
    print("==============================")
    print("====== Menu de Opções: =======")
    print("==============================")
    print("==> 1. Clientes")
    print("==> 2. Contatos")
    print("==> 3. Aulas")
    print("==> 4. Sair...\n")
    print("==> 9. Deletar '.db' (!DEV ONLY!)\n")

    opcao = input("Digite o numero da opção que deseja consultar: ")
    clear_terminal()
    return opcao

# Menu de Seleção --> Clientes: 1.     
def menu_cliente():
    print("==============================")
    print("========= Clientes: ==========")
    print("==============================\n")
    print("==> 1. Criar novo cliente:")
    print("==> 2. Lista de todos os Clientes:")
    print("==> 3. Sair...\n")

    opcao = input("Digite o numero da opção que deseja consultar: ")
    clear_terminal()
    return opcao

# Menu de Seleção --> Contatos 2.
def menu_contato():
    print("==============================")
    print("========= Contatos: ==========")
    print("==============================\n")
    print("==> 1. Vincular novo contato a cliente:")
    print("==> 2. Atualizar contato existente; ")
    print("==> 3. Lista de todos os clientes e respectivos contatos;")
    print("==> 4. Sair...\n")

    opcao = input("Digite o numero da opção que deseja consultar: ")
    clear_terminal()
    return opcao

# Menu de Seleção --> Agenda 3.
def menu_agenda():
    print("==============================")
    print("========= Agenda: ============")
    print("==============================\n")
    print("==> 1. Marcar aula:")
    print("==> 2. Desmarcar aula:")
    print("==> 3. Remarcar aula:")
    print("==> 4. Lista de aulas:")
    print("==> 5. Sair...\n")

    opcao = input("Digite o numero da opção que deseja consultar: ")
    clear_terminal()
    return opcao

# Menu Principal #
def Menu():
    clear_terminal()
    opcao = selecao()   
    while True:     
        if opcao == '1': # Menu Clientes
            cliente = menu_cliente()
            if cliente == '1':
                crud.create_new_client()
                input("\nPressione Enter...")
                clear_terminal()
            elif cliente == '2': 
                crud.show_clients()
                input("\nPressione Enter...")
                clear_terminal()
            elif cliente == '3':
                Menu()
                break
            else:
                clear_terminal()
                print("Opção inválida...")
                input("\nPressione Enter...")
                clear_terminal()
        elif opcao == '2': # Menu Contatos
            contato = menu_contato()
            if contato == '1':
                crud.novo_contato()
                input("Pressione Enter...")
                clear_terminal()
            elif contato == '2':
                crud.update_contato()
                input("Pressione Enter...")
                clear_terminal()
            elif contato == '3':
                crud.show_contatos()
                input("Pressione Enter...")
                clear_terminal()                
            elif contato == '4':
                Menu()
                break
            else:
                clear_terminal()
                print("Opção inválida...")
                input("\nPressione Enter...")
                clear_terminal()
        elif opcao == '3': # Menu Agenda
            aula = menu_agenda()
            if aula == '1':
                crud.marcar_aula()
                input("\nPressione Enter...")
                clear_terminal()
            elif aula == '2':
                crud.desmarcar_aula()
                input("\nPressione Enter..")
                clear_terminal()
            elif aula == '3':
                crud.remarcar_aula()
                input("\nPressione Enter...")
                clear_terminal()
            elif aula == '4':
                crud.show_aulas()
                input("\nPressione Enter...")
                clear_terminal()
            elif aula == '5':
                Menu()
                break
            else:
                print("Opção inválida...")
                continue
        elif opcao == '4':  # 'Log-Out'
            input("Pressione Enter para sair...")
            print(":)")
            clear_terminal()
            return False
        elif opcao == '9': # Kabum!
            clear_terminal()
            deletar_banco_dados('sofieto.db') 
            clear_terminal()
            return False
        else:
            input("Opção inválida, tente novamente.")
            clear_terminal()
            Menu()

def deletar_banco_dados(caminho_db): # Deleta o arquivo '.db'/ Funcionabilidade para testes
    try:
        if os.path.exists(caminho_db):
            os.remove(caminho_db)
            print(f"Arquivo '{caminho_db}' foi deletado com sucesso.")
        else:
            print(f"O arquivo '{caminho_db}' não existe.")
    except Exception as e:
        print(f"Erro ao tentar deletar o arquivo: {e}")

def clear_terminal(): # Limpa o terminal
    if os.name == 'nt': # Windows
        os.system('cls')
    else: # Linux
        os.system('clear')  