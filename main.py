from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.theming import ThemeManager

from login.login import LoginScreen
from password_input.password_input import PasswordInputScreen
from main_screen.main_screen import MainScreen
'''
from scr.MD.login.login import LoginScreen
from scr.MD.password_input.password_input import PasswordInputScreen
from scr.MD.main_screen.main_screen import MainScreen

from main_screen.main_screen import MainScreen
from ice_block.ice_block import IceBlockScreen
from sales_public.sales_public import SalesPublicScreen
from sell_public.sell_public import SellPublicScreen
'''

class MainWindow(BoxLayout):


    screen_manager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.theme_cls  = ThemeManager()
        # Declare the screens
        self.login_screen = LoginScreen()
        self.password_input_screen = PasswordInputScreen()
        self.main_screen = MainScreen()
        '''
        self.ice_block_screen = IceBlockScreen()
        self.sales_public_screen = SalesPublicScreen()
        self.sell_public_screen = SellPublicScreen()
        '''
        # Added it to the screen manager
        self.screen_manager.add_widget(self.login_screen)
        self.screen_manager.add_widget(self.password_input_screen)
        self.screen_manager.add_widget(self.main_screen)
        '''
        self.screen_manager.add_widget(self.ice_block_screen)
        self.screen_manager.add_widget(self.sales_public_screen)
        self.screen_manager.add_widget(self.sell_public_screen)
        '''

class MainApp(MDApp):
    def build(self):
        #self.theme_cls.colors = colors
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Red"
        return MainWindow()

if __name__ == '__main__':
    
    #window_size = [1080, 2280] # Pixels of OnePlus 6
    window_size = [540, 960] # Pixels of Samsung Galaxy Prime Plus
    divide_screen_by = 1

    window_size[0] /= divide_screen_by
    window_size[1] /= divide_screen_by 

    Window.size = (window_size[0], window_size[1])
    
    main_app = MainApp()
    main_app.run()