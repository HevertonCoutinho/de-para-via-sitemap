import flet as ft

import flet as ft

def main(page: ft.Page):
    page.title = "Ferramenta de DE/PARA"
    page.add(
        ft.DataTable(
            width=700,
            bgcolor="dark grey",
            border=ft.border.all(2, "orange"),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(3, "blue"),
            horizontal_lines=ft.border.BorderSide(1, "orange"),
            sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=100,
            data_row_color={"hovered": "0x30FF0000"},
            show_checkbox_column=True,
            divider_thickness=0,
            column_spacing=200,
            columns=[
                ft.DataColumn(
                    ft.Text("Cliente"),
                    on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                ),
                ft.DataColumn(
                    ft.Text("CB"),
                    tooltip="Este é o código do cliente",
                    numeric=True,
                    on_sort=lambda e: print(f"{e.column_index}, {e.ascending}"),
                ),
            ],
            rows=[
                ft.DataRow(
                    [ft.DataCell(ft.Text("CARE")), ft.DataCell(ft.Text("496"))],
                    selected=True,
                    on_select_changed=lambda e: print(f"row select changed: {e.data}"),
                ),
                ft.DataRow([ft.DataCell(ft.Text("LOJAS REDE")), ft.DataCell(ft.Text("535"))]),
            ],
        ),
    )
    page.add(
        ft.ElevatedButton(text="Importar lista 404"),
        ft.ElevatedButton("Realizar DE/PARA", disabled=True),
    )

ft.app(target=main)