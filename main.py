# import kivy
# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button

# class layout(GridLayout):

#     def __init__(self, **kwargs):
#         super(layout, self).__init__(**kwargs)

#         self.cols = 2

#         self.add_widget(Label(text = "Cliente: "))

#         self.name = TextInput(multiline=False)
#         self.add_widget(self.name)

        
#         self.add_widget(Label(text = "CB: "))

#         self.name = TextInput(multiline=False)
#         self.add_widget(self.name)

        
#         self.add_widget(Label(text = "Sitemap: "))

#         self.name = TextInput(multiline=False)
#         self.add_widget(self.name)

#         self.submit = Button(text = "Enviar", font_size = 32)
#         self.add_widget(self.submit)

# class Myapp(App):
#     def build (self):
#         return layout()


# if __name__ == '__main__':
#     Myapp().run()

import produto
import categoria
import json
import sqlite3


# Função para obter sitemap_urls, inicialmente vazia
def get_sitemap_urls():
    return []

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

# Obtenha as URLs do sitemap usando a função atualizada
sitemap_urls = get_sitemap_urls()
categoria.main(sitemap_urls)
produto.main(sitemap_urls)