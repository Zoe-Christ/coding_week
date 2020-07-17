
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
        self.camera = Camera(play= True,resolution= (640,960), size= (160,240))
        self.camOwn = raspCam(self.camera._proxy_ref._camera._camera)
        screen = Screen(name="Rec")
        self.rec.add_widget(self.camera)
        screen.add_widget(self.rec)
        self.manager.add_widget(screen)
        
        self.add = Add()
        self.input = TextInput(multiline= False,center_x= self.add.width /2,center_y= self.add.height / 3,height= 30,font_size= 20,focus= True)
        self.add.add_widget(self.input)
        screen = Screen(name="Add")
        screen.add_widget(self.add)
        self.manager.add_widget(screen)
        
        self.res = Result()
        self.labelResult = Label(font_size = 70,  center_x=self.res.width / 4, center_y= 5, top= self.res.top - 50, text= "Result", color = (0,0.11,0.74,1))
        self.res.add_widget(self.labelResult)
        screen = Screen(name="Res")
        screen.add_widget(self.res)
        self.manager.add_widget(screen)
        
        return self.manager

if __name__ == '__main__':
    Window.fullscreen = True
    Window.clearcolor = (0.62,0.82,1,1)
    app = CowitApp()
    app.run()


