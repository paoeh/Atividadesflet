import flet as ft

def main(page: ft.Page):

    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#FFFFFF"
    page.padding = 0
    page.spacing = 0
    

    def toggle_password_visibility(e):
        password_field.password = not password_field.password
        toggle_icon.icon = (
            ft.Icons.VISIBILITY_OFF if password_field.password else ft.Icons.VISIBILITY
        )
        page.update()


    top_image = ft.Container(
        content=ft.Image(
            src="https://www.enfoquems.com.br/wp-content/uploads/2020/09/corinthians_p000Pmj_widexl.jpeg",
            width=100,
            height=50,
            fit=ft.ImageFit.COVER,
        ),
        width=400,
        height=150,
        border_radius=ft.border_radius.only(bottom_left=20, bottom_right=20),
        margin=ft.margin.only(bottom=20)
    )


    form_container = ft.Container(
        width=400,
        padding=40,
        content=ft.Column(
            [

                ft.Container(
                    content=ft.Text(
                        "LOGIN",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLACK87
                    ),
                    padding=ft.padding.only(bottom=40),
                    alignment=ft.alignment.center
                ),
                

                ft.Container(
                    content=ft.Text(
                        "E-mail",
                        size=16,
                        color=ft.Colors.BLACK87,
                        weight=ft.FontWeight.W_500
                    ),
                    padding=ft.padding.only(bottom=10),
                    alignment=ft.alignment.center_left
                ),
                

                ft.Container(
                    content=ft.TextField(
                        value="breno@breno.com",
                        width=400,
                        height=50,
                        border_radius=6,
                        bgcolor=ft.Colors.WHITE,
                        border_color=ft.Colors.GREY_400,
                        content_padding=15,
                        text_size=16,
                        cursor_color=ft.Colors.BLUE_700,
                        focused_border_color=ft.Colors.BLUE_700,
                    ),
                    padding=ft.padding.only(bottom=25)
                ),
                

                ft.Container(
                    content=ft.Text(
                        "Senha",
                        size=16,
                        color=ft.Colors.BLACK87,
                        weight=ft.FontWeight.W_500
                    ),
                    padding=ft.padding.only(bottom=10),
                    alignment=ft.alignment.center_left
                ),
                

                ft.Container(
                    content=ft.TextField(
                        value="123456",
                        password=True,
                        can_reveal_password=True,
                        width=400,
                        height=50,
                        border_radius=6,
                        bgcolor=ft.Colors.WHITE,
                        border_color=ft.Colors.GREY_400,
                        content_padding=15,
                        text_size=16,
                        cursor_color=ft.Colors.BLUE_700,
                        focused_border_color=ft.Colors.BLUE_700,
                    ),
                    padding=ft.padding.only(bottom=30)
                ),
                

                ft.Container(
                    content=ft.Row(
                        [
                            ft.Container(expand=True, height=1, bgcolor=ft.Colors.GREY_300),
                            ft.Text(" ou ", size=14, color=ft.Colors.GREY_600),
                            ft.Container(expand=True, height=1, bgcolor=ft.Colors.GREY_300),
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    width=400,
                    padding=ft.padding.only(bottom=30),
                ),
                

                ft.Container(
                    content=ft.ElevatedButton(
                        content=ft.Row([
                            ft.Image(
                                src="https://cdn-icons-png.flaticon.com/512/2991/2991148.png", 
                                width=20, 
                                height=20
                            ),
                            ft.Text("Logar com o Google", size=16, color=ft.Colors.BLACK87)
                        ], 
                        alignment=ft.MainAxisAlignment.CENTER, 
                        spacing=10),
                        width=400,
                        height=50,
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.WHITE,
                            color=ft.Colors.BLACK87,
                            side=ft.BorderSide(1, ft.Colors.GREY_400),
                            shape=ft.RoundedRectangleBorder(radius=6),
                        )
                    ),
                    padding=ft.padding.only(bottom=15)
                ),
                

                ft.Container(
                    content=ft.ElevatedButton(
                        content=ft.Row([
                            ft.Image(
                                src="https://cdn-icons-png.flaticon.com/512/0/747.png", 
                                width=20, 
                                height=20,
                                color=ft.Colors.BLACK
                            ),
                            ft.Text("Logar com a Apple", size=16, color=ft.Colors.BLACK87)
                        ], 
                        alignment=ft.MainAxisAlignment.CENTER, 
                        spacing=10),
                        width=400,
                        height=50,
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.WHITE,
                            color=ft.Colors.BLACK87,
                            side=ft.BorderSide(1, ft.Colors.GREY_400),
                            shape=ft.RoundedRectangleBorder(radius=6),
                        )
                    ),
                    padding=ft.padding.only(bottom=30)
                ),
                

                ft.Container(
                    content=ft.ElevatedButton(
                        text="Fazer Login",
                        width=400,
                        height=50,
                        style=ft.ButtonStyle(
                            bgcolor=ft.Colors.BLUE_700,
                            color=ft.Colors.WHITE,
                            shape=ft.RoundedRectangleBorder(radius=6),
                        )
                    ),
                    padding=ft.padding.only(bottom=30)
                ),
                

                ft.Container(
                    content=ft.TextButton(
                        text="Crie sua conta com e-mail aqui",
                        style=ft.ButtonStyle(color=ft.Colors.BLUE_700)
                    ),
                    alignment=ft.alignment.center
                ),
            ],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    
    page.add(
        ft.Column(
            [
                top_image,
                form_container
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO
        )
    )

ft.app(target=main)