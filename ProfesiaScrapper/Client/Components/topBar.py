import customtkinter as ctk
from Util.fontConfig import FontConfig
from Interfaces.component import Component
from Pages.homePage import HomePage


class TopBar(ctk.CTkFrame, Component):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.CreateComponent()

    def CreateComponent(self):
        self.configure(height=80, corner_radius=0, fg_color="#252525")
        self.pack(fill="x", side="top")

        # Configure grid layout for the main frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        # Navbar Frame
        navbar = ctk.CTkFrame(self, corner_radius=10)
        navbar.grid(row=0, column=1, pady=10, sticky="nsew")

        navbar.grid_columnconfigure(0, weight=0)
        navbar.grid_columnconfigure(1, weight=0)

        self.home_frame = ctk.CTkFrame(navbar, fg_color="transparent")
        self.home_frame.grid(row=0, column=0, padx=15, pady=10, sticky="nsew")

        self.jobs_frame = ctk.CTkFrame(navbar, fg_color="transparent")
        self.jobs_frame.grid(row=0, column=1, padx=15, pady=10, sticky="nsew")

        homeLabel = ctk.CTkLabel(self.home_frame, font=FontConfig.GetFont(), text="Home", text_color="white")
        homeLabel.pack(side="top")  
        homeLabel.bind("<Button-1>", lambda event: self.OnHomeLabelClicked())

        jobsLabel = ctk.CTkLabel(self.jobs_frame, font=FontConfig.GetFont(), text="Jobs", text_color="white")
        jobsLabel.pack(side="top")
        jobsLabel.bind("<Button-1>", lambda event: self.OnJobsLabelClicked())

        self.homeBorder = ctk.CTkFrame(self.home_frame, height=2, fg_color="white", width=homeLabel.winfo_reqwidth())
        self.jobsBorder = ctk.CTkFrame(self.jobs_frame, height=2, fg_color="white", width=jobsLabel.winfo_reqwidth())

        self.homeBorder.pack(side="bottom", fill="x")
        self.jobsBorder.pack(side="bottom", fill="x")
        self.jobsBorder.pack_forget()

    def OnHomeLabelClicked(self):
        self.homeBorder.pack(side="bottom", fill="x")
        self.jobsBorder.pack_forget()
        self.controller.ChangeContent(HomePage(self.controller, self.controller))

    def OnJobsLabelClicked(self):
        self.jobsBorder.pack(side="bottom", fill="x")
        self.homeBorder.pack_forget()


