# aluno_view.py
import tkinter as tk

class AlunoView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        tk.Label(self.root, text="Nome:").pack()
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.pack()

        tk.Label(self.root, text="Idade:").pack()
        self.entry_idade = tk.Entry(self.root)
        self.entry_idade.pack()

        tk.Label(self.root, text="Curso:").pack()
        self.entry_curso = tk.Entry(self.root)
        self.entry_curso.pack()

        btn_adicionar = tk.Button(self.root, text="Adicionar Aluno", command=self.adicionar_aluno)
        btn_adicionar.pack()

        self.lista_alunos = tk.Listbox(self.root)
        self.lista_alunos.pack()

        btn_listar = tk.Button(self.root, text="Listar Alunos", command=self.listar_alunos)
        btn_listar.pack()

    def adicionar_aluno(self):
        nome = self.entry_nome.get()
        idade = self.entry_idade.get()
        curso = self.entry_curso.get()
        self.controller.adicionar_aluno(nome, idade, curso)

    def listar_alunos(self):
        alunos = self.controller.listar_alunos()
        self.lista_alunos.delete(0, tk.END)
        for aluno in alunos:
            self.lista_alunos.insert(tk.END, f"{aluno.nome} - {aluno.idade} anos - {aluno.curso}")
