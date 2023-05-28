import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# Função para criar a tabela no banco de dados
def criar_tabela():
    conn = sqlite3.connect('dados.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (nome text, email text, filho text)''')
    conn.commit()
    conn.close()

# Chamada da função para criar a tabela
criar_tabela()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        filho = request.form['filho']
        
        # Conexão com o banco de dados
        conn = sqlite3.connect('dados.db')
        c = conn.cursor()
        
        # Inserir os dados na tabela
        c.execute("INSERT INTO usuarios VALUES (?, ?, ?)", (nome, email, filho))
        
        # Salvar as alterações e fechar a conexão com o banco de dados
        conn.commit()
        conn.close()

        return render_template('sucesso.html')
    
    return render_template('cadastro.html')


if __name__ == '__main__':
    app.run(debug=True)