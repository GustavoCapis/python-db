import sqlite3 as conector

try:
    conexao = conector.connect('./meu_banco.db')
    cursor = conexao.cursor()

    # 1. Dados de Pessoas
    pessoas = [
        ("11111111111", "João Silva", "1990-05-10", 1),
        ("22222222222", "Maria Souza", "1985-08-22", 0),
        ("33333333333", "Carlos Lima", "2000-01-15", 1)
    ]

    # 2. Dados de Marcas
    marcas = [
        (1, "Toyota", "TYT"),
        (2, "Honda", "HND"),
        (3, "Ford", "FRD")
    ]

    # 3. Dados de Veículos
    veiculos = [
        ("ABC1234", 2010, "Preto", "1.0", "11111111111", 1),
        ("DEF5678", 2015, "Branco", "1.6", "22222222222", 2),
        ("GHI9012", 2020, "Vermelho", "2.0", "33333333333", 3)
    ]

    # Inserindo com "OR IGNORE" para não dar erro se você rodar duas vezes
    cursor.executemany("INSERT OR IGNORE INTO Pessoa VALUES (?, ?, ?, ?)", pessoas)
    cursor.executemany("INSERT OR IGNORE INTO Marca VALUES (?, ?, ?)", marcas)
    cursor.executemany("INSERT OR IGNORE INTO Veiculo VALUES (?, ?, ?, ?, ?, ?)", veiculos)

    conexao.commit()
    print("✅ Show! Banco populado com sucesso.")

except conector.Error as e:
    print(f"❌ Erro ao popular: {e}")

finally:
    if conexao:
        conexao.close()