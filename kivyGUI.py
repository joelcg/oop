import kivy
kivy.require('1.0.6')

from kivy.uix.label import Label
from kivy.app import App

class MyApp(App):
    
    def build(self):
        return Label(text='Hello World')

from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
      
class LoginScreen(GridLayout):
    def __init__(self, **var_args):
        
        super(LoginScreen, self).__init__(**var_args)
        self.cols = 2
        self.add_widget(Label(text ='User Name'))
        self.username = TextInput(multiline = True)
        self.add_widget(self.username)
        
