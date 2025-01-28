from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

from screens.register import RegisterScreen


class MainApp(MDApp):
    def build(self):
        Window.size = (360, 640)
        sm = MDScreenManager()
        sm.add_widget(RegisterScreen(name='register'))

        sm.current = 'register'
        return sm

if __name__ == '__main__':
    MainApp().run()