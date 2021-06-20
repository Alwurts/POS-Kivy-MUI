from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window


from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from kivy.lang import Builder
Builder.load_file(r'kivy_env\scr\nonMD\sell_public\sell_public.kv')

from scr.nonMD.database_functions import sell_item

class SellPublicScreen(Screen):
    lbl_quantity_ice_block = ObjectProperty()
    lbl_quantity_ice_bag = ObjectProperty()
    lbl_quantity_water_19L = ObjectProperty()
    user_logged = ObjectProperty()
    
    def update_quantity(self, value,product):

        if value > 0:
            temp = float(product.text) + value
            product.text = str(temp)
        elif float(product.text) > 0:
            temp = float(product.text) + value
            product.text = str(temp)

    def reset_screen(self):
        self.lbl_quantity_ice_block.text = '0.0'
        self.lbl_quantity_ice_bag.text = '0.0'
        self.lbl_quantity_water_19L.text = '0.0'

    def sell_items(self):
        print("running")
        print(self.user_logged.text[6:])
        temp = True
        if float(self.lbl_quantity_ice_block.text) > 0:
            sell_item("ice block",self.lbl_quantity_ice_block.text, 160, self.user_logged.text[6:])
            temp = False
        if float(self.lbl_quantity_ice_bag.text) > 0:
            sell_item("ice bag",self.lbl_quantity_ice_bag.text, 30, self.user_logged.text[6:])
            temp = False
        if float(self.lbl_quantity_water_19L.text) > 0:
            sell_item("water 19L",self.lbl_quantity_water_19L.text, 14, self.user_logged.text[6:])
            temp = False
        if temp == False:
            self.parent.parent.sales_public_screen.load_data()
            self.parent.current = 'sales_public'
            self.reset_screen()
        
        

class SellPublicApp(App):
    def build(self):
        return SellPublicScreen()

if __name__ == '__main__':

    window_size = [1080, 2280] # Pixels of OnePlus 6
    divide_screen_by = 3

    window_size[0] /= divide_screen_by
    window_size[1] /= divide_screen_by 


    Window.size = (window_size[0], window_size[1])

    sell_public_screen_app = SellPublicApp()
    sell_public_screen_app.run()