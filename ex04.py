import sqlite3 as conector

try:
    
    conexao = conector.connect("./meu_banco.db")
    
    cursor = conexao.cursor()
    
    comando1 = '''DROP TABLE Veiculo;'''    
    cursor.execute(comando1)
    
    comando2 = '''CREATE TABLE Veiculo (
                    placa VARCHAR(7) NOT NULL,
                    ano INTEGER NOT NULL,
                    cor TEXT NOT NULL,
                    motor REAL NOT NULL,
                    proprietario TEXT NOT NULL,
                    marca INTEGER NOT NULL,
                    PRIMARY KEY(placa),
                    FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
                    FOREIGN KEY(marca) REFERENCES Marca(id)  
                );'''
    cursor.execute(comando2)
    
    conexao.commit()

except conector.DatabaseError as err:
    print('Erro de banco de dados', err)

finally:
    if conexao:
        cursor.close()
        conexao.close()
    