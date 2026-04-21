import sqlite3 as conector

try:
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()
    
    comando = '''-- 1. Criar nova tabela
CREATE TABLE Veiculo_novo (
    placa CHARACTER(7) PRIMARY KEY NOT NULL,
    ano INTEGER NOT NULL,
    cor TEXT NOT NULL,
    proprietario TEXT NOT NULL,
    marca INTEGER NOT NULL,
    modelo INTEGER NOT NULL,

    FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
    FOREIGN KEY(marca) REFERENCES Modelo(id)
);

-- 2. Copiar dados
INSERT INTO Veiculo_novo (placa, ano, cor, proprietario, marca)
SELECT placa, ano, cor, proprietario, marca FROM Veiculo;

-- 3. Apagar antiga
DROP TABLE Veiculo;

-- 4. Renomear
ALTER TABLE Veiculo_novo RENAME TO Veiculo;'''
    
    cursor.execute(comando)
    
    conexao.commit()

except conector.DatabaseError as err:
    print("Erro no banco de dados", err)

finally:
    if conexao:
        cursor.close()
        conexao.close()
    