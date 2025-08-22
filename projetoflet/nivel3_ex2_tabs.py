import flet as ft


def main(page: ft.Page):
    page.title = "Navegação por Abas (ft.Tabs)"

    tab_perfil = ft.Tab(
        text="Perfil",
        content=ft.Column([
            ft.Text("Nome: Aluno do IFNMG"),
            ft.Text("Curso: Técnico em Informática"),
        ], spacing=8),
    )

    tab_contato = ft.Tab(
        text="Contato",
        content=ft.Column([
            ft.Text("E-mail: aluno@ifnmg.edu.br"),
            ft.Text("Telefone: (38) 0000-0000"),
        ], spacing=8),
    )

    tab_fotos = ft.Tab(
        text="Fotos",
        content=ft.Column([
            ft.Text("Aqui poderiam estar suas fotos..."),
            ft.Icon(ft.Icons.IMAGE),
        ], spacing=8),
    )

    tabs = ft.Tabs(tabs=[tab_perfil, tab_contato, tab_fotos], expand=1)
    page.add(tabs)

if __name__ == "__main__":
    ft.app(target=main)
