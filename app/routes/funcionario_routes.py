from flask import Blueprint, render_template, request, redirect, url_for
from app.models.funcionario import (
    listar_funcionarios,
    inserir_funcionario,
    buscar_funcionario,
    atualizar_funcionario,
    deletar_funcionario,
)

bp_funcionario = Blueprint('funcionario', __name__)

@bp_funcionario.route('/')
def index():
    return render_template('index.html')

@bp_funcionario.route('/listar')
def listar():
    funcionarios = listar_funcionarios()
    return render_template('listar.html', funcionarios=funcionarios)

@bp_funcionario.route('/inserir', methods=['GET', 'POST'])
def inserir():
    if request.method == 'POST':
        nome = request.form['nome']
        cargo = request.form['cargo']
        salario = request.form['salario']
        inserir_funcionario(nome, cargo, salario)
        return redirect(url_for('funcionario.listar'))
    return render_template('inserir.html')

@bp_funcionario.route('/atualizar/<int:id>', methods=['GET', 'POST'])
def atualizar(id):
    if request.method == 'POST':
        cargo = request.form['cargo']
        salario = request.form['salario']
        atualizar_funcionario(id, cargo, salario)
        return redirect(url_for('funcionario.listar'))
    funcionario = buscar_funcionario(id)
    return render_template('atualizar.html', funcionario=funcionario)

@bp_funcionario.route('/deletar/<int:id>')
def deletar(id):
    deletar_funcionario(id)
    return redirect(url_for('funcionario.listar'))