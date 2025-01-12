import customtkinter as ctk
from dashboard import Dashboard
from Pages.loginPage import LoginPage
from Pages.registerPage import RegisterPage
from Firebase.firebaseInitializer import FirebaseInitializer

class MyApp(ctk.CTk): 
    def __init__(self):
        super().__init__()
        FirebaseInitializer.Initialize()

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("green")

        self.title("Profesia scrapper")
        self.geometry("1200x800")

        self.pages = {} 
        self.currentPage = None

        self.CreatePages()

        self.ShowPage("LoginPage")

    def CreatePages(self):
        self.pages["LoginPage"] = LoginPage
        self.pages["DashboardPage"] = Dashboard
        self.pages["RegisterPage"] = RegisterPage

    def ShowPage(self, pageName):
        if self.currentPage:
            self.currentPage.destroy()

        pageClass = self.pages.get(pageName)
        if pageClass:
            page = pageClass(self, self)
            page.pack(fill="both", expand=True)
            self.currentPage = page  


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()