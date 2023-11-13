import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Função para adicionar aluno ao banco de dados
def adicionar_aluno():
    nome = entry_nome.get()
    idade = entry_idade.get()
    curso = entry_curso.get()

    if nome and idade and curso:
        try:
            cursor.execute("INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)", (nome, idade, curso))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso!")
            limpar_campos()
            listar_alunos()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar aluno: {str(e)}")
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")

# Função para listar alunos na interface gráfica
def listar_alunos():
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    lista_alunos.delete(0, tk.END)
    for aluno in alunos:
        lista_alunos.insert(tk.END, aluno)

# Função para limpar os campos de entrada
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_curso.delete(0, tk.END)

# Configurações da janela principal
root = tk.Tk()
root.title("Cadastro de Alunos")

# Conectar ao banco de dados MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="samuellucas",
    database="escola"
)
cursor = conexao.cursor()

# Componentes da interface gráfica
tk.Label(root, text="Nome:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="Idade:").pack()
entry_idade = tk.Entry(root)
entry_idade.pack()

tk.Label(root, text="Curso:").pack()
entry_curso = tk.Entry(root)
entry_curso.pack()

btn_adicionar = tk.Button(root, text="Adicionar Aluno", command=adicionar_aluno)
btn_adicionar.pack()

lista_alunos = tk.Listbox(root)
lista_alunos.pack()

btn_listar = tk.Button(root, text="Listar Alunos", command=listar_alunos)
btn_listar.pack()

root.mainloop()
