import customtkinter as ctk
from Interfaces.page import Page
from Util.fontConfig import FontConfig
from Server.regionDataManager import RegionDataManager
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from DataModels.region import Region


class HomePage(ctk.CTkFrame, Page):
     def __init__(self, parent, controller):
        super().__init__(parent)
        self.regionData = []
        self.numOfJobsOfRegion = {}
        self.averageWageOfRegion = {}
        self.controller = controller
        self.InitializeData()     
        self.CreatePage()
        

     def InitializeData(self):
         self.regionData = RegionDataManager.regions
         for region in self.regionData:
             regionName = region.regionName
             numOfJobs = region.numOfJobPostings
             averageWage = region.averageWage
             self.numOfJobsOfRegion[regionName] = numOfJobs
             self.averageWageOfRegion[regionName] = averageWage


     def CreatePage(self):
        chartFrame = ctk.CTkFrame(self)
        chartFrame.pack(pady=20, padx=20, fill="both", expand=True)

        fig1 = self.CreateBarChart(self.numOfJobsOfRegion, "Job postings of region")
        fig2 = self.CreateBarChart(self.averageWageOfRegion, "Average wage of region")

        canvas1 = FigureCanvasTkAgg(fig1, master=chartFrame)
        canvas1Widget = canvas1.get_tk_widget()
        canvas1Widget.grid(row=0, column=0, padx=10, pady=10)

        canvas2 = FigureCanvasTkAgg(fig2, master=chartFrame)
        canvas2Widget = canvas2.get_tk_widget()
        canvas2Widget.grid(row=0, column=1, padx=10, pady=10)
     
     def CreateBarChart(self, data, title):
        sortedData = sorted(data.items(), key=lambda item: item[1], reverse=True)
        labels, values = zip(*sortedData)

        fig = Figure(figsize=(7, 7), dpi=100)
        ax = fig.add_subplot(111)
        ax.bar(labels, values, color="blue")
        ax.set_title(title)
        ax.set_xlabel("Regions")
        ax.set_ylabel("Values")

        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels(labels, rotation=45, ha="right")
        fig.tight_layout()
        return fig
        



        

         
         