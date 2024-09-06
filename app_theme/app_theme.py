import flet as ft

class AppTheme:
    # Cores principais
    PRIMARY = "#007AFF"
    SECONDARY = "#5856D6"
    BACKGROUND = "#FFFFFF"
    SURFACE = "#F2F2F7"
    
    # Cores de texto
    TEXT_PRIMARY = "#000000"
    TEXT_SECONDARY = "#8E8E93"
    
    # Cores de ação
    ERROR = "#FF3B30"
    SUCCESS = "#34C759"
    WARNING = "#FF9500"
    
    # Cores de estado
    DISABLED = "#C7C7CC"
    HOVER = "#E5E5EA"
    
    @classmethod
    def apply_to_page(cls, page: ft.Page):
        page.bgcolor = cls.BACKGROUND
        page.theme = ft.Theme(
            color_scheme=ft.ColorScheme(
                primary=cls.PRIMARY,
                secondary=cls.SECONDARY,
                background=cls.BACKGROUND,
                surface=cls.SURFACE,
                on_primary=cls.BACKGROUND,
                on_secondary=cls.BACKGROUND,
                on_surface=cls.TEXT_PRIMARY,
                error=cls.ERROR,
            ),
            visual_density=ft.ThemeVisualDensity.COMFORTABLE,
        )
        
    @classmethod
    def get_text_style(cls, size: int = 16, color: str = TEXT_PRIMARY, weight: str = "normal"):
        return ft.TextStyle(
            size=size,
            color=color,
            weight=weight,
        )
    
    @classmethod
    def get_button_style(cls):
        return ft.ButtonStyle(
            color={
                ft.MaterialState.HOVERED: cls.HOVER,
                ft.MaterialState.FOCUSED: cls.PRIMARY,
                ft.MaterialState.DEFAULT: cls.PRIMARY,
            },
            bgcolor={
                ft.MaterialState.HOVERED: cls.PRIMARY,
                ft.MaterialState.FOCUSED: cls.BACKGROUND,
                ft.MaterialState.DEFAULT: cls.BACKGROUND,
            },
        )