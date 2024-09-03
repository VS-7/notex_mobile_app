import flet as ft
from services.api_client import APIClient
from utils.utils import show_error

class RegisterView(ft.View):
    def __init__(self, page: ft.Page, show_login, register_success):
        super().__init__()
        self.page = page
        self.show_login = show_login
        self.register_success = register_success
        self.api_client = APIClient()

        self.name_input = ft.TextField(label="Nome", width=300)
        self.email_input = ft.TextField(label="E-mail", width=300)
        self.password_input = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=300)
        self.confirm_password_input = ft.TextField(label="Confirmar Senha", password=True, can_reveal_password=True, width=300)

        self.controls = [
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Cadastro", size=24, weight=ft.FontWeight.BOLD),
                        self.name_input,
                        self.email_input,
                        self.password_input,
                        self.confirm_password_input,
                        ft.ElevatedButton("Cadastrar", on_click=self.register, width=300),
                        ft.TextButton("Já tem uma conta? Faça login", on_click=lambda _: self.show_login()),
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