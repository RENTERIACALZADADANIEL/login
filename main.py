import flet as ft

def main(page: ft.Page):
    page.title = "Inicio de sesion"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def cambio_tab(e):
        indice = e.control.selected_index
        if indice == 0:
            cuerpo_texto.value = "Seccion: Explorar"
        elif indice == 1:
            cuerpo_texto.value = "Seccion: Search"
        elif indice == 2:
            cuerpo_texto.value = "Seccion: Settings"
        page.update()

    cuerpo_texto = ft.Text("has ingresado correctamente", size=30, weight="bold")

    def realizar_login(e):
        if username.value == "tester" and password.value == "prueba":
            page.controls.clear()

            page.navigation_bar = ft.NavigationBar(
                selected_index=0,
                on_change=cambio_tab,
                destinations=[
                    ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Explorar"),
                    ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="Search"),
                    ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Settings"),
                ]
            )

            page.add(
                ft.Container(
                    content=cuerpo_texto,
                    alignment=ft.Alignment.CENTER,
                    expand=True
                )
            )
            page.update()
        else:
            password.error_text = "Credenciales incorrectas"
            page.update()

    username = ft.TextField(label="Usuario", width=300)
    password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)

    login = ft.ElevatedButton("Iniciar Sesion", on_click=realizar_login, width=300)

    forgot_password = ft.TextButton(
        content=ft.Text("¿Olvidaste la contraseña?", italic=True),
        on_click=lambda _: print("Recuperar contraseña clickeado")
    )

    page.add(
        ft.Column(
            [
                ft.Text("Login de Usuario", size=25, weight="bold"),
                username,
                password,
                login,
                forgot_password
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.app(target=main)