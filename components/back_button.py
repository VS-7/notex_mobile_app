import flet as ft

class BackButton(ft.IconButton):
    def __init__(self, on_click):
        super().__init__(icon=ft.icons.ARROW_BACK_IOS_NEW_OUTLINED, on_click=on_click, icon_color="#383838")
        self.width = 40
        self.height = 40
        self.style = ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.GREY_300,
            shape=ft.RoundedRectangleBorder(radius=30),
            elevation=0)