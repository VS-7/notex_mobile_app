import flet as ft
from services.api_client import APIClient
from utils.utils import show_error
from components.back_button import BackButton
from components.primary_input import PrimaryInput
from components.primary_button import PrimaryButton

class LoginView(ft.View):
    def __init__(self, page: ft.Page, show_initial, show_register, login_success):
        super().__init__()
        self.page = page
        self.show_register = show_register 
        self.show_initial = show_initial
        self.login_success = login_success
        self.api_client = APIClient()

        self.email_input = PrimaryInput(label="Insira seu e-mail")
        self.password_input = PrimaryInput(label="Insira sua senha", password=True, can_reveal_password=True)

        self.controls = [
            ft.Container(
                padding=ft.padding.all(20),
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                controls=[
                                    BackButton(on_click=lambda _: self.show_initial()),
                                ]
                            ),
                            ft.Container(expand=True),
                            ft.Text("Entrar", size=40, weight=ft.FontWeight.BOLD),
                            
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Text("Se Precisar De Algum Suporte", weight=ft.FontWeight.W_400),
                                    ft.TextButton("Clique Aqui", on_click=lambda _: self.show_register()),
                                ]
                            ),
                            self.email_input,
                            self.password_input,
                             ft.Container(expand=True),
                            PrimaryButton("Entrar", on_click=self.login),
                            ft.TextButton("Não Possui Uma Conta? Cadastre-se", on_click=lambda _: self.show_register()),
                            ft.Container(expand=True),
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

