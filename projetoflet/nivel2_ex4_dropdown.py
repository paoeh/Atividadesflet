import flet as ft


def main(page: ft.Page):
    page.title = "Selecionando com Dropdown"
    page.spacing = 20

    cursos = [
        ft.dropdown.Option("Técnico em Informática"),
        ft.dropdown.Option("Técnico em Edificações"),
        ft.dropdown.Option("Técnico em Meio Ambiente"),
    ]
    dd_curso = ft.Dropdown(label="Por favor, selecione seu curso:", options=cursos)
    saida = ft.Text("Você selecionou: (nada)")

    def on_curso_change(e):
        saida.value = f"Você selecionou: {dd_curso.value}"
        page.update()

    dd_curso.on_change = on_curso_change

    estados = {
        "MG": ["Diamantina", "Belo Horizonte", "Montes Claros"],
        "SP": ["São Paulo", "Campinas", "Santos"],
        "RJ": ["Rio de Janeiro", "Niterói", "Petrópolis"],
    }

    dd_estado = ft.Dropdown(label="Estado", options=[ft.dropdown.Option(k) for k in estados.keys()])
    dd_cidade = ft.Dropdown(label="Cidade", options=[], disabled=True)

    def on_estado_change(e):
        selecionado = dd_estado.value
        dd_cidade.options = [ft.dropdown.Option(c) for c in estados.get(selecionado, [])]
        dd_cidade.disabled = False if dd_cidade.options else True
        dd_cidade.value = None
        page.update()

    dd_estado.on_change = on_estado_change

    page.add(dd_curso, saida, ft.Divider(), ft.Text("Desafio: Estado e Cidade"), dd_estado, dd_cidade)

if __name__ == "__main__":
    ft.app(target=main)
