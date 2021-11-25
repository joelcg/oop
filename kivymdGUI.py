import psutil as ps
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton

KV = '''
MDScreen:
    
    MDBoxLayout:
        id: box
        orientation: "vertical"
        
        MDToolbar:
            title: "PC Monitoring"
            type: "top"
'''

class MonitoringApp(MDApp):   
    def build(self):
        
        dvmem = dict(ps.virtual_memory()._asdict())
        cpu1 = ps.cpu_percent(1)
        cpu2 = ps.cpu_percent(2)
        
        total = "CPU 1 : "+ str(cpu1) + "\n"
        total = total + "CPU 2  : "+ str(cpu2) + "\n"
        total = total + "Total Memory: "+ str(dvmem['total']) + "\n"
        total = total + "Used Memory: "+ str(dvmem['used']) + "\n"
        total = total + "Free Memory: "+ str(dvmem['free']) + "\n"
        
        screen = Builder.load_string(KV)
        screen.ids.box.add_widget(
            MDLabel(
                text = total,
                height = 50
            )
        )
        screen.ids.box.add_widget(
            MDLabel(
                text = "",
                halign = "center",
                height = 200
            )
        )
        screen.add_widget(
            MDRectangleFlatButton(
                text = "Reload", 
                pos_hint = {"center_x": 0.5}
            )
        )
        
        return screen
        
MonitoringApp().run()
