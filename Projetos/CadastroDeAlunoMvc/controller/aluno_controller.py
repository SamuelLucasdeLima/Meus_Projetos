# aluno_controller.py
from model.aluno_model import AlunoModel
from view.aluno_view import AlunoView

class AlunoController:
    def __init__(self, root):
        self.model = AlunoModel()
        self.view = AlunoView(root, self)

    def adicionar_aluno(self, nome, idade, curso):
        if self.model.adicionar_aluno(nome, idade, curso):
            self.view.listar_alunos()

    def listar_alunos(self):
        return self.model.listar_alunos()
