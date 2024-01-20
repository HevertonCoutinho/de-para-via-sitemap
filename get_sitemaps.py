import sqlite3
import json

escolha = int(input('1 - Adicionar ao banco\n2 - Inserir o sitemap manualmente\n3 - Listar Clientes do banco\n> '))

resultado = None

if escolha == 1:

    conn = sqlite3.connect('banco.db')

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,    
            cliente TEXT NOT NULL,
            cb INT NOT NULL,
            sitemap TEXT NOT NULL
        )
    ''')

    cliente = str(input('Nome do cliente: '))
    cb = int(input('CB: '))
    entrada_usuario = input('Insira a lista de sitemaps separados por vírgula:\n> ')
    sitemap = list(map(str.strip, entrada_usuario.split(',')))

    sitemaps_json = json.dumps(sitemap)

    cursor.execute("INSERT INTO cliente (cliente, cb, sitemap) VALUES (?, ?, ?)", (cliente, cb, sitemaps_json))

    conn.commit()

    cliente_nome = cliente
    cursor.execute("SELECT sitemap FROM cliente WHERE cliente = ?", (cliente_nome,))
    resultado = cursor.fetchone()
    print("Cliente Adicionado")

elif escolha == 2:

    listaSitemap = []
    entrada_usuario = input('Insira a lista de sitemaps separados por vírgula:\n> ')
    listaSitemap.extend(map(str.strip, entrada_usuario.split(', ')))

    def get_sitemap_urls():
        return listaSitemap

elif escolha == 3:

    sitemaps_json = resultado[0]

    sitemaps_recuperados = json.loads(sitemaps_json)

    print (sitemaps_recuperados)

else:
    print("errado")