from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField


class RegisterScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        wrapper = MDBoxLayout(
            orientation='vertical',
            padding=dp(10),
            spacing=dp(10),
        )

        container = MDBoxLayout(
            orientation='vertical',
            pos_hint={"center_x":0.5, "center_y":0.5}
        )

        label_title = MDLabel(
            text="Welcome to Temenan",
            halign="center",
            font_style="H4",
            theme_text_color="Primary",
        )

        heart_icon = MDIcon(
            icon="heart",
            pos_hint={"center_x":0.5, "center_y":0.5},
            font_size=dp(60)
        )

        label_register = MDLabel(
            text="Please Register before use our service\n use your active phone number!",
            halign="center",
            font_style="Subtitle1",
            theme_text_color="Primary",
        )

        phone_number = MDTextField(
            hint_text="Insert Your Phone Number",
            size_hint=(0.8,None),
            pos_hint={"center_x":0.5, "center_y":0.5}
        )

        signup_button = MDFlatButton(
            text="Sign Up",
            md_bg_color=(0,0,0,0),
            pos_hint={"center_x":0.5, "center_y":0.5},
            on_press=lambda x: self.verify_number()
        )

        container.add_widget(MDLabel(text=""))
        container.add_widget(heart_icon)
        container.add_widget(label_title)
        container.add_widget(label_register)
        container.add_widget(phone_number)
        container.add_widget(signup_button)
        container.add_widget(MDLabel(text=""))

        wrapper.add_widget(container)

        self.add_widget(wrapper)