import flet as ft
from services.api_client import APIClient
from utils.utils import show_error
import json

class LoginView(ft.View):
    def __init__(self, page: ft.Page, show_register, login_success):
        super().__init__()
        self.page = page
        self.show_register = show_register
        self.login_success = login_success
        self.api_client = APIClient()

        self.email_input = ft.TextField(label="E-mail", width=300)
        self.password_input = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=300)

        self.controls = [
            ft.Container(
                content=ft.Container(
                    width=300,
                    content=ft.Column(
                        [
                            ft.Text("Login", size=24, weight=ft.FontWeight.BOLD),
                            self.email_input,
                            self.password_input,
                            ft.ElevatedButton("Entrar", on_click=self.login, width=300),
                            ft.TextButton("Não tem uma conta? Cadastre-se", on_click=lambda _: self.show_register()),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    )
                ),
                alignment=ft.alignment.center,
                expand=True
            ),
        ]

    def login(self, e):
        email = self.email_input.value
        password = self.password_input.value

        try:
            response = self.api_client.login(email, password)
            print(f"Response from API: {response}")

            # Verifique se os dados do usuário estão presentes
            if "user" in response:
                user = response["user"]
                print(f"Login successful. User: {user}")
                self.login_success(user)
                self.page.snack_bar = ft.SnackBar(ft.Text("Login realizado com sucesso!"))
                self.page.snack_bar.open = True
                self.page.update()
            else:
                print(f"Login failed. Message: {response.get('message')}")
                show_error(self.page, "E-mail ou senha incorretos")
        except Exception as ex:
            print(f"Login exception: {str(ex)}")
            show_error(self.page, f"Erro ao tentar logar: {str(ex)}")

