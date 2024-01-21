import produto
import categoria
import json
import sqlite3
import os

# Função para obter sitemap_urls a partir do banco de dados
def get_sitemap_urls(cb, cursor):
    cursor.execute("SELECT sitemap FROM cliente WHERE cb = ?", (cb,))
    result = cursor.fetchone()
    if result:
        sitemap_json = result[0]
        return json.loads(sitemap_json)
    else:
        return []

while True:
    escolha = int(input('1 - Rodar DE/PARA\n2 - Listar Clientes da base\n3 - Adicionar cliente\n4 - Atualizar cliente\n5 - Sair\n> '))

    resultado = None

    # Função para verificar se já existe um CB na tabela
    def verificar_cb_existente(cursor, cb):
        cursor.execute("SELECT COUNT(*) FROM cliente WHERE cb = ?", (cb,))
        quantidade = cursor.fetchone()[0]
        return quantidade > 0

    if escolha == 1:

        os.system('cls')

        cb = input("Informe o CB do cliente que deseja realizar o DE/PARA:\n")
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
        if verificar_cb_existente(cursor, cb):
            escolha_de_para = input('Que tipo de DE/PARA deseja realizar?\n1 - DE/PARA de Categoria\n2 - DE/PARA de produto\n')
            sitemap_urls = get_sitemap_urls(cb, cursor)
            
            if escolha_de_para == '1':
                categoria.main(sitemap_urls)
            elif escolha_de_para == '2':    
                produto.main(sitemap_urls)
            else:
                print('Escolha invalida')
        else:
            print('Cliente com CB {cb} não encontrado no banco de dados\n>')
        
        # Fecha a conexão
        conn.close()  

    elif escolha == 2:

        os.system('cls')

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

        # Consulta para obter os clientes e suas informações
        cursor.execute("SELECT cliente, cb FROM cliente")
        clientes = cursor.fetchall()

        if clientes:
            print("Lista de Clientes:\n")
            for cliente in clientes:
                print(f"Cliente: {cliente[0]}\nCB: {cliente[1]}\n")
        else:
            print("Não há clientes cadastrados.")

        # Fecha a conexão
        conn.close()
        
    elif escolha == 3:
        
        os.system('cls')

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
        
        # Verifique se já existe um cliente com o mesmo CB
        if verificar_cb_existente(cursor, cb):
            resposta = input(f"Já existe um cliente com o CB {cb}. Deseja continuar e substituir? (s/n): ").lower()
            if resposta != 's':
                print("Inserção cancelada.")
                conn.close()
                exit()
                
            # Se o usuário decidiu continuar, atualize a linha existente
            entrada_usuario = input('Insira a lista de sitemaps separados por vírgula:\n> ')
            sitemap = list(map(str.strip, entrada_usuario.split(',')))
            sitemaps_json = json.dumps(sitemap)
            cursor.execute("UPDATE cliente SET cliente = ?, sitemap = ? WHERE cb = ?", (cliente, sitemaps_json, cb))
            print("Cliente Atualizado")
        else:
            # Se não existir, insira uma nova linha       
            entrada_usuario = input('Insira a lista de sitemaps separados por vírgula:\n> ')
            sitemap = list(map(str.strip, entrada_usuario.split(',')))
            sitemaps_json = json.dumps(sitemap)
            cursor.execute("INSERT INTO cliente (cliente, cb, sitemap) VALUES (?, ?, ?)", (cliente, cb, sitemaps_json))
            print("Cliente Adicionado")

        conn.commit()

        cliente_nome = cliente
        cursor.execute("SELECT sitemap FROM cliente WHERE cliente = ?", (cliente_nome,))
        resultado = cursor.fetchone()
        
        # Fecha a conexão
        conn.close()

    elif escolha == 4:

        os.system('cls')

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
        
        #Add informações cliente atualizar
        cliente = str(input('Nome do cliente: '))
        cb = int(input('CB: '))
        entrada_usuario = input('Insira a lista de sitemaps separados por vírgula:\n> ')
        
        # Verifica se o cliente com o CB fornecido existe
        cursor.execute("SELECT * FROM cliente WHERE cb = ?", (cb,))
        existing_client = cursor.fetchone()
        
        if existing_client:
            #Condição que oferece opção de criar novo cliente ou cancelar o cadastro de novo cliente
            resposta_atualizar_cliente = input(f"Você esta prestes a alterar as informações de cadastro deste cliente, deseja continuar? s/n:\n")
            if resposta_atualizar_cliente == 'n':
                print('Atualização cancelada.')
            else: 
                #Atualiza Cliente
                existing_client = cursor.fetchone()
                sitemap = list(map(str.strip, entrada_usuario.split(',')))
                sitemaps_json = json.dumps(sitemap)
                cursor.execute("UPDATE cliente SET cliente = ?, sitemap = ? WHERE cb = ?", (cliente, sitemaps_json, cb))
                print("Cliente Atualizado")
        else:
            #Condição que oferece opção de criar novo cliente ou cancelar o cadastro de novo cliente
            resposta_atualizar_cliente = input(f"Não foi possível realizar a atualização (Motivo: CB informado não existe).\nDeseja cadastrar este cliente como Novo Cliente? s/n:\n")
            if resposta_atualizar_cliente != 's':
                print('Cadastramento Cancelado.')
            else:
                sitemap = list(map(str.strip, entrada_usuario.split(',')))
                sitemaps_json = json.dumps(sitemap)
                cursor.execute("INSERT INTO cliente (cliente, cb, sitemap) VALUES (?, ?, ?)", (cliente, cb, sitemaps_json))
                print("Cliente Adicionado")

        conn.commit()
        
        # Fecha a conexão
        conn.close()           

    elif escolha == 5:

        os.system('cls')

        print("Encerrando o programa. Até logo! \n")
        break

    else:

        os.system('cls')

        print('Opção invalida\n')