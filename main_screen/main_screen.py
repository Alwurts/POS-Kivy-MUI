from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import MDList

from scr.MD.sales_public.sales_public import SalesPublicScreen
from scr.MD.overview_screen.overview_screen import OverviewScreen   

from kivy.lang import Builder
Builder.load_file(r'kivy_env\scr\MD\main_screen\main_screen.kv')


class MainScreen(Screen):
    screen_manager = ObjectProperty()
    #lbl_user_logged = ObjectProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.sales_public_screen = SalesPublicScreen()
        self.overview_screen = OverviewScreen()

        self.screen_manager.add_widget(self.overview_screen)
        self.screen_manager.add_widget(self.sales_public_screen)
        
    '''
    def log_out(self):
        self.parent.current = 'login'
        self.reset_screen()

    def reset_screen(self):
        self.user_logged.text = ''
    
    def open_sales_public(self):
        self.parent.parent.sales_public_screen.load_data()
        self.parent.parent.sales_public_screen.user_logged.text = self.user_logged.text
        self.parent.current = 'sales_public'
    ''' 

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
    lbl_user_logged = ObjectProperty()
    main_screen = ObjectProperty()

    def log_out(self):
        self.main_screen.parent.current = 'login'
        self.reset_screen()

    def reset_screen(self):
        self.lbl_user_logged.text = ''
    

class MainScreenApp(MDApp):
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