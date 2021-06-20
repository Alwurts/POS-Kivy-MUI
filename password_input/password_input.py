from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.core.window import Window

from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from kivy.lang import Builder
Builder.load_file(r'kivy_env\scr\MD\password_input\password_input.kv')

#from database_functions import *
from scr.nonMD.database_functions import get_password_with_name
  
class PasswordInputScreen(Screen):
    show_password = ObjectProperty()
    def update_password(self, instance):
        if self.show_password.text == 'WRONG' or self.show_password.text == '. . . .':
            self.clear_password()

        if len(self.show_password.text) < 4 :
            self.show_password.text = self.show_password.text + instance.text
    
    def reset_password(self):
        self.show_password.text = '. . . .'

    def clear_password(self):
        self.show_password.text = ''

    def reset_screen (self):
        self.reset_password()
        self.user=''

    def check_password(self):
        #print(self.user)
        temp_pass = get_password_with_name(self.user)
        if (self.show_password.text == temp_pass):
            self.parent.parent.main_screen.user_logged.text = 'User: ' + self.user
            self.reset_screen()
            self.parent.current = 'main_screen'
          
        else:
            self.show_password.text = 'WRONG'

    def go_back(self):
        self.parent.current = 'login'
        self.reset_screen()

        

class PasswordInputApp(MDApp):
    def build(self):
        return PasswordInputScreen()

if __name__ == '__main__':

    window_size = [1080, 2280] # Pixels of OnePlus 6
    divide_screen_by = 3

    window_size[0] /= divide_screen_by
    window_size[1] /= divide_screen_by 


    Window.size = (window_size[0], window_size[1])

    #MainApp().run()
    password_app = PasswordInputApp()
    password_app.run()