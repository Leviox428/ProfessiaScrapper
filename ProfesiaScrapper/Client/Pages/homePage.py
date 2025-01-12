import customtkinter as ctk
from Interfaces.page import Page
from Util.fontConfig import FontConfig


class HomePage(ctk.CTkFrame, Page):
     def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller     
        self.CreatePage()

     def CreatePage(self):
        top = ctk.CTkFrame(self, height=80, corner_radius=0)
        top.pack(fill="x")

        top.grid_columnconfigure(0, weight=1)
        top.grid_columnconfigure(1, weight=1)
        top.grid_columnconfigure(2, weight=1)
        



        

         
         