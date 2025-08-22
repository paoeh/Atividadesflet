import flet as ft


def main(page: ft.Page):
    page.title = "Capturando Dados"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 20

    nome = ft.TextField(label="Qual é o seu nome?")
    sobrenome = ft.TextField(label="Qual é o seu sobrenome?")
    saida = ft.Text("Olá! (seu nome aparecerá aqui)!")

    def mostrar_click(e):
        completo = f"{nome.value.strip()} {sobrenome.value.strip()}".strip()
        saida.value = f"Olá, {completo}!" if completo else "Olá! Digite seu nome."
        page.update()

    botao = ft.ElevatedButton("MOSTRAR", on_click=mostrar_click)

    page.add(nome, sobrenome, botao, saida)

if __name__ == "__main__":
    ft.app(target=main)
