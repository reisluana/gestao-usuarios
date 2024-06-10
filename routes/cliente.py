from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

"""
rota de clientes

/clientes/ (GET) - listar os clientes
/clientes/ (POST) - inserir cliente no server
/clientes/new (GET) - renderizar form para cadastro de cliente
/clientes/<id> (GET) - obter os dados de um cliente
/clientes/<id>/edit (GET) - renderizar form de edição
/clientes/<id>/update (PUT) - atualizar os dados de um cliente
/clientes/<id>/delete (DELETE) - deletar o cliente
"""

@cliente_route.route('/')
def lista_clientes():
    # listar todos os clientes
    return render_template('lista_clientes.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    # insere os dados do cliente no banco
    
    data = request.json

    novo_usuario = {
        "id": len(CLIENTES)+1,
        "nome": data['nome'],
        "email": data['email']
    }

    CLIENTES.append(novo_usuario)

    return render_template('item_cliente.html', cliente=novo_usuario)


@cliente_route.route('/new')
def form_cliente():
    # form para cadastro de cliente
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    # exibir infos do cliente
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    # form para editar um cliente
    return render_template('form_edit_cliente.html')

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    # atualizar infos do cliente
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['PUT'])
def deletar_cliente(cliente_id):
    # deletar cliente
    pass