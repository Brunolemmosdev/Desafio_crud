 mysql.importconnector

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Blf072712@",
            database="funcionarios",
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None

def criar_tabela(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS funcionarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                cargo VARCHAR(100) NOT NULL,
                salario DECIMAL(10,2) NOT NULL
            )
        """)
        conexao.commit()
        cursor.close()
    except mysql.connector.Error as erro:
        print(f"Erro ao criar tabela: {erro}")

def inserir_funcionario(conexao):
    try:
        nome = input("Nome: ")
        cargo = input("Cargo: ")
        salario = float(input("Salário: "))
        cursor = conexao.cursor()
        comando = "INSERT INTO funcionarios (nome, cargo, salario) VALUES (%s, %s, %s)"
        valores = (nome, cargo, salario)
        cursor.execute(comando, valores)
        conexao.commit()
        print("Funcionário inserido com sucesso!")
        cursor.close()
    except ValueError:
        print("Salário inválido!")
    except mysql.connector.Error as erro:
        print(f"Erro ao inserir funcionário: {erro}")

def listar_funcionarios(conexao):
    try:
        cursor = conexao.cursor()
        comando = "SELECT * FROM funcionarios"
        cursor.execute(comando)
        resultado = cursor.fetchall()
        if resultado:
            print("Funcionários cadastrados:")
            for funcionario in resultado:
                print(f"ID: {funcionario[0]}, Nome: {funcionario[1]}, Cargo: {funcionario[2]}, Salário: {funcionario[3]}")
        else:
            print("Nenhum funcionário cadastrado.")
        cursor.close()
    except mysql.connector.Error as erro:
        print(f"Erro ao consultar funcionários: {erro}")

def atualizar_funcionario(conexao):
    try:
        id_func = int(input("ID do funcionário a atualizar: "))
        cargo = input("Novo cargo: ")
        salario = float(input("Novo salário: "))
        cursor = conexao.cursor()
        comando = "UPDATE funcionarios SET cargo = %s, salario = %s WHERE id = %s"
        valores = (cargo, salario, id_func)
        cursor.execute(comando, valores)
        if cursor.rowcount == 0:
            print("Funcionário não encontrado.")
        else:
            conexao.commit()
            print("Funcionário atualizado com sucesso!")
        cursor.close()
    except ValueError:
        print("Entrada inválida!")
    except mysql.connector.Error as erro:
        print(f"Erro ao atualizar funcionário: {erro}")

def deletar_funcionario(conexao):
    try:
        id_func = int(input("ID do funcionário a deletar: "))
        cursor = conexao.cursor()
        comando = "DELETE FROM funcionarios WHERE id = %s"
        valores = (id_func,)
        cursor.execute(comando, valores)
        if cursor.rowcount == 0:
            print("Funcionário não encontrado.")
        else:
            conexao.commit()
            print("Funcionário deletado com sucesso!")
        cursor.close()
    except ValueError:
        print("ID inválido!")
    except mysql.connector.Error as erro:
        print(f"Erro ao deletar funcionário: {erro}")

def menu():
    conexao = conectar()
    if not conexao:
        return
    criar_tabela(conexao)
    while True:
        print("\n--- MENU CRUD FUNCIONÁRIOS ---")
        print("1. Inserir funcionário")
        print("2. Listar funcionários")
        print("3. Atualizar funcionário")
        print("4. Deletar funcionário")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            inserir_funcionario(conexao)
        elif opcao == '2':
            listar_funcionarios(conexao)
        elif opcao == '3':
            atualizar_funcionario(conexao)
        elif opcao == '4':
            deletar_funcionario(conexao)
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
    conexao.close()

if __name__ == "__main__":
    menu()
