from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import Label, MDLabel
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from kivy.lang import Builder
Builder.load_file(r'kivy_env\scr\MD\login\login.kv')

from scr.nonMD.database_functions import get_users
  
class LoginScreen(Screen):

    buttons_layout = ObjectProperty()
    buttons_layout = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_users()
        self.load_users()
    
    def load_users (self):
        users = get_users()
        self.buttons_layout.clear_widgets()
        for user in users:
            

            
            temp_box = BoxLayout(orientation='vertical', size_hint_y= None, spacing=10, height=100)
            temp_icon = MDIconButton(icon='account',user_font_size= "50sp",md_bg_color= (0, 0, .8, .5))
            temp_icon.bind(on_press=self.login)
            temp_anchor = AnchorLayout(size_hint_y= None, height= temp_icon.height)
            temp_anchor.add_widget(temp_icon)
            
            temp_box.add_widget(temp_anchor)
    
            temp_label = MDLabel(text=user,
                                font_style= 'H5',
                                halign= "center")

            temp_box.add_widget(temp_label)
            
            self.buttons_layout.add_widget(temp_box)
        '''
        for user in users:
            temp_button = Button(text=user,bold= True, font_size= '18dp', background_color= (0, 0.22, 0.373, 1.0))
            temp_button.bind(on_press=self.login)
            self.buttons_layout.add_widget(temp_button)
        '''

    def login(self, user):
        
        self.parent.current = 'password_input'
        self.parent.parent.password_input_screen.user = user.text
        

class LoginApp(MDApp):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':

    window_size = [1080, 2280] # Pixels of OnePlus 6
    divide_screen_by = 3

    window_size[0] /= divide_screen_by
    window_size[1] /= divide_screen_by 


    Window.size = (window_size[0], window_size[1])

    login_app = LoginApp()
    login_app.run()