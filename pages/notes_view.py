import flet as ft
from services.api_client import APIClient
from utils.utils import show_error, apply_shadow

class NotesView(ft.View):
    def __init__(self, page: ft.Page, current_user, show_note_details, logout):
        super().__init__()
        self.page = page
        self.current_user = current_user
        self.show_note_details = show_note_details
        self.logout = logout
        self.api_client = APIClient()

        self.notes_grid = self.create_notes_grid()

        self.controls = [
            ft.Container(
                expand=True,
                padding=ft.padding.all(30),
                content=ft.Column(
                    spacing=50,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Text(value='NoteX', style=ft.TextThemeStyle.DISPLAY_LARGE),
                                 ft.ElevatedButton(
                                    "Sair",
                                    icon=ft.icons.LOGOUT,
                                    on_click=self.logout,
                                    style=ft.ButtonStyle(
                                        color=ft.colors.WHITE,
                                        bgcolor=ft.colors.BLACK,
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                    ),
                                ),
                            ]
                        ),
                        ft.Column(
                            expand=True,
                            scroll=ft.ScrollMode.HIDDEN,
                            controls=[self.notes_grid]
                        )
                    ]
                )
            )
        ]

        self.floating_action_button = ft.FloatingActionButton(
            icon=ft.icons.ADD,
            shape=ft.CircleBorder(),
            tooltip='Adicionar uma nota',
            on_click=lambda _: self.show_note_details(),
            bgcolor=ft.colors.BLUE_400,
        )

    def create_notes_grid(self):
        notes = self.api_client.get_notes(self.current_user["id"])
        return ft.ResponsiveRow(
            columns=2,
            controls=[self.create_note_card(note) for note in notes]
        )

    def create_note_card(self, note):
        return ft.Container(
            col=2 if note['expand'] else 1,
            bgcolor=note['color'],
            padding=ft.padding.all(20),
            border_radius=ft.border_radius.all(10),
            shadow=None,
            content=ft.Column(
                controls=[
                    ft.Text(
                        value=note['title'],
                        style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                        max_lines=3,
                        overflow=ft.TextOverflow.ELLIPSIS,
                    ),
                    ft.Text(
                        value=note['date'],
                        style=ft.TextThemeStyle.BODY_MEDIUM,
                    ),
                    ft.ElevatedButton(
                        text="Excluir",
                        icon=ft.icons.DELETE,
                        on_click=lambda _: self.delete_note(note['id']),
                        style=ft.ButtonStyle(
                            color=ft.colors.WHITE,
                            bgcolor=ft.colors.BLACK,
                            shape=ft.RoundedRectangleBorder(radius=20),
                        ),
                    )
                ]
            ),
            data=note['id'],
            on_hover=apply_shadow,
            on_click=lambda _: self.show_note_details(note),
        )

    def delete_note(self, note_id):
        try:
            response = self.api_client.delete_note(note_id)
            if response.status == 200:
                self.refresh_notes()
            else:
                show_error(self.page, "Erro ao excluir a nota")
        except Exception as ex:
            show_error(self.page, "Erro ao excluir a nota: Verifique sua conexão")

    def refresh_notes(self):
        self.notes_grid = self.create_notes_grid()
        self.controls[0].content.controls[2].controls[0] = self.notes_grid
        self.page.update()