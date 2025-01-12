import customtkinter as ctk
import re
from Firebase.firebaseAuth import FirebaseAuth
from Util.fontConfig import FontConfig
from Interfaces.page import Page

class RegisterPage(ctk.CTkFrame, Page):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.auth = FirebaseAuth()
        self.CreatePage()

    def CreatePage(self):
        self.registerPanel = ctk.CTkFrame(self, width=600, height=400, corner_radius=15)
        self.registerPanel.pack_propagate(False)
        self.registerPanel.place(relx=0.5, rely=0.5, anchor="center")

        self.widgetPanel = ctk.CTkFrame(self.registerPanel, width=200, height=100, fg_color="transparent")
        self.widgetPanel.pack(expand=True, fill="both", padx=20, pady=20)
        self.widgetPanel.place(relx=0.5, rely=0.5, anchor="center")

        titleLabel = ctk.CTkLabel(self.widgetPanel, text="Register", font=FontConfig.GetFont(20))
        titleLabel.pack(pady=10)

        self.usernameEntry = ctk.CTkEntry(self.widgetPanel, placeholder_text="Enter your username", width=200)
        self.usernameEntry.pack(pady=5)

        self.emailEntry = ctk.CTkEntry(self.widgetPanel, placeholder_text="Enter your email", width=200)
        self.emailEntry.pack(pady=5)

        self.passwordEntry = ctk.CTkEntry(self.widgetPanel, placeholder_text="Enter your password", show="*", width=200)
        self.passwordEntry.pack(pady=5)

        self.confirmPasswordEntry = ctk.CTkEntry(self.widgetPanel, placeholder_text="Confrim password", show="*", width=200)
        self.confirmPasswordEntry.pack(pady=5)

        self.registerButton = ctk.CTkButton(self.widgetPanel, text="Register", font=FontConfig.GetFont(), width=80, command=self.OnRegisterButtonClicked)
        self.registerButton.pack(pady=5)

        self.loginLabel = ctk.CTkLabel(self.widgetPanel, cursor="hand2", text="Click here to login", font=FontConfig.GetFont(14), text_color="blue")
        self.loginLabel.bind("<Button-1>", self.OnLoginLinkClicked)
        self.loginLabel.pack()

        self.errorLabel = ctk.CTkLabel(self.widgetPanel, text="", text_color="red", font=FontConfig.GetFont())
        self.errorLabel.pack_forget()
    
    def OnRegisterButtonClicked(self):
        email = self.emailEntry.get()
        password = self.passwordEntry.get()
        confirmedPassword = self.confirmPasswordEntry.get()
        username = self.usernameEntry.get()


        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(pattern, email):
            self.errorLabel.configure(text="Invalid email") 
            self.errorLabel.pack(in_=self.widgetPanel)
            return
        
        if password != confirmedPassword:
            self.errorLabel.configure(text="Passwords does not match") 
            self.errorLabel.pack(in_=self.widgetPanel)
            return
        
        if len(password) <= 4:
            self.errorLabel.configure(text="The password is weak") 
            self.errorLabel.pack(in_=self.widgetPanel)
            return

        if not email or not password or not confirmedPassword or not username:
            self.errorLabel.configure(text="Missing register credentials") 
            self.errorLabel.pack(in_=self.widgetPanel)
            return
            
        else:
            message = self.auth.RegisterUser(email, password, username)
            self.errorLabel.configure(text=message) 
            self.errorLabel.pack(in_=self.widgetPanel)
            if message == "User registered successfully":
                self.controller.ShowPage("LoginPage")

    def OnLoginLinkClicked(self, event):
        self.controller.ShowPage("LoginPage")