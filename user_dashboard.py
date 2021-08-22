from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
#from Swipe_Bot import TinderBot


class SwiperBot(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.greeting = Label (
                        text = "The smart way to Swipe",
                        font_size = 22,
                        italic = True,
                        color = '#00FFCE',
                        )

        self.window.add_widget(self.greeting)

        self.user = TextInput(
                    multiline=False,
                    font_size= 22,
                    padding_y=(20, 20),
                    size_hint=(1, 0.3),
                    hint_text= 'Your username',
                    )
        self.window.add_widget(self.user)

        self.pwd = TextInput(
            multiline=False,
            font_size=22,
            padding_y=(20, 20),
            size_hint=(1, 0.3),
            hint_text='Your password',
            password = True,

        )
        self.window.add_widget(self.pwd)

        self.button = Button (text = "Get me Laid!",
                              size_hint = (1,0.3),
                              bold = True,
                              background_color = '#00FFCE'
                              )


        self.button.bind (on_press = self.callback)
        self.window.add_widget(self.button)
        return self.window


    def callback(self, instance):
        pass
        #tb = TinderBot()
        #login = tb.login
        #login (_username=self.user.text, _password=self.pwd.text)
        #tb.auto_swipe()

        #add widgets to window
if __name__ == "__main__":
    SwiperBot().run()