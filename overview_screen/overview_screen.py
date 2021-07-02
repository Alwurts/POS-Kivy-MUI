from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout


from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from kivy.lang import Builder
Builder.load_file(r'overview_screen\overview_screen.kv')


from database_functions import get_items


class OverviewScreen(Screen):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.load_sales()
    '''
    def open_sell_public(self):
        self.parent.parent.sell_public_screen.user_logged.text = self.user_logged.text
        self.parent.current = 'sell_public'
    '''
    def load_data(self):
        
        self.sales_layout.clear_widgets()
        self.load_sales()
        

    def load_sales (self):
        temp = get_items()
        for row in temp:

            temp_box = BoxLayout(size_hint_y= None,
                                size_hint_x= 1,
                                height= '40dp',
                                padding= [10,10],
                                spacing= 10)
            temp_lbl = Label(text= str(row[0]),
                                size_hint_x= .4,
                                font_size= '15dp',
                                bold= True)
            temp_box.add_widget(temp_lbl)
            temp_lbl = Label(text= str(row[1]),
                                size_hint_x= .2,
                                font_size= '15dp',
                                bold= True)
            temp_box.add_widget(temp_lbl)
            temp_lbl = Label(text= str(row[2]),
                                size_hint_x= .2,
                                font_size= '15dp',
                                bold= True)
            temp_box.add_widget(temp_lbl)
            temp_lbl = Label(text= '$' + str(row[3]),
                                size_hint_x= .2,
                                font_size= '15dp',
                                bold= True)
            temp_box.add_widget(temp_lbl)
            self.sales_layout.add_widget(temp_box)
       

   
        

class OverviewApp(MDApp):
    def build(self):
        return OverviewScreen()

if __name__ == '__main__':

    window_size = [1080, 2280] # Pixels of OnePlus 6
    divide_screen_by = 3

    window_size[0] /= divide_screen_by
    window_size[1] /= divide_screen_by 

    Window.size = (window_size[0], window_size[1])

    sales_public_screen_app = OverviewApp()
    sales_public_screen_app.run()