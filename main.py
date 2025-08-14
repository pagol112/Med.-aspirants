from kivy.app import App
from kivy.uix.label import Label

class SquadApp(App):
    def build(self):
        return Label(text="🔥 Squad APK Build Successful!")

if __name__ == "__main__":
    SquadApp().run()

