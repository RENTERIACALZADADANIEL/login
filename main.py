import flet as ft

def main(page: ft.Page):
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text("Inicio de sesión", size=28)

    def realizar_login(e):
        if user_input.value == "tester" and pass_input.value == "prueba":
            page.controls.clear()

    username = ft.TextField(
        label="Username",
        width=300,

    )
    forgot_password = ft.Button(
        content=ft.Text("¿Olvidaste la contraseña?", italic=True),
        on_click=lambda _: print("Recuperar contraseña clickeado")
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
                forgot_password,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    

    )

    page.add(card)

ft.app(target=main)