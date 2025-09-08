import tkinter as tk
from app.db import add_user, init_db
from app.pages.login_page import LoginPage
from app.pages.user_management_page import UserManagementPage
from app.pages.book_management_page import BookManagementPage
from app.config import APP_TITLE, WINDOW_SIZE


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry(WINDOW_SIZE)
        self.resizable(False, False)
        self.configure(bg="white")

        init_db()
        add_user("admin@gmail.com", "Admin", "User", "1234")

        self.current_frame = None
        self.show_frame(UserManagementPage)

    def show_frame(self, page_class):
        if self.current_frame is not None:
            self.current_frame.destroy()

        frame = page_class(self, self)
        frame.pack(fill="both", expand=True)

        self.current_frame = frame

        self.update_idletasks()
        w = frame.winfo_reqwidth()
        h = frame.winfo_reqheight()
        self.geometry(f"{w}x{h}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
