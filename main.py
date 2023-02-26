from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from stopwatch import Stopwatch

#Designate kv file for design layout
Builder.load_file('timer_layout.kv')

class CustomLayout(FloatLayout):
    pass

class TimerLayout(FloatLayout):
    
    def clear(self):
        Stopwatch.reset(self)
        self.ids.time_field.text = "Shot time cleared!"

    def add_shot(self):
        stopwatch = Stopwatch(3)
        stopwatch.start()
        

    def stop_time(self):
        stopwatch = Stopwatch()
        stopwatch.stop()
        self.ids.time_field.text = str(stopwatch.duration)

class MainApp(App):
    
    def build(self):
        return TimerLayout()

if __name__ == '__main__':
    app = MainApp()
    app.run()
