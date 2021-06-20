from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window


from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from kivy.lang import Builder
Builder.load_file(r'kivy_env\scr\nonMD\ice_block\ice_block.kv')

class IceBlockScreen(Screen):
    lbl_quantity = ObjectProperty()
    def update_ice_quantity(self, value):
        temp = float(self.lbl_quantity.text) + value
        self.lbl_quantity.text = str(temp)
        

class IceBlockApp(App):
    def build(self):
        return IceBlockScreen()

if __name__ == '__main__':

    window_size = [1080, 2280] # Pixels of OnePlus 6
    divide_screen_by = 3

    window_size[0] /= divide_screen_by
    window_size[1] /= divide_screen_by 


    Window.size = (window_size[0], window_size[1])

    ice_block_screen_app = IceBlockApp()
    ice_block_screen_app.run()