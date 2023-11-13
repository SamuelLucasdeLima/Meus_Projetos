# main.py
from tkinter import *
from controller.aluno_controller import AlunoController

class Application:
    def __init__(self):
        self.root = Tk()
        self.tela()
        self.root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Alunos")
        self.controller = AlunoController(self.root)
        self.root.configure(background='white')
        self.root.geometry("788x588")
        self.root.resizable(True, True)
        self.root.maxsize(width=988, height=788)
        self.root.minsize(width=488, height=388)



if __name__ == "__main__":
    Application()
