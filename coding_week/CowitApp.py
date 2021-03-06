from picamera import PiCamera
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.camera import Camera
from camera import raspCam
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class FaceRecognition(Widget):
    pass
    def capture(self):
        print("hibade")
        app.labelResult.text = app.camOwn.recognize()
        app.manager.current = "Res"
    def add(self):
        app.camOwn.takePicture()
        app.manager.current = "Add"
    def stop(self):
        app.stop()
class Result(Widget):
    pass
    def start(self):
        app.camera._proxy_ref._camera._camera.start_preview()
        app.manager.current = "Rec"
    def stop(self):
        app.stop()
        
class Add(Widget):
    pass
    def start(self):
        app.manager.current = "Rec"
    def add(self):
        app.labelResult.text = app.camOwn.addPerson(app.input.text)
        app.manager.current = "Res"
    def stop(self):
        app.stop()

class CowitApp(App):
    def build(self):
        self.manager = ScreenManager()
        
        self.rec = FaceRecognition()
        self.camera = self.rec.children[0].children[1]
        print(self.rec.children[0].children)
        self.camOwn = raspCam(self.camera._proxy_ref._camera._camera)
        screen = Screen(name="Rec")
        screen.add_widget(self.rec)
        self.manager.add_widget(screen)
        
        self.add = Add()
        self.input = self.add.children[0]
        screen = Screen(name="Add")
        screen.add_widget(self.add)
        self.manager.add_widget(screen)
        
        self.res = Result()
        self.labelResult = self.res.children[0].children[2]
        print(self.labelResult, self.labelResult.text)
        print(self.res.children[0].children)
        screen = Screen(name="Res")
        screen.add_widget(self.res)
        self.manager.add_widget(screen)
        
        return self.manager

if __name__ == '__main__':
    Window.fullscreen = True
    Window.size=(320,240)
    Window.clearcolor = (0.62,0.82,1,1)
    app = CowitApp()
    app.run()


