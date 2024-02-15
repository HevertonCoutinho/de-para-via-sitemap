from time import sleep
import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    pb = ft.ProgressBar(width=400)

    page.add(
        ft.Text("Realizando Mapeamento de DE/PARA", style="headlineSmall", text_align=ft.TextAlign.CENTER),
        ft.Column([ ft.Text("Aguarde..."), pb], alignment=ft.MainAxisAlignment.CENTER)
    )

    for i in range(0, 101):
        pb.value = i * 0.01
        sleep(0.1)
        page.update()

ft.app(target=main)