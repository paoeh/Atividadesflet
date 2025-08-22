import flet as ft


def main(page: ft.Page):
    page.title = "App com Navegação Principal"
    page.padding = 20

    conteudo = ft.Column(spacing=10)

    def render_home():
        conteudo.controls = [ft.Text("Bem-vindo à Página Inicial!", size=20, weight=ft.FontWeight.BOLD)]
    def render_search():
        conteudo.controls = [ft.Text("Pesquisar..."), ft.TextField(hint_text="Digite para buscar...")]
    def render_settings():
        conteudo.controls = [ft.Text("Configurações"), ft.Switch(label="Tema escuro"), ft.Switch(label="Notificações", value=True)]

    renders = {0: render_home, 1: render_search, 2: render_settings}

    def on_change(e):
        idx = page.navigation_bar.selected_index
        renders.get(idx, render_home)()
        page.update()

    page.navigation_rail = ft.NavigationRail(
         destinations=[
             ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Home"),
             ft.NavigationRailDestination(icon=ft.Icons.SEARCH, label="Pesquisa"),
             ft.NavigationRailDestination(icon=ft.Icons.SETTINGS, label="Config"),
         ],
         selected_index=0,
         on_change=lambda e: on_change(e),
     )

    render_home()
    page.add(conteudo)



if __name__ == "__main__":
    ft.app(target=main)