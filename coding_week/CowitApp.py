
from kivy.app import App
from kivy.uix.widget import Widget


class FaceRecognition(Widget):
    pass


class CowitApp(App):
    def build(self):
        return FaceRecognition()


if __name__ == '__main__':
    CowitApp().run()