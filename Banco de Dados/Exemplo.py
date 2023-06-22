import sqlite3

conexao = sqlite3.connect('exemplo.db')

cursor = conexao.cursor()

#cursor.execute('INSERT INTO alunos (nome, email) VALUES ("Cedric","cedric.dev.assist@outlook.pt")')
#cursor.execute('SELECT * FROM alunos')
#cursor.execute('SELECT * FROM clientes')
#cursor.execute('SELECT * alunos WHERE ra = 1')
#cursor.execute('SELECT email, nome FROM clientes WHERE nome = "Cedric"')
cursor.execute('CREATE TABLE IF NOT EXISTS alunos ( ra INTEGER PRIMARY KEY, nome TEXT, email TEXT)')

#linhas = cursor.fetchall()
#print(linhas)
#for linha in linhas:
#    print(linha)

conexao.commit()

conexao.close()