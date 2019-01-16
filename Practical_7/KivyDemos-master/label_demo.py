from kivy.app import App
from kivy.lang import Builder
from kivy.properties import Property
from kivy.uix.popup import Popup
from kivy.uix.modalview import ModalView
from kivy.properties import (StringProperty, OptionProperty)


class LabelDemo(App):
    def build(self):
        self.title = "Hi"
        self.title_align = OptionProperty('center')
        self.root = Builder.load_file('label.kv')
        return self.root

# create and start the App running
LabelDemo().run()
