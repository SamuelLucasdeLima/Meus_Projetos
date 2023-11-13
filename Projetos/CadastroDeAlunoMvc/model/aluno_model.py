
import mysql.connector

class Aluno:
    def __init__(self, id, nome, idade, curso):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.curso = curso

class AlunoModel:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="samuellucas",
            database="escola"
        )
        self.cursor = self.conexao.cursor()

    def adicionar_aluno(self, nome, idade, curso):
        try:
            self.cursor.execute("INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)", (nome, idade, curso))
            self.conexao.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao adicionar aluno: {err}")
            return False

    def listar_alunos(self):
        self.cursor.execute("SELECT * FROM alunos")
        resultados = self.cursor.fetchall()
        alunos = [Aluno(id, nome, idade, curso) for id, nome, idade, curso in resultados]
        return alunos
