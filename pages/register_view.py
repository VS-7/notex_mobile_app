import flet as ft
from services.api_client import APIClient
from utils.utils import show_error
from components.back_button import BackButton
from components.primary_input import PrimaryInput
from components.primary_button import PrimaryButton

class RegisterView(ft.View):
    def __init__(self, page: ft.Page, show_initial, show_login, register_success):
        super().__init__()
        self.page = page
        self.show_login = show_login
        self.show_initial = show_initial
        self.register_success = register_success
        self.api_client = APIClient()       

        self.name_input = PrimaryInput(label="Insira seu nome")
        self.email_input = PrimaryInput(label="Insira seu e-mail")
        self.password_input = PrimaryInput(label="Insira sua senha", password=True, can_reveal_password=True)
        self.confirm_password_input = PrimaryInput(label="Confirme sua senha", password=True, can_reveal_password=True)

        self.controls = [
            ft.Container(
                padding=ft.padding.all(20),
                content=ft.Column(
                    [   
                        ft.Row(
                            controls=[
                                BackButton(on_click=lambda _: self.show_initial()),
                            ]
                        ),
                        ft.Container(expand=True),
                        ft.Text("Cadastre-se", size=40, weight=ft.FontWeight.BOLD),
                        ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Text("Se Precisar De Algum Suporte", weight=ft.FontWeight.W_400),
                                    ft.TextButton("Clique Aqui", on_click=lambda _: self.show_register()),
                                ]
                            ),
                        self.name_input,
                        self.email_input,
                        self.password_input,
                        self.confirm_password_input,
                        ft.Container(expand=True),
                        PrimaryButton("Cadastrar", on_click=self.register),
                        ft.TextButton("Já tem uma conta? Faça login", on_click=lambda _: self.show_login()),
                        ft.Container(expand=True),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center,
                expand=True
            )
        ]

    def register(self, e):
        name = self.name_input.value
        email = self.email_input.value
        password = self.password_input.value
        confirm_password = self.confirm_password_input.value

        if password != confirm_password:
            show_error(self.page, "As senhas não coincidem")
            return

        try:
            response = self.api_client.register(name, email, password)
            if response.status == 200:
                self.register_success()
                self.page.snack_bar = ft.SnackBar(ft.Text("Cadastro realizado com sucesso! Faça login para continuar."))
                self.page.snack_bar.open = True
                self.page.update()
            else:
                show_error(self.page, "Erro ao cadastrar usuário")
        except Exception as ex:
            show_error(self.page, "Erro ao cadastrar usuário: Verifique sua conexão")