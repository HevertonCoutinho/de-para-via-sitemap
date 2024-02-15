import flet as ft

def main(page: ft.Page):
    page.add(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Cliente")),
                ft.DataColumn(ft.Text("CB")),
                ft.DataColumn(ft.Text("Sitemap"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("CARE")),
                        ft.DataCell(ft.Text("496")),
                        ft.DataCell(ft.Text("https://carenb.com/sitem....")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Chocolat Du Jour")),
                        ft.DataCell(ft.Text("500")),
                        ft.DataCell(ft.Text("https://chocolatdujour.com/sitem....")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Edeltec")),
                        ft.DataCell(ft.Text("527")),
                        ft.DataCell(ft.Text("https://edeltec.com/sitem....")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Elastobor")),
                        ft.DataCell(ft.Text("535")),
                        ft.DataCell(ft.Text("https://elastobor.com/sitem....")),
                    ],
                ),
            ],
        ),
    )

ft.app(target=main)