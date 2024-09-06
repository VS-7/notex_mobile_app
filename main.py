import flet as ft
from pages.login_view import LoginView
from pages.register_view import RegisterView
from pages.notes_view import NotesView
from pages.note_detail_view import NoteDetailView
from pages.initial_view import InitialView
from app_theme.app_theme import AppTheme
import json

class NoteXApp:
    def __init__(self):
        self.page = None
        self.current_user = None
        

    def main(self, page: ft.Page):
        self.page = page
        self.page.title = 'NoteX'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.check_login()
        

    def check_login(self):
        stored_user = self.page.client_storage.get("user")
        if stored_user:
            try:
                self.current_user = json.loads(stored_user)
                self.validate_stored_user()
            except:
                self.page.client_storage.remove("user")
                self.show_initial()
        else:
            self.show_initial()

    def validate_stored_user(self):
        if self.current_user and 'id' in self.current_user:
            self.show_notes()
        else:
            self.page.client_storage.remove("user")
            self.show_initial()



    def show_initial(self):
        self.page.views.clear()
        self.page.views.append(
            InitialView(self.page, self.show_login, self.show_register)
        )
        self.page.update()

    def show_login(self):
        self.page.views.clear()
        self.page.views.append(
            LoginView(self.page, self.show_initial, self.show_register, self.login_success)
        )
        self.page.update()

    def show_register(self):
        self.page.views.clear()
        self.page.views.append(
            RegisterView(self.page, self.show_initial, self.show_login, self.register_success)
        )
        self.page.update()

    def show_note_details(self, note=None):
        self.page.views.append(
            NoteDetailView(self.page, self.current_user, note, self.show_notes)
        )
        self.page.update()

    def login_success(self, user):
        self.current_user = user
        self.page.client_storage.set("user", json.dumps(user))
        self.show_notes()

    def show_notes(self):
        self.page.views.clear()
        notes_view = NotesView(self.page, self.current_user, self.show_note_details, self.logout)
        self.page.views.append(notes_view)
        self.page.update()

    def register_success(self):
        self.show_login()

    def logout(self, e=None):
        self.page.client_storage.remove("user")
        self.current_user = None
        self.show_login()

if __name__ == "__main__":
    app = NoteXApp()
    ft.app(target=app.main)
