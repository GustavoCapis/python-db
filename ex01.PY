import sqlite3 as conector

try:
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()
    
    comando = '''CREATE TABLE Pessoa (
        cpf TEXT NOT NULL,
        nome TEXT NOT NULL,
        nascimento DATE NOT NULL,
        oculos BOOLEAN NOT NULL,
        PRIMARY KEY (cpf));'''
        
    cursor.execute(comando)
    
    conexao.commit()
    
except conector.DatabaseError as err:
    print("Erro de banco de dados", err)

finally:
    if conexao:
        cursor.close()
        conexao.close()