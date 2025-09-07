import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white", width=600, height=400)
        self.controller = controller
        self.pack_propagate(False)

        tk.Label(self, text="Bienvenue sur l'application!", font=('Microsoft YaHei UI Light', 23, 'bold')).pack(pady=20)
        tk.Button(self, text="Gérer les utilisateurs", width=20, command=self.go_user_management).pack(pady=10)
        tk.Button(self, text="Gérer les livres", width=20, command=self.go_book_management).pack(pady=10)
        tk.Button(self, text="Déconnexion", width=20, command=self.go_login).pack(pady=10)

    def go_user_management(self):
        from app.pages.user_management_page import UserManagementPage
        self.controller.show_frame(UserManagementPage)

    def go_book_management(self):
        from app.pages.book_management_page import BookManagementPage
        self.controller.show_frame(BookManagementPage)

    def go_login(self):
        from app.pages.login_page import LoginPage 
        self.controller.show_frame(LoginPage)
