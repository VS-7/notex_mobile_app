import flet as ft

class PrimaryButton(ft.ElevatedButton):
    def __init__(self, text, on_click, color="#383838", bgcolor="#A7E100"):
        super().__init__(text, on_click=on_click)
        self.width = 330
        self.height = 80
        self.style = ft.ButtonStyle(
            color=color,
            bgcolor=bgcolor,
            shape=ft.RoundedRectangleBorder(radius=30),
            elevation=0
        )
        self.content = ft.Text(text, size=20, weight=ft.FontWeight.BOLD)