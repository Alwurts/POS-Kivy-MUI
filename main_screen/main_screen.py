from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window


from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from kivy.lang import Builder
Builder.load_file(r'kivy_env\scr\nonMD\main_screen\main_screen.kv')

class MainScreen(Screen):
    user_logged = ObjectProperty()

    def reset_screen(self):
        self.user_logged.text = 'User: '

    def log_out(self):
        self.parent.current = 'login'
        self.reset_screen()

    def open_sales_public(self):
        self.parent.parent.sales_public_screen.load_data()
        self.parent.parent.sales_public_screen.user_logged.text = self.user_logged.text
        self.parent.current = 'sales_public'
        
    

class MainScreenApp(App):
    def build(self):
        return MainScreen()

if __name__ == '__main__':

    window_size = [1080, 2280] # Pixels of OnePlus 6
    divide_screen_by = 3

    window_size[0] /= divide_screen_by
    window_size[1] /= divide_screen_by 


    Window.size = (window_size[0], window_size[1])

    main_screen_app = MainScreenApp()
    main_screen_app.run()