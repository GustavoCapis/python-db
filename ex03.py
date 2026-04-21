import sqlite3 as conector

try:
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()
    
    comando = '''CREATE TABLE Veiculo (
        placa CHARACTER(7) PRIMARY KEY NOT NULL,
        ano INTEGER  NOT NULL,
        cor TEXT NOT NULL,
        proprietario TEXT NOT NULL,
        marca INTEGER NOT NULL,
        FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf)
        )'''
    
    cursor.execute(comando)
    
    conexao.commit()

except conector.DatabaseError as err:
    print("Erro no banco de dados", err)

finally:
    if conexao:
        cursor.close()
        conexao.close()
    