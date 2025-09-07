import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from app.pages.home_page import HomePage
from app.db import check_user

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white",width=925, height=500)
        self.controller = controller
        self.pack_propagate(False)

        B = os.path.dirname(os.path.abspath(__file__)) 
        image_path = os.path.join(B, "..", "..", "assets", "images", "flower.png")
        image_path = os.path.abspath(image_path)

        img = Image.open(image_path)
        img = img.resize((400, 400))  
        self.photo = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.photo, bg='white').place(x=30, y=50)

        frame = tk.Frame(self, width=350, height=350, bg="white")
        frame.place(x=480, y=70)
        
        heading = tk.Label(frame, text='Connexion', fg='#57a1f8', bg='white',
                           font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=100, y=5)

        self.user = tk.Entry(frame, width=25, fg='black',
                     bg='white', font=('Microsoft YaHei UI Light', 11),
                     bd=0, highlightthickness=0)
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Email') 
        self.user.bind('<FocusIn>', self.on_enter_user)
        self.user.bind('<FocusOut>', self.on_leave_user)
        tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

        self.code = tk.Entry(frame, width=25, fg='black',
                            bg='white', font=('Microsoft YaHei UI Light', 11),
                            bd=0, highlightthickness=0)
        self.code.place(x=30, y=150)
        self.code.insert(0, 'Mot de passe')
        self.code.bind('<FocusIn>', self.on_enter_code)
        self.code.bind('<FocusOut>', self.on_leave_code)
        tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

        tk.Button(frame, width=39, pady=7, text='Se connecter',
                  bg='#57a1f8', fg='white', border=0,
                  command=self.signin).place(x=35, y=204)

    def on_enter_user(self, event):
        if self.user.get() == 'Email':
            self.user.delete(0, 'end')

    def on_leave_user(self, event):
        if self.user.get() == '':
            self.user.insert(0, 'Email')

    def on_enter_code(self, event):
        if self.code.get() == 'Mot de passe':
            self.code.delete(0, 'end')
            self.code.config(show='*')  

    def on_leave_code(self, event):
        if self.code.get() == '':
            self.code.insert(0, 'Mot de passe')
            self.code.config(show='')

    def signin(self):
        username = self.user.get()
        password = self.code.get()

        if check_user(username, password):
            messagebox.showinfo("Succès", "Connexion réussie ✅")
            self.controller.show_frame(HomePage)
        else:
            messagebox.showerror("Erreur", "Identifiants invalides ❌")
