from flask import Blueprint, render_template, request, redirect, url_for, jsonify
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

@bp_funcionario.route('/api/funcionarios')
def api_funcionarios():
    funcionarios = listar_funcionarios()
    return jsonify(funcionarios)

@bp_funcionario.route('/inserir', methods=['POST'])
def inserir():
    data = request.get_json()
    nome = data['nome']
    cargo = data['cargo']
    salario = data['salario']
    inserir_funcionario(nome, cargo, salario)
    return jsonify({'status': 'ok'})

@bp_funcionario.route('/atualizar/<int:id>', methods=['PUT'])
def atualizar(id):
    data = request.get_json()
    cargo = data['cargo']
    salario = data['salario']
    atualizar_funcionario(id, cargo, salario)
    return jsonify({'status': 'ok'})

@bp_funcionario.route('/deletar/<int:id>', methods=['DELETE'])
def deletar(id):
    deletar_funcionario(id)
    return jsonify({'status': 'ok'})