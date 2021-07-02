from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.list import MDList, ThreeLineAvatarListItem, ImageLeftWidget,IRightBodyTouch 

from kivymd.uix.screen import MDScreen
#from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from kivy.lang import Builder
Builder.load_file(r'sales_public\sales_public.kv')


from database_functions import get_items
#from database_functions import *

class SalesPublicScreen(MDScreen):

    md_list_sales = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.load_sales()

    def load_data(self):
        
        self.md_list_sales.clear_widgets()
        self.load_sales()
        
    
    def load_sales (self):
        temp_items = get_items()
        
        for row in temp_items:

            temp_container = Container()
            temp_icon_btn_1 = MDIconButton(icon= "minus")
            temp_icon_btn_2 = MDIconButton(icon= "plus")
            
            temp_container.add_widget(temp_icon_btn_1)
            temp_container.add_widget(temp_icon_btn_2)
            
            temp_list_item = ThreeLineAvatarListItem(text= str(row[2]),
                                            secondary_text= str(row[3]),
                                            tertiary_text= str(row[0]))

            if str(row[1]) == 'ice block':
                temp_image_item = ImageLeftWidget(source= r"assets\icon_ice_block.png")
            elif str(row[1]) == 'ice bag':
                temp_image_item = ImageLeftWidget(source= r"assets\icon_ice_cube.png")
            elif str(row[1]) == 'water 19L':
                temp_image_item = ImageLeftWidget(source= r"assets\icon_water_19L.png")

            temp_list_item.add_widget(temp_image_item)

            

            #temp_list_item.add_widget(temp_container)

            self.md_list_sales.add_widget(temp_list_item)

class Container(IRightBodyTouch, MDBoxLayout):
    pass   
        

class SalesPublicApp(MDApp):
    def build(self):
        return SalesPublicScreen()

if __name__ == '__main__':

    window_size = [1080, 2280] # Pixels of OnePlus 6
    divide_screen_by = 3

    window_size[0] /= divide_screen_by
    window_size[1] /= divide_screen_by 

    Window.size = (window_size[0], window_size[1])

    sales_public_screen_app = SalesPublicApp()
    sales_public_screen_app.run()