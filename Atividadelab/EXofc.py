
import flet as ft

def main(page: ft.Page):
    page.title = "Criar Conta"
    page.bgcolor = ft.Colors.GREY_100
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 20

    avatar = ft.CircleAvatar(
        content=ft.Image(
            src="https://pbs.twimg.com/media/E41OKDOWQAUgpZr.jpg:large",
            width=80, height=80, fit=ft.ImageFit.COVER
        ),
        radius=50,
    )


    email = ft.TextField(
        label="Email",
        prefix_icon=ft.Icons.EMAIL_OUTLINED,
        border_radius=8,
        width=280,
    )

    username = ft.TextField(
        label="Username",
        prefix_icon=ft.Icons.PERSON_OUTLINE,
        border_radius=8,
        width=280,
    )

    senha = ft.TextField(
        label="Senha",
        prefix_icon=ft.Icons.KEY_OUTLINED,
        password=True,
        can_reveal_password=True,
        border_radius=8,
        width=280,
    )

    confirmar = ft.TextField(
        label="Confirmar Senha",
        prefix_icon=ft.Icons.KEY_OUTLINED,
        password=True,
        can_reveal_password=True,
        border_radius=8,
        width=280,
    )


    def registrar_click(e):
        if not email.value or not username.value or not senha.value or not confirmar.value:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos."), open=True)
            page.update()
            return
        if senha.value != confirmar.value:
            page.snack_bar = ft.SnackBar(ft.Text("As senhas não conferem."), open=True)
            page.update()
            return

        page.snack_bar = ft.SnackBar(ft.Text("Conta criada com sucesso!"), open=True)
        page.update()


    registrar_btn = ft.ElevatedButton(
        "Registrar",
        width=280,
        height=45,
        bgcolor=ft.Colors.INDIGO,
        color=ft.Colors.WHITE,
        on_click=registrar_click
    )

    rodape = ft.Row(
        [
            ft.Text("Já tenho uma conta  "),
            ft.TextButton(
                "Entrar",
                on_click=lambda e: page.launch_url("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&dsh=S991115218%3A1755265406683177&ec=asw-gmail-globalnav-signin&flowEntry=AccountChooser&flowName=GlifWebSignIn&service=mail"),
                style=ft.ButtonStyle(color=ft.Colors.INDIGO),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )


    card = ft.Container(
        width=340,
        padding=20,
        bgcolor=ft.Colors.WHITE,
        border_radius=12,
        content=ft.Column(
            [
                ft.Text("Criar Conta!", size=24, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.Text(
                    "Descubra as melhores novidades\nCriando uma conta conosco",
                    size=12,
                    text_align=ft.TextAlign.CENTER,
                ),
                avatar,
                email,
                username,
                senha,
                confirmar,
                registrar_btn,
                rodape,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
    )

    page.add(card)

if __name__ == "__main__":
    ft.app(target=main)
