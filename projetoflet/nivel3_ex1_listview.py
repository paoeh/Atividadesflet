import flet as ft


def main(page: ft.Page):
    page.title = "Lista de Tarefas com ListView"
    page.padding = 20
    page.spacing = 10

    entrada = ft.TextField(hint_text="Nova tarefa...", expand=True)
    lista = ft.ListView(expand=True, spacing=10, padding=10, auto_scroll=True)

    def remover_tarefa(chk: ft.Checkbox, row: ft.Row):
        def _inner(e):
            lista.controls.remove(row)
            page.update()
        return _inner

    def adicionar(e):
        if not (texto := (entrada.value or "").strip()):
            return
        chk = ft.Checkbox(label=texto, value=False)
        trash = ft.IconButton(icon=ft.Icons.DELETE, tooltip="Remover")
        row = ft.Row([chk, trash], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        trash.on_click = remover_tarefa(chk, row)
        lista.controls.append(row)
        entrada.value = ""
        page.update()

    add_btn = ft.ElevatedButton("Adic.", on_click=adicionar)

    page.add(ft.Row([entrada, add_btn]), ft.Divider(), lista)

if __name__ == "__main__":
    ft.app(target=main)
