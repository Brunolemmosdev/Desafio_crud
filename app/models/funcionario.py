import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Blf072712@",
        database="funcionarios"
    )

def listar_funcionarios():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, cargo, salario FROM funcionarios")
    funcionarios = cursor.fetchall()
    cursor.close()
    conexao.close()
    return funcionarios

def inserir_funcionario(nome, cargo, salario):
    conexao = conectar()
    cursor = conexao.cursor()
    comando = "INSERT INTO funcionarios (nome, cargo, salario) VALUES (%s, %s, %s)"
    valores = (nome, cargo, salario)
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def buscar_funcionario(id):
    conexao = conectar()
    cursor = conexao.cursor()
    comando = "SELECT * FROM funcionarios WHERE id = %s"
    cursor.execute(comando, (id,))
    funcionario = cursor.fetchone()
    cursor.close()
    conexao.close()
    return funcionario

def atualizar_funcionario(id, cargo, salario):
    conexao = conectar()
    cursor = conexao.cursor()
    comando = "UPDATE funcionarios SET cargo = %s, salario = %s WHERE id = %s"
    valores = (cargo, salario, id)
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def deletar_funcionario(id):
    conexao = conectar()
    cursor = conexao.cursor()
    comando = "DELETE FROM funcionarios WHERE id = %s"
    cursor.execute(comando, (id,))
    conexao.commit()
    cursor.close()
    conexao.close()