import flet as ft


def main(page: ft.Page):
    page.title = "Opções com Checkbox e Switch"
    page.spacing = 20

    termos = ft.Checkbox(label="Li e aceito os termos de uso.", value=False)
    novidades = ft.Checkbox(label="Desejo receber novidades por e-mail.", value=False, disabled=True)

    modo_noturno = ft.Switch(label="Modo Noturno", value=False)
    notificacoes = ft.Switch(label="Notificações", value=True)

    estado = ft.Text("Estado: Termos não aceitos. Modo Noturno OFF.")

    def atualizar_estado():
        estado.value = (
            f"Estado: {'Termos aceitos' if termos.value else 'Termos não aceitos'}. "
            f"Modo Noturno {'ON' if modo_noturno.value else 'OFF'}. "
            f"Notificações {'ON' if notificacoes.value else 'OFF'}."
        )
        page.update()

    def on_termos_change(e):
        novidades.disabled = not termos.value
        atualizar_estado()

    termos.on_change = on_termos_change
    novidades.on_change = lambda e: atualizar_estado()
    modo_noturno.on_change = lambda e: atualizar_estado()
    notificacoes.on_change = lambda e: atualizar_estado()

    page.add(termos, novidades, ft.Divider(), modo_noturno, notificacoes, ft.Divider(), estado)

if __name__ == "__main__":
    ft.app(target=main)
