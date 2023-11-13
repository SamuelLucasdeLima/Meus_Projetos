import mysql.connector

class EstoqueModel:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()
        self.criar_tabela_saidas()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255),
                tipo VARCHAR(255),
                quantidade INT
            )
        ''')
        self.connection.commit()

    def criar_tabela_saidas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS saidas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                produto_id INT,
                quantidade INT,
                funcionario VARCHAR(255)
            )
        ''')
        self.connection.commit()

    def inserir_produto(self, nome, tipo, quantidade):
        query = "INSERT INTO produtos (nome, tipo, quantidade) VALUES (%s, %s, %s)"
        values = (nome, tipo, quantidade)
        self.cursor.execute(query, values)
        self.connection.commit()

    def listar_produtos(self):
        self.cursor.execute("SELECT * FROM produtos")
        return self.cursor.fetchall()

    def obter_produto_por_nome_tipo(self, nome, tipo):
        self.cursor.execute("SELECT * FROM produtos WHERE nome = %s AND tipo = %s", (nome, tipo))
        return self.cursor.fetchone()

    def listar_produtos_por_categoria(self, categoria):
        self.cursor.execute("SELECT * FROM produtos WHERE tipo = %s", (categoria,))
        return self.cursor.fetchall()

    def registrar_entrada(self, nome, tipo, quantidade):
        self.inserir_produto(nome, tipo, quantidade)

    def registrar_saida(self, nome, tipo, quantidade, funcionario):
        produto = self.obter_produto_por_nome_tipo(nome, tipo)
        if produto:
            produto_id = produto[0]
            estoque_atual = produto[3]
            if tipo.lower() == 'alimentício' and quantidade < 0:
                print("Produto alimentício consumido, não pode ser devolvido.")
            elif estoque_atual >= abs(quantidade):
                self.cursor.execute("INSERT INTO saidas (produto_id, quantidade, funcionario) VALUES (%s, %s, %s)",
                                    (produto_id, quantidade, funcionario))
                self.cursor.execute("UPDATE produtos SET quantidade = quantidade - %s WHERE id = %s",
                                    (abs(quantidade), produto_id))
                self.connection.commit()
            else:
                print("Estoque insuficiente.")
        else:
            print("Produto não encontrado.")

    def listar_produto_zerado(self):
        self.cursor.execute("SELECT * FROM produtos WHERE quantidade = 0")
        return self.cursor.fetchall()

    def registrar_devolucao(self, nome, tipo, quantidade):
        produto = self.obter_produto_por_nome_tipo(nome, tipo)
        if produto:
            produto_id = produto[0]
            self.cursor.execute("UPDATE produtos SET quantidade = quantidade + %s WHERE id = %s",
                                (quantidade, produto_id))
            self.connection.commit()

    def fechar_conexao(self):
        self.cursor.close()
        self.connection.close()
