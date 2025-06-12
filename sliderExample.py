# pip install kivy
import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle


class SliderApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Titel
        title = Label(text='Slider Beispiel', size_hint_y=None, height=40)
        main_layout.add_widget(title)
        
        # Horizontaler Slider
        self.h_slider = Slider(
            min=0, max=100, value=50,
            size_hint_y=None, height=30
        )
        self.h_slider.bind(value=self.on_slider_value)
        main_layout.add_widget(self.h_slider)
        
        # Label für Slider-Wert
        self.slider_label = Label(text='Wert: 50', size_hint_y=None, height=30)
        main_layout.add_widget(self.slider_label)
        
        # RGB Slider für Farbänderung
        rgb_layout = BoxLayout(orientation='vertical', spacing=10)
        
        # Rot Slider
        red_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=30)
        red_layout.add_widget(Label(text='Rot:', size_hint_x=None, width=50))
        self.red_slider = Slider(min=0, max=1, value=0.5)
        self.red_slider.bind(value=self.on_color_change)
        red_layout.add_widget(self.red_slider)
        rgb_layout.add_widget(red_layout)
        
        # Grün Slider
        green_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=30)
        green_layout.add_widget(Label(text='Grün:', size_hint_x=None, width=50))
        self.green_slider = Slider(min=0, max=1, value=0.5)
        self.green_slider.bind(value=self.on_color_change)
        green_layout.add_widget(self.green_slider)
        rgb_layout.add_widget(green_layout)
        
        # Blau Slider
        blue_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=30)
        blue_layout.add_widget(Label(text='Blau:', size_hint_x=None, width=50))
        self.blue_slider = Slider(min=0, max=1, value=0.5)
        self.blue_slider.bind(value=self.on_color_change)
        blue_layout.add_widget(self.blue_slider)
        rgb_layout.add_widget(blue_layout)
        
        main_layout.add_widget(rgb_layout)
        
        # Farbvorschau Widget
        self.color_widget = Label(text='Farbvorschau')
        main_layout.add_widget(self.color_widget)
        
        # Initiale Farbe setzen
        self.on_color_change(None, None)
        
        return main_layout
    
    def on_slider_value(self, instance, value):
        self.slider_label.text = f'Wert: {int(value)}'
    
    def on_color_change(self, instance, value):
        # Hintergrundfarbe des Color Widgets ändern
        with self.color_widget.canvas.before:
            Color(self.red_slider.value, self.green_slider.value, self.blue_slider.value, 1)
            self.color_rect = Rectangle(pos=self.color_widget.pos, size=self.color_widget.size)
        
        # Widget neu zeichnen wenn sich die Größe ändert
        self.color_widget.bind(pos=self.update_color_rect, size=self.update_color_rect)
    
    def update_color_rect(self, instance, value):
        if hasattr(self, 'color_rect'):
            self.color_rect.pos = instance.pos
            self.color_rect.size = instance.size


if __name__ == '__main__':
    SliderApp().run()
