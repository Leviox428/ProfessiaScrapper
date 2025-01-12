import customtkinter as ctk
from Components.topBar import TopBar
from Pages.homePage import HomePage

class Dashboard(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.content = None
        self.CreateDashboard()

    def CreateDashboard(self):
        TopBar(parent=self, controller=self)
        self.ChangeContent(HomePage(self, self))

    def ChangeContent(self, page):
        if self.content:
                self.content.destroy()
        page.pack(fill="both", expand=True)
        self.content = page
    