import flet as ft


def linha_icone(icone, texto):
    return ft.Row([ft.Icon(icone), ft.Text(texto)], alignment=ft.MainAxisAlignment.START)

def main(page: ft.Page):
    page.title = "Usando Ícones"
    page.spacing = 15

    favorito = ft.IconButton(icon=ft.Icons.FAVORITE_BORDER, selected_icon=ft.Icons.FAVORITE, selected=False, tooltip="Curtir")

    def toggle_like(e):
        favorito.selected = not favorito.selected
        page.update()

    favorito.on_click = toggle_like

    page.add(
        linha_icone(ft.Icons.HOME, "Página Inicial"),
        linha_icone(ft.Icons.SETTINGS, "Configurações"),
        linha_icone(ft.Icons.LOGOUT, "Sair"),
        ft.Divider(),
        ft.Text("Desafio: Botão de like (IconButton):"),
        favorito,
    )

if __name__ == "__main__":
    ft.app(target=main)
