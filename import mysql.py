import mysql.connector

conexao = mysql.connector.connect (
    host='localhost',
    user='root',
    password='samuellucas',
    database='bdteste',
)

cursor = conexao.cursor()


nome_produto = "todynho"
valor = 6


comando = f'DELETE FROM vendas  WHERE idvendas = {2}'
cursor.execute(comando) 
conexao.commit() # edita o banco de dados


cursor.close()
conexao.close()




#CRUD
#nome_produto = "chocolate"
#valor = 15

#comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}" , {valor})'
#cursor.execute(comando) 

#conexao.commit() # edita o banco de dados



#READ
#comando = f'SELECT * FROM vendas'
#cursor.execute(comando) 
#resultado = cursor.fetchall() # ler o banco de dados
#print(resultado)

#UPDATE
#nome_produto = "todynho"
#valor = 6

#comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando) 
#conexao.commit() # edita o banco de dados


#DELETE
#comando = f'DELETE FROM vendas  WHERE idvendas = {2}'
#cursor.execute(comando) 
#conexao.commit() # edita o banco de dados

