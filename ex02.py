import sqlite3 as conector

try:
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()
    
    comando = ''' CREATE TABLE Marca (
                        id SERIAL PRIMARY KEY NOT NULL,
                         nome TEXT NOT NULL,
                         sigla CHARACTER(2) NOT NULL);
                    '''
    cursor.execute(comando)
    
    conexao.commit()

except conector.DatabaseError as err:
    print('Erro de banco de dados', err)

finally:
    if conexao:
        cursor.close()
        conexao.close()
    

