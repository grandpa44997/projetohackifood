import tkinter as tk
import sqlite3

def mostrar_dados():
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    rows = cursor.fetchall()
    conn.close()
    
    for row in rows:
        print(row)  # Exemplo: exibir os dados no console

def criar_tabela():
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (nome TEXT, email TEXT, filho TEXT)')
    conn.commit()
    conn.close()

# Cria a janela principal
root = tk.Tk()

# Função para criar a tabela no banco de dados
criar_tabela()

# Botão para mostrar os dados
btn_mostrar_dados = tk.Button(root, text="Mostrar Dados", command=mostrar_dados)
btn_mostrar_dados.pack()

# Inicie o loop principal da janela
root.mainloop()