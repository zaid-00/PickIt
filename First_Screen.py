import customtkinter

from Second_Screen import Game

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class Welcome(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("PickIt")
        self.first_user_entry = None
        self.second_user_entry = None

        self.create_widgets()

    def create_widgets(self):
        self.create_welcome_textbox()
        self.create_first_user_entry()
        self.create_second_user_entry()
        self.create_proceed_button()

    def create_welcome_textbox(self):
        self.welcome_textbox = customtkinter.CTkTextbox(
            self,
            padx=25,
            corner_radius=15,
            fg_color='transparent',
            width=530,
            height=10,
            text_color="RoyalBlue1",
            font=('', 28)
        )
        self.welcome_textbox.insert("0.0", "Welcome to the PickIt")
        self.welcome_textbox.configure(state="disabled")
        self.welcome_textbox.pack(padx=80, pady=(100, 20))

    def create_first_user_entry(self):
        self.first_user_entry = customtkinter.CTkEntry(
            self,
            placeholder_text="Enter name for team 1",
            width=300,
            text_color='white',
            fg_color='transparent',
            height=35,
            border_width=2,
            font=('', 15),
            corner_radius=10
        )
        self.first_user_entry.pack(padx=40)

    def create_second_user_entry(self):
        self.second_user_entry = customtkinter.CTkEntry(
            self,
            placeholder_text="Enter name for team 2",
            width=300,
            text_color='white',
            fg_color='transparent',
            height=35,
            border_width=2,
            font=('', 15),
            corner_radius=10
        )
        self.second_user_entry.pack(pady=15)

    def create_proceed_button(self):
        button = customtkinter.CTkButton(
            self,
            fg_color='RoyalBlue3',
            text="Proceed",
            text_color='white',
            command=self.button_callback
        )
        button.pack(pady=10, padx=10)

    def button_callback(self):
        a,b=self.first_user_entry.get(), self.second_user_entry.get()
        self.destroy()
        Game(a,b).mainloop()


Welcome().mainloop()
