from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página de pagamento
@app.route('/cadastro', methods=['GET'])
def pagamento():
    return render_template('cadastro.html')

@app.route('/resumo', methods=['GET'])
def resumo():
    # nome = "Paulo Henrique Brincker"
    # email = "paulobrincker@gmail.com"
    # telefone = "(65) 99271-7666"
    # tipo = 'Pessoa Física'
    # cpf_cnpj = '024.648.321-03'
    # itens = ['item1']
    
    nome = request.form.get('nome')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    tipo = request.form.get('tipo')
    cpf_cnpj = request.form.get('cpf-cnpj')
    itens = request.form.getlist('itens')

    return render_template('cadastro_resumo.html', nome=nome, email=email, telefone=telefone, tipo=tipo, cpf_cnpj=cpf_cnpj, itens=itens)


if __name__ == '__main__':
    app.run(debug=True)
