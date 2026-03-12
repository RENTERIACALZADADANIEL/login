import flet as ft

def main(page: ft.Page):
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text("Inicio de sesión", size=28)

    username = ft.TextField(
        label="Username",
        width=300,

    )

    password = ft.TextField(
        label="Password",
        password=True,
        can_reveal_password=True,
        width=300,
    
    )



    login_button = ft.Button(
        content=ft.Text("Login", size=16),
        width=300,
        height=45
    )

    card = ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                username,
                password,
                login_button,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    

    )

    page.add(card)

ft.app(target=main)