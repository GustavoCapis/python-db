import sqlite3 as conector

class Livro:
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        
class Pedido:
    def __init__(self, cliente_id, livro_id, quantidade, data_pedido):
        self.cliente_id = cliente_id
        self.livro_id = livro_id
        self.quantidade = quantidade
        self.data_pedido =data_pedido
        
def conectar_banco(nome_banco):
    conexao = conector.connect(nome_banco)
    return conexao

def criar_tabelas(conexao):
    cursor = conexao.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS LIVROS(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        TITULO TEXT NOT NULL,
                        AUTOR TEXT NOT NULL,
                        PRECO REAL NOT NULL
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS CLIENTES(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NOME TEXT NOT NULL,
                        EMAIL REAL NOT NULL
    )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS PEDIDOS(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        CLIENTE_ID INTEGER NOT NULL,
                        LIVRO_ID INTEGER NOT NULL,
                        QUANTIDADE INTEGER NOT NULL,
                        DATA_PEDIDO DATE NOT NULL,
                        FOREIGN KEY (CLIENTE_ID) REFERENCES CLIENTES(ID),
                        FOREIGN KEY (LIVRO_ID) REFERENCES LIVROS(ID)
    )''')
    
    conexao.commit()
    
def inserir_dados(conexao):
    cursor = conexao.cursor()
    
    livros = [Livro('Python para Iniciantes', 'John Doe', 39.99),
              Livro('Algoritmos e Estruturas de Dados', 'Jane Smith', 49.99),
              Livro('Inteligência Artificial', 'Alan Turing', 59.99)]
    
    clientes = [Cliente('Alice', 'alice@example.com'),
                Cliente('Bob', 'bob@example.com'),
                Cliente('Charlie', 'charlie@example.com')]
    
    pedidos = [Pedido(1, 1, 2, '2023-06-15'),
               Pedido(2, 2, 1, '2023-06-16'),
               Pedido(3, 3, 3, '2023-06-17')]
    
    for livro in livros:
        cursor.execute('INSERT INTO LIVROS (TITULO, AUTOR, PRECO) VALUES (:titulo, :autor, :preco)',
                       vars(livro))
        
    for cliente in clientes:
        cursor.execute('INSERT INTO CLIENTES (NOME, EMAIL) VALUES (:nome, :email)',
                       vars(cliente))
    
    for pedido in pedidos:
        cursor.execute('INSERT INTO PEDIDOS (CLIENTE_ID, LIVRO_ID, QUANTIDADE, DATA_PEDIDO) VALUES (:cliente_id, :livro_id, :quantidade, :data_pedido)',
                       vars(pedido))
    
    conexao.commit()
    
def exibir_pedidos(conexao):
    cursor = conexao.cursor()
    query = '''
    SELECT PEDIDOS.ID, CLIENTES.NOME, LIVROS.TITULO, PEDIDOS.QUANTIDADE, PEDIDOS.DATA_PEDIDO
    FROM PEDIDOS
    JOIN CLIENTES ON PEDIDOS.CLIENTE_ID = CLIENTES.ID
    JOIN LIVROS ON PEDIDOS.LIVRO_ID = LIVROS.ID 
    '''
    cursor.execute(query)
    pedidos = cursor.fetchall()
    print('Pedidos: ')
    
    for pedido in pedidos:
        print(pedido)
        
if __name__ == '__main__':
    conexao = conectar_banco('livraria.db')
    criar_tabelas(conexao)
    inserir_dados(conexao)
    exibir_pedidos(conexao)
    conexao.close()