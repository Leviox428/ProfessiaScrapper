import customtkinter as ctk
from Interfaces.page import Page
from Util.fontConfig import FontConfig
from Firebase.Database.dataManager import DataManager


class HomePage(ctk.CTkFrame, Page):
     def __init__(self, parent, controller):
        super().__init__(parent)
        self.data = DataManager.GetData()
        self.controller = controller     
        self.CreatePage()

     def CreatePage(self):
        top = ctk.CTkFrame(self, height=80, corner_radius=0)
        top.pack(fill="x")

        top.grid_columnconfigure(0, weight=1)
        top.grid_columnconfigure(1, weight=1)
        top.grid_columnconfigure(2, weight=1)
        
        lastUpdatedLabel = ctk.CTkLabel(top, font=FontConfig.GetFont(14), text="Not updated", text_color="white")
        if self.data and self.data.get("lastUpdated"):
            lastUpdatedLabel.configure(text=self.data.get("lastUpdated"))           
        
        lastUpdatedLabel.grid(row=0, column=0, padx=15, pady=10, sticky="w")

        updateButton = ctk.CTkButton(top, text="Update", font=FontConfig.GetFont(), width=80, command=self.OnUpdateButtonClicked)
        updateButton.grid(row=0, column=2, padx=15, sticky="e")

        options = ["Today", "This Week", "This Mont"]
        self.dateRangeComboBox = ctk.CTkComboBox(top, values=options, font=FontConfig.GetFont(), state="readonly", width=160)
        self.dateRangeComboBox.grid(row=0, column=1, sticky="") 
        self.dateRangeComboBox.set("Choose date range")



     def OnUpdateButtonClicked(self):
        self.webScrapper = WebScrapper()
        selectedDateRange = self.dateRangeComboBox.get()
        daysCount = None 
        if selectedDateRange == "This Month":
            daysCount = 31
        elif selectedDateRange == "This Week":
            daysCount = 7
        else:
            daysCount = 1
        self.webScrapper.ScrapeAllRegions(daysCount)
        

         
         