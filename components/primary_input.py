import flet as ft

class PrimaryInput(ft.TextField):
    def __init__(self, label: str, password: bool = False, can_reveal_password: bool = False):
        super().__init__()
        self.hint_text = label
        self.password = password
        self.can_reveal_password = can_reveal_password
        self.color = "#383838"
        self.border_radius = ft.border_radius.all(30)
        self.height = 80
        self.width = 330
        self.content_padding = ft.padding.all(30)
        
        # Adicionando cores para estados diferentes
        self.focused_border_color = "#383838"  # Cor quando focado
        self.disabled_color = "#383838"  # Cor quando desabilitado
        
    def on_focus(self, e):
        if not self.disabled:
            self.border_color = self.focused_border_color
        self.update()
    
    def on_blur(self, e):
        self.border_color = None
        self.update()

