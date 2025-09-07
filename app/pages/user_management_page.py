from customtkinter import *
from tkinter import messagebox, ttk
import tkinter as tk

class UserManagementPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white", width=1200, height=850)
        self.controller = controller
        self.pack_propagate(False)


        logoLabel = CTkLabel(self, text="Gestion des membres", font=('Microsoft YaHei UI Light', 30, 'bold'), text_color="#f857e3")
        logoLabel.grid(row=0, column=0, columnspan=2, pady=20)

        leftFrame = CTkFrame(self, fg_color="white")
        leftFrame.grid(row=1, column=0, padx=20, pady=(10,10), sticky="n")

        labels = ["Id", "Nom", "Prénom", "Email", "Mot de passe"]
        self.entries = {}

        for i, text in enumerate(labels):
            label = CTkLabel(leftFrame, text=text, font=('Microsoft YaHei UI Light', 16, 'bold'), text_color="#28047A")
            label.grid(row=i, column=0, pady=10, sticky='w')

            entry = CTkEntry(leftFrame, font=('Microsoft YaHei UI Light', 14), width=180)
            entry.grid(row=i, column=1, padx=10)
            self.entries[text] = entry

        # === Frame droite : recherche + tableau ===
        rightFrame = CTkFrame(self, fg_color="white")
        rightFrame.grid(row=1, column=1, padx=20, pady=10)

        search_options = ('Id', 'Nom', 'Prénom', 'Email', 'Mot de passe')
        searchBox = CTkComboBox(rightFrame, values=search_options, state='readonly', width=120,
                                fg_color="black", text_color="white",
                                button_color="#57a1f8", button_hover_color="#4682B4")
        searchBox.grid(row=0, column=0, padx=5, pady=5)
        searchBox.set('Recherche')

        searchEntry = CTkEntry(rightFrame, width=150, fg_color="#f0f0f0",
                               border_color="#57a1f8", text_color="black",
                               placeholder_text="Tapez ici..." )
        searchEntry.grid(row=0, column=1, padx=5)

        searchButton = CTkButton(rightFrame, text='Rechercher', width=100, fg_color="#023F05")
        searchButton.grid(row=0, column=2, padx=5)

        showallButton = CTkButton(rightFrame, text='Afficher tout', width=100, fg_color="#4682B4")
        showallButton.grid(row=0, column=3, padx=5)

        # === Tableau utilisateurs ===
        self.tree = ttk.Treeview(rightFrame, height=10)
        self.tree.grid(row=1, column=0, columnspan=4, pady=10)

        self.tree['columns'] = ('Id', 'Nom', 'Prenom', 'Email', 'Mot de passe')
        for col in self.tree['columns']:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        self.tree.config(show='headings')

        style = ttk.Style()
        style.configure('Treeview.Heading', font=('Microsoft YaHei UI Light', 14, 'bold'))
        style.configure('Treeview', font=('Microsoft YaHei UI Light', 12))

        scrollbar = ttk.Scrollbar(rightFrame, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=1, column=4, sticky='ns')
        self.tree.configure(yscroll=scrollbar.set)

        # === Boutons ===
        buttonFrame = CTkFrame(self, fg_color="white")
        buttonFrame.grid(row=2, column=0, columnspan=2, pady=10)

        buttons = [
            ("Nouveau Utilisateur", "#57a1f8"),
            ("Ajouter Utilisateur", "#57a1f8"),
            ("Modifier Utilisateur", "#57a1f8"),
            ("Supprimer Utilisateur", "#57a1f8"),
            ("Supprimer tout", "#0626B3"),
            ("Retour Home", "#FF5733")
        ]

        for i, (text, color) in enumerate(buttons):
            btn = CTkButton(buttonFrame, text=text, font=('Microsoft YaHei UI Light', 14, 'bold'),
                            width=160, corner_radius=15, fg_color=color,
                            command=(lambda t=text: self.button_command(t)))
            btn.grid(row=0, column=i, padx=5, pady=5)
    
    def button_command(self, text):
        if text == "Retour Home":
            from app.pages.login_page import HomePage 
            self.controller.show_frame(HomePage)
        else:
            messagebox.showinfo("Info", f"Action: {text}")