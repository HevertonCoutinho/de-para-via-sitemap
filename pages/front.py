import flet as ft
from flet import theme

def main(page):
    
    #page.theme = theme.Theme(color_scheme_seed='green')
    #page.update()
    
    page.title = "Ferramenta de DE/PARA"
    #Card de cadastro
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("Cadastro de cliente"),
                            subtitle=ft.Text(
                                "Cadastre seus clientes para conseguir utilizar esta ferramenta."
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton("Realizar Cadastro"), ft.TextButton("Atualizar Cadastro")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
    )
    #Fim card cadastro
    
    #Card de cadastro
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("Base de dados"),
                            subtitle=ft.Text(
                                "Verifique todos os clientes cadastrados em nossa base de dados."
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton("Acessar base de dados")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
    )
    #Fim card cadastro
    
    page.add(
        ft.FilledButton(text="Realizar DE/PARA"),
        ft.FilledButton(text="Sair"),
    )

ft.app(target=main)


    