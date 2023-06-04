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

@app.route('/resumo', methods=['POST'])
def resumo():
    # nome = "Paulo Henrique Brincker"
    # email = "paulobrincker@gmail.com"
    # telefone = "(65) 99271-7666"
    # tipo = 'Pessoa Física'
    # cpf_cnpj = '024.648.321-03'
    # itens = ['item1', 'item2']
    
    nome = request.form.get('nome')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    tipo = request.form.get('tipo')
    cpf_cnpj = request.form.get('cpf-cnpj')
    itens = request.form.getlist('itens')
    print(request.form)
    return render_template('cadastro_resumo.html', nome=nome, email=email, telefone=telefone, tipo=tipo, cpf_cnpj=cpf_cnpj, itens=itens)

@app.route('/add_item', methods=['get', 'post'])
def add_item():
    if request.method == "POST":
        return ('''
        <h5>Item adicionado!</h5>
        ''')
    else:
        return render_template("add_item.html")

@app.route('/dashboard', methods=['get'])
def dashboard():
    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run(debug=True)
