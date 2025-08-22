import flet as ft


def main(page: ft.Page):
    page.title = "App Contador"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 25

    contador = {"valor": 0}

    display = ft.Text(str(contador["valor"]), size=48, weight=ft.FontWeight.BOLD)

    def atualizar():
        display.value = str(contador["valor"])
        page.update()

    def somar(e):
        contador["valor"] += 1
        atualizar()

    def subtrair(e):
        contador["valor"] -= 1
        atualizar()

    def zerar(e):
        contador["valor"] = 0
        atualizar()

    linha = ft.Row(
        controls=[
            ft.FilledButton("-1", on_click=subtrair),
            ft.OutlinedButton("+1", on_click=somar),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    page.add(display, linha, ft.ElevatedButton("Zerar", on_click=zerar))

if __name__ == "__main__":
    ft.app(target=main)
