import os
import random
from PIL import Image, ImageDraw
import customtkinter
from Sound import Sound

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class Game(customtkinter.CTk):
    def __init__(self, a, b):
        super().__init__()
        self.geometry("900x600")
        self.title("PickIt")
        self.user_turn = 1
        self.first_user_answer = None
        self.second_user_answer = None
        self.first_user_score = '0'
        self.second_user_score = '0'
        self.first_user_name = a
        self.second_user_name = b
        self.sounds_folder_path = 'sounds/cvc_samples'
        self.sound_file_names = os.listdir(self.sounds_folder_path)
        self.images_folder_path = 'cvc_images'
        self.images_file_names = os.listdir(self.images_folder_path)
        self.index = random.choice([num for num in range(0, len(self.images_file_names)) if num != 0])
        self.random_number = random.choice([num for num in range(0, len(self.images_file_names)) if num != self.index])
        self.chose = random.randint(1,5000)
        self.create_widgets()

    def create_widgets(self):
        self.load_image()
        self.create_first_user_name()
        self.create_first_user_score()
        self.create_second_user_name()
        self.create_second_user_score()
        self.create_1st_option_button()
        self.create_2nd_option_button()
        self.create_audio_button()
        self.turn_indicator()

    def sound_click(self):
        complete_pth = self.sounds_folder_path + '/' + (
                    self.images_file_names[self.index].split('.')[0].strip() + '.mp3')
        try:
            s = Sound(complete_pth)
            s.play_sound()
        except:
            pass

    def make_image_cornors_curve(self, image):
        radius = 50
        mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0, image.width, image.height), radius, fill=255)
        image.putalpha(mask)
        return image

    def load_image(self):
        file_path = os.path.join(self.images_folder_path, self.images_file_names[self.index])
        image = Image.open(file_path)
        self.show_image(self.make_image_cornors_curve(image))

    def create_first_user_name(self):
        first_user_textbox = customtkinter.CTkTextbox(
            self,
            corner_radius=15,
            fg_color='transparent',
            width=200,
            height=10,
            text_color="RoyalBlue1",
            font=('', 26, 'bold')
        )
        first_user_textbox.insert("1.0", self.first_user_name)
        first_user_textbox.configure(state="disabled")
        first_user_textbox.pack(anchor="nw", padx=(90, 0), pady=(110, 0))

    def create_first_user_score(self):
        self.first_user_score_text = customtkinter.CTkTextbox(
            self,
            corner_radius=15,
            padx=16,
            fg_color='transparent',
            width=120,
            height=10,
            text_color="RoyalBlue1",
            font=('', 30, 'bold')
        )
        self.first_user_score_text.insert("1.0", self.first_user_score)
        self.first_user_score_text.configure(state="disabled")
        self.first_user_score_text.pack(anchor="nw", padx=(120, 0), pady=(0, 0))

    def show_image(self, img_obj):
        image = customtkinter.CTkImage(img_obj, size=(260, 260))
        self.image_label = customtkinter.CTkLabel(self, text="", image=image)
        self.image_label.place(x=340, y=40)

    def create_second_user_name(self):
        self.second_user_textbox = customtkinter.CTkTextbox(
            self,
            corner_radius=15,
            fg_color='transparent',
            width=200,
            height=10,
            text_color="RoyalBlue1",
            font=('', 26, 'bold')
        )
        self.second_user_textbox.insert("1.0", self.second_user_name)
        self.second_user_textbox.configure(state="disabled")
        self.second_user_textbox.place(x=680, y=110)

    def create_second_user_score(self):
        self.second_user_score_text = customtkinter.CTkTextbox(
            self,
            corner_radius=15,
            padx=16,
            fg_color='transparent',
            width=120,
            height=10,
            text_color="RoyalBlue1",
            font=('', 30, 'bold')
        )
        self.second_user_score_text.insert("1.0", self.second_user_score)
        self.second_user_score_text.configure(state="disabled")
        self.second_user_score_text.place(x=725, y=170)

    def create_1st_option_button(self):
        if self.chose == 1:
            tem = self.images_file_names[self.index].split('.')[0]
        else:
            tem = self.images_file_names[self.random_number].split('.')[0]
        self.button1 = customtkinter.CTkButton(
            self,
            fg_color='RoyalBlue1',
            text=tem,
            text_color='white',
            command=lambda: self.answer_button_click(self.button1.cget('text')),
            width=120,
            height=50
        )
        self.button1.place(x=250, y=350)

    def create_audio_button(self):
        self.audio_button = customtkinter.CTkButton(
            self,
            fg_color='DarkGoldenRod2',
            hover_color='DarkGoldenRod3',
            text="Audio",
            text_color='white',
            command=self.sound_click,
            width=40,
            corner_radius=125,
            height=40,
            border_width=0
        )
        self.audio_button.place(x=450, y=360)

    def create_2nd_option_button(self):
        if self.chose == 1:
            tem = self.images_file_names[self.random_number].split('.')[0]
        else:
            tem = self.images_file_names[self.index].split('.')[0]
        self.button2 = customtkinter.CTkButton(
            self,
            fg_color='RoyalBlue1',
            text=tem,
            text_color='white',
            command=lambda: self.answer_button_click(self.button2.cget('text')),
            width=120,
            height=50
        )
        self.button2.place(x=620, y=350)

    def turn_indicator(self):
        self.turn_textbox = customtkinter.CTkTextbox(
            self,
            padx=25,
            corner_radius=15,
            fg_color='transparent',
            width=500,
            height=10,
            text_color="RoyalBlue1",
            font=('', 38)
        )
        if self.user_turn == 1:
            self.turn_textbox.insert("1.0", self.first_user_name + ' Turn!')
        elif self.user_turn == 2:
            self.turn_textbox.insert("1.0", self.second_user_name + ' Turn!')
        self.turn_textbox.configure(state="disabled")
        self.turn_textbox.pack(padx=(230, 0), pady=(220, 0))

    def update_first_user_score_text(self):
        self.first_user_score = str(int(self.first_user_score) + 10)
        self.first_user_score_text.configure(state="normal")
        self.first_user_score_text.delete('1.0', customtkinter.END)
        self.first_user_score_text.insert('1.0', self.first_user_score)
        self.first_user_score_text.configure(state="disabled")

    def update_second_user_score_text(self):
        self.second_user_score = str(int(self.second_user_score) + 10)
        self.second_user_score_text.configure(state="normal")
        self.second_user_score_text.delete('1.0', customtkinter.END)
        self.second_user_score_text.insert('1.0', self.second_user_score)
        self.second_user_score_text.configure(state="disabled")

    def update_turn_textbox(self):
        self.turn_textbox.configure(state="normal")
        self.turn_textbox.delete('1.0', customtkinter.END)
        if self.user_turn == 2:
            self.turn_textbox.insert('1.0', self.second_user_name + ' Turn!')
        elif self.user_turn == 1:
            self.turn_textbox.insert('1.0', self.first_user_name + ' Turn!')
        self.turn_textbox.configure(state='disabled')

    def update_2nd_option(self):
        if self.chose %2==0:
            tem = self.images_file_names[self.random_number].split('.')[0]
        else:
            tem = self.images_file_names[self.index].split('.')[0]
        self.button2.configure(text=tem)

    def update_1st_option(self):
        if self.chose %2==0:
            tem = self.images_file_names[self.index].split('.')[0]
        else:
            tem = self.images_file_names[self.random_number].split('.')[0]
        self.button1.configure(text=tem)

    def update_image(self):
        tem = Image.open(os.path.join(self.images_folder_path, self.images_file_names[self.index]))
        tem = self.make_image_cornors_curve(tem)
        image = customtkinter.CTkImage(
            tem, size=(260, 260))
        self.image_label.configure(image=image)

    def answer_button_click(self, ans):
        if self.user_turn == 1:
            self.first_user_answer = ans + ".png"
            try:
                if self.first_user_answer == self.images_file_names[self.index]:
                    self.update_first_user_score_text()
                    s = Sound('sounds/effects/correct_answer.mp3')
                    s.play_sound()
                else:
                    s = Sound('sounds/effects/wrong_answer.mp3')
                    s.play_sound()
                self.user_turn = 2
                self.update_turn_textbox()
            except:
                pass
        else:
            self.second_user_answer = ans + ".png"
            try:
                if self.second_user_answer == self.images_file_names[self.index]:
                    self.update_second_user_score_text()
                    s = Sound('sounds/effects/correct_answer.mp3')
                    s.play_sound()
                else:
                    s = Sound('sounds/effects/wrong_answer.mp3')
                    s.play_sound()
                self.user_turn = 1
                self.update_turn_textbox()
            except:
                pass
        self.index=random.choice([num for num in range(0, len(self.images_file_names)) if num != self.index])
        self.random_number = random.choice(
            [num for num in range(0, len(self.images_file_names)) if num != self.index])
        self.chose = random.randint(1,5000)
        self.update_1st_option()
        self.update_2nd_option()
        self.update_image()
