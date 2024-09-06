import flet as ft

def show_error(page, message):
    page.snack_bar = ft.SnackBar(ft.Text(message))
    page.snack_bar.open = True
    page.update()

def go_back(page: ft.Page):
    if len(page.views) > 1:
        page.views.pop()
        page.update()

def apply_shadow(e):
    if e.control.shadow:
        e.control.shadow = None
    else:
        e.control.shadow = ft.BoxShadow(
            blur_radius=20, 
            color=e.control.bgcolor, 
            blur_style=ft.ShadowBlurStyle.OUTER
        )
    e.control.update()