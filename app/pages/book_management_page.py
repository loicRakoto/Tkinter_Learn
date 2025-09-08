from customtkinter import *
from tkinter import messagebox, ttk
import tkinter as tk

from app.db import add_book, delete_book, get_all_books, update_book

class BookManagementPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white", width=1200, height=850)
        self.controller = controller
        self.pack_propagate(False)


        logoLabel = CTkLabel(self, text="Gestion des livres", font=('Microsoft YaHei UI Light', 30, 'bold'), text_color="#f857e3")
        logoLabel.grid(row=0, column=0, columnspan=2, pady=20)

        leftFrame = CTkFrame(self, fg_color="white")
        leftFrame.grid(row=1, column=0, padx=20, pady=(10,10), sticky="n")

        labels = ["Id", "Titre", "Auteur", "Publication", "Résumé", "Lien"]
        self.entries = {}

        for i, text in enumerate(labels):
            label = CTkLabel(leftFrame, text=text, font=('Microsoft YaHei UI Light', 16, 'bold'), text_color="#28047A")
            label.grid(row=i, column=0, pady=10, sticky='w')

            entry = CTkEntry(leftFrame, font=('Microsoft YaHei UI Light', 14), width=180)
            entry.grid(row=i, column=1, padx=10)
            self.entries[text] = entry
        
        self.entries["Id"].configure(state="readonly")

        # === Frame droite : recherche + tableau ===
        rightFrame = CTkFrame(self, fg_color="white")
        rightFrame.grid(row=1, column=1, padx=20, pady=10)

        search_options = ('Id', 'Titre', 'Auteur', 'Publication', 'Résumé', 'Lien')
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

        # === Tableau livres ===
        self.tree = ttk.Treeview(rightFrame, height=10)
        self.tree.grid(row=1, column=0, columnspan=4, pady=10)

        self.tree['columns'] = ('Id', 'Titre', 'Auteur', 'Publication', 'Résumé', 'Lien')
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
            ("Nouveau Livre", "#57a1f8",self.new_insert_book_table),
            ("Ajouter Livre", "#57a1f8",self.add_book_to_table),
            ("Modifier Livre", "#57a1f8",self.update_book_in_table),
            ("Supprimer Livre", "#0626B3",self.delete_book_from_table),
            ("Retour Home", "#FF5733",self.return_to_home)
        ]

        for i, (text, color, cmd) in enumerate(buttons):
            btn = CTkButton(buttonFrame, text=text, font=('Microsoft YaHei UI Light', 14, 'bold'),
                            width=160, corner_radius=15, fg_color=color,
                            command=cmd)
            btn.grid(row=0, column=i, padx=5, pady=5)

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        self.load_books()

    def new_insert_book_table(self):
        self.clear_entries()
    
    def load_books(self):
        self.tree.delete(*self.tree.get_children())
        books = get_all_books()
        for book in books:
            self.tree.insert('', 'end', values=book)

    
    def update_book_in_table(self):
        book_id = self.entries["Id"].get()
        if not book_id:
            messagebox.showerror("Erreur", "Sélectionnez un livre à modifier")
            return
        title = self.entries["Titre"].get()
        author = self.entries["Auteur"].get()
        publication = self.entries["Publication"].get()
        summary = self.entries["Résumé"].get()
        link = self.entries["Lien"].get()
        if not title or not author or not publication or not summary or not link :
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires")
            return
        try:
            update_book(book_id, title, author, publication, summary, link)
            messagebox.showinfo("Succès", f"Livre {title} modifié")
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de modifier le livre : {e}")
        finally:
            self.load_books()
            self.clear_entries()


    def return_to_home(self):
        from app.pages.login_page import HomePage 
        self.controller.show_frame(HomePage)

    def delete_book_from_table(self):
        book_id = self.entries["Id"].get()
        if not book_id:
            messagebox.showerror("Erreur", "Sélectionnez un livre à supprimer")
            return
        try:
            delete_book(book_id)
            messagebox.showinfo("Succès", f"Livre {book_id} supprimé")
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de supprimer le livre : {e}")
        finally:
            self.load_books()
            self.clear_entries()

    def add_book_to_table(self):
        title = self.entries["Titre"].get()
        author = self.entries["Auteur"].get()
        publication = self.entries["Publication"].get()
        summary = self.entries["Résumé"].get()
        link = self.entries["Lien"].get()
        if not title or not author or not publication or not summary or not link :
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires")
            return
        try:
            add_book(title, author, publication, summary, link)
            messagebox.showinfo("Succès", f"Livre {title} ajouté")
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ajouter le livre : {e}")
        finally:
            self.load_books()
            self.clear_entries()

    def clear_entries(self):
        for key in self.entries:
            self.entries[key].configure(state="normal")
            self.entries[key].delete(0, "end")
        self.entries["Id"].configure(state="readonly")
    
    def on_tree_select(self, event):
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], "values")

            # Id (lecture seule)
            self.entries["Id"].configure(state="normal")
            self.entries["Id"].delete(0, "end")
            self.entries["Id"].insert(0, values[0])
            self.entries["Id"].configure(state="readonly")

            # Titre
            self.entries["Titre"].delete(0, "end")
            self.entries["Titre"].insert(0, values[1])

            # Auteur
            self.entries["Auteur"].delete(0, "end")
            self.entries["Auteur"].insert(0, values[2])

            # Date de publication
            self.entries["Publication"].delete(0, "end")
            self.entries["Publication"].insert(0, values[3])

            # Résumé
            self.entries["Résumé"].delete(0, "end")
            self.entries["Résumé"].insert(0, values[4])

            # Lien
            self.entries["Lien"].delete(0, "end")
            self.entries["Lien"].insert(0, values[5])