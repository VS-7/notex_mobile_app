import flet as ft
from services.api_client import APIClient
from utils.utils import show_error

class NoteDetailView(ft.View):
    def __init__(self, page: ft.Page, current_user, note, show_notes):
        super().__init__()
        self.page = page
        self.current_user = current_user
        self.note = note
        self.show_notes = show_notes
        self.api_client = APIClient()

        self.title = ft.TextField(
            value=note['title'] if note else "",
            max_length=50,
            text_style=ft.TextStyle(size=30, weight=ft.FontWeight.BOLD),
            border=ft.InputBorder.UNDERLINE,
            hint_text='Qual será o título da sua nota?',
            hint_style=ft.TextStyle(italic=True),
            content_padding=ft.padding.only(bottom=20),
        )
        
        self.content = ft.TextField(
            value=note['content'] if note else "",
            multiline=True,
            min_lines=5,
            max_lines=15,
            hint_text='Escreva o conteúdo da sua nota...',
            border=ft.InputBorder.UNDERLINE,
        )

        self.color_input = ft.Dropdown(
            label="Selecione a cor do card",
            options=[
               ft.dropdown.Option("blue", "Azul"),
               ft.dropdown.Option("red", "Vermelho"),
               ft.dropdown.Option("green", "Verde"),
               ft.dropdown.Option("yellow", "Amarelo"),
               ft.dropdown.Option("purple", "Roxo"),
            ],
            value=note['color'] if note else "blue",
        )

        self.controls = [
            ft.Container(
                content=ft.Column(
                    [   
                        ft.Row(
                            [
                                ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda _: self.show_notes()),
                                
                            ]
                        ),
                        self.title,
                        self.content,
                        self.color_input,
                        ft.ElevatedButton("Salvar Anotação", on_click=self.save_note),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=20,
            )
        ]

    def save_note(self, e):
        new_note = {
            "title": self.title.value,
            "content": self.content.value,
            "color": self.color_input.value,
            "expand": 1,
            "user_id": self.current_user['id'],
        }
        
        try:
            if self.note:
                response = self.api_client.update_note(self.note["id"], new_note)
            else:
                response = self.api_client.create_note(new_note)
            
            if response.status == 200:
                self.show_notes()
            else:
                show_error(self.page, "Erro ao salvar a nota")
        except Exception as ex:
            show_error(self.page, "Erro ao salvar a nota: Verifique sua conexão")