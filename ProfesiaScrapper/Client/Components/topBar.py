import customtkinter as ctk
from Util.fontConfig import FontConfig
from Interfaces.component import Component
from Server.userDataManager import UserDataManager
from Pages.homePage import HomePage


class TopBar(ctk.CTkFrame, Component):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.user = UserDataManager.user
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
        navbar.grid_columnconfigure(2, weight=0)

        homeFrame = ctk.CTkFrame(navbar, fg_color="transparent")
        homeFrame.grid(row=0, column=0, padx=15, pady=10, sticky="nsew")

        jobsFrame = ctk.CTkFrame(navbar, fg_color="transparent")
        jobsFrame.grid(row=0, column=1, padx=15, pady=10, sticky="nsew")

        profileFrame = ctk.CTkFrame(navbar, fg_color="transparent")
        profileFrame.grid(row=0, column=2, padx=15, pady=10, sticky="nsew")


        homeLabel = ctk.CTkLabel(homeFrame, font=FontConfig.GetFont(), text="Home", text_color="white")
        homeLabel.pack(side="top")  
        homeLabel.bind("<Button-1>", lambda event: self.OnHomeLabelClicked())

        jobsLabel = ctk.CTkLabel(jobsFrame, font=FontConfig.GetFont(), text="Jobs", text_color="white")
        jobsLabel.pack(side="top")
        jobsLabel.bind("<Button-1>", lambda event: self.OnJobsLabelClicked())

        profileLabel = ctk.CTkLabel(profileFrame, font=FontConfig.GetFont(), text="Profile", text_color="white")
        profileLabel.pack(side="top")
        profileLabel.bind("<Button-1>", lambda event: self.OnProfileLabelClicked())

        self.homeBorder = ctk.CTkFrame(homeFrame, height=2, fg_color="white", width=homeLabel.winfo_reqwidth())
        self.jobsBorder = ctk.CTkFrame(jobsFrame, height=2, fg_color="white", width=jobsLabel.winfo_reqwidth())
        self.profileBorder = ctk.CTkFrame(profileFrame, height=2, fg_color="white", width=jobsLabel.winfo_reqwidth())

        self.homeBorder.pack(side="bottom", fill="x")

        usernameLabel = ctk.CTkLabel(self, font=FontConfig.GetFont(), text=self.user.username, text_color="white")
        usernameLabel.grid(row=0, column=2, pady=10, sticky="nsew")

    def OnHomeLabelClicked(self):
        self.homeBorder.pack(side="bottom", fill="x")
        self.jobsBorder.pack_forget()
        self.profileBorder.pack_forget()
        self.controller.ChangeContent(HomePage(self.controller, self.controller))

    def OnJobsLabelClicked(self):
        self.jobsBorder.pack(side="bottom", fill="x")
        self.homeBorder.pack_forget()
        self.profileBorder.pack_forget()
    
    def OnProfileLabelClicked(self):
        self.profileBorder.pack(side="bottom", fill="x")
        self.homeBorder.pack_forget()
        self.jobsBorder.pack_forget()


