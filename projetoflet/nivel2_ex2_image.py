import flet as ft


def main(page: ft.Page):
    page.title = "Exibindo Imagens com ft.Image"
    page.assets_dir = "assets"
    page.spacing = 20

    img_url = ft.Image(
        src="https://flet.dev/img/flet-logo.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )

    img_local = ft.Image(
        src="assets/logo_ifnmg.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )

    page.add(
        ft.Text("Imagem carregada de uma URL da Web:", weight=ft.FontWeight.BOLD),
        img_url,
        ft.Text("Imagem carregada de um arquivo local (assets/logo_ifnmg.png):", weight=ft.FontWeight.BOLD),
        img_local,
    )

if __name__ == "__main__":
    ft.app(target=main)
