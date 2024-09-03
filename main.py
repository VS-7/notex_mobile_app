import flet as ft
from pages.login_view import LoginView
from pages.register_view import RegisterView
from pages.notes_view import NotesView
from pages.note_detail_view import NoteDetailView
import json

class NoteXApp:
    def __init__(self):
        self.page = None
        self.current_user = None

    def main(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.BLACK
        self.page.title = 'NoteX'
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.check_login()

    def check_login(self):
        # Try to get stored user data
        stored_user = self.page.client_storage.get("user")
        if stored_user:
            # If user data exists, try to validate it
            try:
                self.current_user = json.loads(stored_user)
                self.validate_stored_user()
            except:
                # If there's an error, clear the stored data and show login
                self.page.client_storage.remove("user")
                self.show_login()
        else:
            # If no stored user data, show login
            self.show_login()

    def validate_stored_user(self):
        # Here you would typically validate the stored user data with your backend
        # For this example, we'll just check if the user ID exists
        if self.current_user and 'id' in self.current_user:
            self.show_notes()
        else:
            self.page.client_storage.remove("user")
            self.show_login()

    def show_login(self):
        self.page.views.clear()
        self.page.views.append(
            LoginView(self.page, self.show_register, self.login_success)
        )
        self.page.update()

    def show_register(self):
        self.page.views.clear()
        self.page.views.append(
            RegisterView(self.page, self.show_login, self.register_success)
        )
        self.page.update()

    def show_note_details(self, note=None):
        self.page.views.append(
            NoteDetailView(self.page, self.current_user, note, self.show_notes)
        )
        self.page.update()

    def login_success(self, user):
        print("Login success called with user:", user)
        self.current_user = user
        self.page.client_storage.set("user", json.dumps(user))
        print("User data stored in client_storage")
        self.show_notes()

    def show_notes(self):
        print("Showing notes view")
        self.page.views.clear()
        notes_view = NotesView(self.page, self.current_user, self.show_note_details, self.logout)
        print("NotesView created")
        self.page.views.append(notes_view)
        print("NotesView appended to page views")
        self.page.update()
        print("Page updated")

    def register_success(self):
        self.show_login()

    def logout(self, e=None):
        self.page.client_storage.remove("user")
        self.current_user = None
        self.show_login()

if __name__ == "__main__":
    app = NoteXApp()
    ft.app(target=app.main)
