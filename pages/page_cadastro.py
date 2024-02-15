
import flet as ft

def main(page):
    first_name = ft.TextField(label="Cliente", autofocus=True)
    last_name = ft.TextField(label="CB")
    sitemap = ft.TextField(label="Sitemap.xml")
    greetings = ft.Column()

    def btn_click(e):
        greetings.controls.append(ft.Text(f"cadastro realizado com sucesso!, {first_name.value} {last_name.value} {sitemap.value}!"))
        first_name.value = ""
        last_name.value = ""
        sitemap.value = ""
        page.update()
        first_name.focus()

    page.add(
        first_name,
        last_name,
        sitemap,
        ft.ElevatedButton("Cadastrar Cliente", on_click=btn_click),
        greetings,
    )
ft.app(target=main)