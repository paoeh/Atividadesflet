import flet as ft


def colored_box(texto, cor):
    return ft.Container(
        content=ft.Text(texto, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
        bgcolor=cor,
        width=150,
        height=50,
        alignment=ft.alignment.center,
        border_radius=8,
    )

def main(page: ft.Page):
    page.title = "Organizando com Colunas e Linhas"
    page.scroll = ft.ScrollMode.AUTO

    coluna = ft.Column(
        [colored_box("Item A", ft.Colors.BLUE), colored_box("Item B", ft.Colors.GREEN), colored_box("Item C", ft.Colors.AMBER)],
        spacing=10,
    )

    linha = ft.Row(
        [colored_box("Item 1", ft.Colors.PURPLE), colored_box("Item 2", ft.Colors.TEAL), colored_box("Item 3", ft.Colors.RED)],
        spacing=10,
        wrap=True,
    )

    grade_2x2 = ft.Column(
        [
            ft.Row([colored_box("G1", ft.Colors.INDIGO), colored_box("G2", ft.Colors.BROWN)], spacing=10),
            ft.Row([colored_box("G3", ft.Colors.DEEP_ORANGE), colored_box("G4", ft.Colors.CYAN)], spacing=10),
        ],
        spacing=10,
    )

    page.add(
        ft.Text("Itens Organizados em uma Coluna:", size=20, weight=ft.FontWeight.BOLD),
        coluna,
        ft.Divider(),
        ft.Text("Itens Organizados em uma Linha:", size=20, weight=ft.FontWeight.BOLD),
        linha,
        ft.Divider(),
        ft.Text("Desafio: Grade 2x2", size=20, weight=ft.FontWeight.BOLD),
        grade_2x2,
    )

if __name__ == "__main__":
    ft.app(target=main)
