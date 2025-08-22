import flet as ft


def main(page: ft.Page):
    page.title = "Minha Primeira Tela Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    t1 = ft.Text(
        "Bem-vindo ao IFNMG Diamantina!",
        size=28,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_700,
        text_align=ft.TextAlign.CENTER,
    )
    t2 = ft.Text(
        "Você está aprendendo a usar o Flet para criar interfaces gráficas com Python.",
        size=16,
        color=ft.Colors.BLACK87,
    )
    t3 = ft.Text(
        "Este é um componente de Texto (ft.Text).",
        size=16,
        color=ft.Colors.GREY_800,
        italic=True,
    )

    page.add(t1, t2, t3)

if __name__ == "__main__":
    ft.app(target=main)
