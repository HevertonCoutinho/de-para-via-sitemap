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


from get_sitemaps import get_sitemap_urls
import produto
import categoria

sitemap_urls = get_sitemap_urls()

categoria.main(sitemap_urls)
produto.main(sitemap_urls)
