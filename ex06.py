import sqlite3 as conector

def conectar_banco(nome_banco):
    conexao = conector.connect(nome_banco)
    return conexao

def criar_tabelas(conexao):
    cursor = conexao.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS PRODUTOS (
                        ID SERIAL PRIMARY KEY,
                        NOME TEXT NOT NULL,
                        PRECO REAL NOT NULL,
                        ESTOQUE INTEGER NOT NULL
                 );''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS CLIENTES (
                        ID SERIAL PRIMARY KEY,
                        NOME TEXT NOT NULL,
                        EMAIL TEXT NOT NULL
                );''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS PEDIDOS(
                        ID SERIAL PRIMARY KEY,
                        CLIENTE_ID INTEGER NOT NULL,
                        PRODUTO_ID INTEGER NOT NULL,
                        QUANTIDADE INTEGER NOT NULL,
                        DATA_PEDIDO DATE NOT NULL,
                        FOREIGN KEY(CLIENTE_ID) REFERENCES CLIENTE(ID),
                        FOREIGN KEY(PRODUTO_ID) REFERENCES PRODUTOS(ID)
        
                );''')
    
    conexao.commit()
    cursor.close()
    
def inserir_dados(conexao):
    cursor = conexao.cursor()
    
    produtos = [('Notebook', 2999.99, 10),
                ('Smartphone', 1999.99, 20),
                ('Tablet', 999.99, 30)]
    
    clientes = [('Alice', 'alice@example.com'),
                ('Bob', 'bob@example.com'),
                ('Charlie', 'charlie@example.com')]
    
    pedidos = [(1, 1, 2, '2023/06/15'),
               (2, 2, 1, '2023/06/16'),
               (3, 3, 3, '2023/06/17')]
    cursor.executemany('INSERT INTO PRODUTOS(NOME, PRECO, ESTOQUE) VALUES (?, ?, ?)', produtos)
    cursor.executemany('INSERT INTO CLIENTES(NOME, EMAIL) VALUES (?, ?)', clientes)
    cursor.executemany('INSERT INTO PEDIDOS(CLIENTE_ID, PRODUTO_ID, QUANTIDADE, DATA_PEDIDO) VALUES (?, ?, ?, ?)', pedidos)
    
    conexao.commit()
    cursor.close()

    
if __name__ == '__main__':
    conexao =  conectar_banco('ecommerce.db')
    criar_tabelas(conexao)
    inserir_dados(conexao)
    conexao.close()