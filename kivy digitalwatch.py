from kivy.app import App                        #Kivy v2.0.0
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window
import datetime
import time

class gettime(Label):
    def update(self, *args):
        def current_time():
            parser = datetime.datetime.now()
            return parser.strftime("%a %d-%m-%Y\n      %H:%M:%S")
            time.sleep(1)
        self.text = current_time()
            
class DigitalwatchApp(App):
    def build(self):
        watchtime = gettime()
        Clock.schedule_interval(watchtime.update, 1)
        Window.clearcolor = (0,0,1,1)
        return watchtime

if __name__ == '__main__':
    DigitalwatchApp().run()

