import flet as ft
from components.primary_button import PrimaryButton

class InitialView(ft.View):
    def __init__(self, page: ft.Page, show_login, show_register):
        super().__init__(page)
        self.page = page
        self.show_login = show_login
        self.show_register = show_register

    def build(self):


        description = ft.Text("Bem-vindo ao NoteX", size=20, weight=ft.FontWeight.W_500)


        button = ft.ElevatedButton(
                    on_click=lambda _: self.show_login(),
                    width=330,
                    height=80,
                    style=ft.ButtonStyle(
                        color="#383838",
                        bgcolor="#A7E100",
                        shape=ft.RoundedRectangleBorder(radius=30),
                        elevation=0
                    ),
                    content=ft.Container(
                        content=ft.Row(
                            [
                                ft.Text("COMEÇAR", size=25, weight=ft.FontWeight.W_500),
                                ft.Container(
                                    content=ft.Icon(ft.icons.ARROW_OUTWARD, color=ft.colors.WHITE, size=50),
                                    alignment=ft.alignment.center,
                                    width=62,
                                    height=62,
                                    bgcolor="#1A2300",
                                    border_radius=ft.border_radius.all(100),
                                    margin=ft.margin.only(right=-15)
                                ),
                                
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            
                        )
                    )
                )

        return ft.Container(
            padding=ft.padding.all(20),
            content=ft.Column(
                [
                    description,
                    ft.Container(expand=True),
                    button,
                

                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )   ,
            alignment=ft.alignment.center,
            expand=True
        )