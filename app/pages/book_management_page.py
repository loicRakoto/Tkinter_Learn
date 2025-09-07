import tkinter as tk

class BookManagementPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        self.controller = controller

        tk.Label(self, text="Ceci est la Page de Gestion des Livres", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Retour Home", command=lambda: self.controller.show_frame(__import__("app.pages.home_page").pages.home_page.HomePage)).pack(pady=10)
