import customtkinter as ctk
from Firebase.firebaseAuth import FirebaseAuth
from Util.fontConfig import FontConfig
from Interfaces.page import Page

class LoginPage(ctk.CTkFrame, Page):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.auth = FirebaseAuth()
        self.CreatePage()

    def CreatePage(self):
        self.loginPanel = ctk.CTkFrame(self, width=600, height=400, corner_radius=15)
        self.loginPanel.pack_propagate(False)
        self.loginPanel.place(relx=0.5, rely=0.5, anchor="center")

        self.widgetPanel = ctk.CTkFrame(self.loginPanel, width=200, height=100, fg_color="transparent")
        self.widgetPanel.pack(expand=True, fill="both", padx=20, pady=20)
        self.widgetPanel.place(relx=0.5, rely=0.5, anchor="center")

        titleLabel = ctk.CTkLabel(self.widgetPanel, text="Login", font=FontConfig.GetFont(20))
        titleLabel.pack(pady=10)

        self.emailEntry = ctk.CTkEntry(self.widgetPanel, placeholder_text="Enter your email", width=200)
        self.emailEntry.pack(pady=5)

        self.passwordEntry = ctk.CTkEntry(self.widgetPanel, placeholder_text="Enter your password", show="*", width=200)
        self.passwordEntry.pack(pady=5)

        self.loginButton = ctk.CTkButton(self.widgetPanel, text="Login", font=FontConfig.GetFont(), width=80, command=self.OnLoginButtonClicked)
        self.loginButton.pack(pady=5)

        self.registerLabel = ctk.CTkLabel(self.widgetPanel, cursor="hand2", text="Click here to register", font=FontConfig.GetFont(14), text_color="blue")
        self.registerLabel.bind("<Button-1>", self.OnRegisterLinkClicked)
        self.registerLabel.pack()

        self.errorLabel = ctk.CTkLabel(self.widgetPanel, text="", text_color="red", font=FontConfig.GetFont())
        self.errorLabel.pack_forget()


    def OnLoginButtonClicked(self):
        email = self.emailEntry.get()
        password = self.passwordEntry.get()
        email = "test2@gmail.com"
        password = "12345678"
        if not email or not password:
            self.errorLabel.configure(text="Missing login credentials") 
            self.errorLabel.pack(in_=self.widgetPanel)
            
        else:
            message = self.auth.LoginUser(email, password)
            if message == "Success":
                self.controller.ShowPage("DashboardPage")
            else:
                self.errorLabel.configure(text=message)
                self.errorLabel.pack(in_=self.widgetPanel)
                
        
    def OnRegisterLinkClicked(self, event):
        self.controller.ShowPage("RegisterPage")