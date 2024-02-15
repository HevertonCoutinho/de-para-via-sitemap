import flet as ft

def main(pagina: ft.Page):
    pagina.title = "Ferramenta de DE/PARA"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    def diminuir(e):
        caixa_texto.value = str(int(caixa_texto.value) -1)
        pagina.update()
        
    def somar(e):
        caixa_texto.value = str(int(caixa_texto.value) +1)
        pagina.update()
    
    #itens que queremos na pagina
    botao_menos = ft.IconButton(ft.icons.REMOVE, on_click=diminuir)
    caixa_texto = ft.TextField(value=0, width=100, text_align=ft.TextAlign.CENTER)
    botao_mais = ft.IconButton(ft.icons.ADD, on_click=somar)
    
    #Adicionar os itens na página
    pagina.add(
        
        ft.Row([botao_menos, botao_mais, caixa_texto], alignment=ft.MainAxisAlignment.CENTER)
        
    )

ft.app(target=main)