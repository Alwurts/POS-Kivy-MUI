from ntpath import join
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
    btn_cancel_delete = ObjectProperty()
    lbl_info_field = ObjectProperty()
    lbl_user_to_log = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pwd_array = []

    def update_password(self, instance):
        
        if len(self.pwd_array) < 4 :
            
            # If to avoid using a space on the last dot
            if len(self.pwd_array) == 3: 
                self.show_password.text = self.show_password.text + "."
            else:
                self.show_password.text = self.show_password.text + ". "

            self.pwd_array.append(instance.text)

            self.lbl_info_field.text = 'Ingresa la contrasena'

            if len(self.pwd_array) > 0:
                self.btn_cancel_delete.text='BORRAR'


    def clear_password(self):
        self.show_password.text = ''
        self.pwd_array = []
        self.btn_cancel_delete.text='CANCELAR'
        

    def reset_screen (self):
        self.clear_password()
        self.lbl_info_field.text = 'Ingresa la contrasena'
        self.user=''

    def check_password(self):
        #print(self.user)
        temp_pass = get_password_with_name(self.user)
        '''
        print(temp_pass)
        temp = ""
        temp = temp.join(self.pwd_array)
        print(temp)
        '''
        temp = ""
        if (temp.join(self.pwd_array) == temp_pass):
            
            self.parent.parent.main_screen.children[0].children[0].children[0].lbl_user_logged.text = self.user
            self.parent.parent.main_screen.user_logged = self.user
            
            self.reset_screen()
            self.parent.current = 'main_screen'
          
        else:
            self.lbl_info_field.text = 'Contrasena incorrecta'
            self.clear_password()
        

    def go_back(self):
        if self.btn_cancel_delete.text == 'CANCELAR':
            self.parent.current = 'login'
            self.reset_screen()
        elif self.btn_cancel_delete.text == 'BORRAR':
            self.clear_password()

        

        

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