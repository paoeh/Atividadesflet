import flet as ft


def main(page: ft.Page):
    page.title = "Estilizando com Container"
    page.padding = 20

    card = ft.Container(
        content=ft.Column([
            ft.Text("Card de Perfil", size=20, weight=ft.FontWeight.BOLD),
            ft.Text("Este é um texto dentro do card."),
        ], tight=True, spacing=8),
        bgcolor=ft.Colors.BLUE_GREY_100,
        padding=ft.padding.all(15),
        border_radius=ft.border_radius.all(12),
        margin=ft.margin.all(10),
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[ft.Colors.BLUE_GREY_100, ft.Colors.WHITE],
        ),
    )

    page.add(card, ft.Text("Este é um Container com cor de fundo, padding, margem e borda arredondadas."))

if __name__ == "__main__":
    ft.app(target=main)
