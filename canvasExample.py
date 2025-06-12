# pip install kivy
import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.uix.slider import Slider
import random


class PaintWidget(Widget):
    def __init__(self, **kwargs):
        super(PaintWidget, self).__init__(**kwargs)
        self.brush_size = 5
        self.brush_color = [1, 0, 0, 1]  # Rot als Standard
        
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            with self.canvas:
                Color(*self.brush_color)
                d = self.brush_size
                Ellipse(pos=(touch.pos[0] - d / 2, touch.pos[1] - d / 2), size=(d, d))
                touch.ud['line'] = Line(points=[touch.pos[0], touch.pos[1]], width=self.brush_size)
            return True
        return False
    
    def on_touch_move(self, touch):
        if 'line' in touch.ud and self.collide_point(*touch.pos):
            touch.ud['line'].points += [touch.pos[0], touch.pos[1]]
            return True
        return False
    
    def clear_canvas(self):
        self.canvas.clear()
    
    def set_brush_size(self, size):
        self.brush_size = size
    
    def set_brush_color(self, color):
        self.brush_color = color


class CanvasApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical')
        
        # Titel und Controls
        controls_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=100, padding=10, spacing=10)
        
        # Pinselgröße Control
        size_layout = BoxLayout(orientation='vertical', size_hint_x=None, width=150)
        size_layout.add_widget(Label(text='Pinselgröße:', size_hint_y=None, height=30))
        self.size_slider = Slider(min=1, max=20, value=5, size_hint_y=None, height=30)
        self.size_slider.bind(value=self.on_size_change)
        size_layout.add_widget(self.size_slider)
        self.size_label = Label(text='5', size_hint_y=None, height=30)
        size_layout.add_widget(self.size_label)
        controls_layout.add_widget(size_layout)
        
        # Farb-Buttons
        color_layout = BoxLayout(orientation='horizontal', spacing=5)
        
        # Vordefinierte Farben
        colors = [
            ([1, 0, 0, 1], 'Rot'),
            ([0, 1, 0, 1], 'Grün'),
            ([0, 0, 1, 1], 'Blau'),
            ([1, 1, 0, 1], 'Gelb'),
            ([1, 0, 1, 1], 'Magenta'),
            ([0, 1, 1, 1], 'Cyan'),
            ([0, 0, 0, 1], 'Schwarz')
        ]
        
        for color, name in colors:
            btn = Button(text=name, size_hint_x=None, width=60)
            btn.bind(on_press=lambda x, c=color: self.set_color(c))
            color_layout.add_widget(btn)
        
        controls_layout.add_widget(color_layout)
        
        # Action Buttons
        action_layout = BoxLayout(orientation='vertical', size_hint_x=None, width=100)
        
        clear_btn = Button(text='Löschen', size_hint_y=None, height=40)
        clear_btn.bind(on_press=self.clear_canvas)
        action_layout.add_widget(clear_btn)
        
        random_btn = Button(text='Zufällig', size_hint_y=None, height=40)
        random_btn.bind(on_press=self.draw_random)
        action_layout.add_widget(random_btn)
        
        controls_layout.add_widget(action_layout)
        
        main_layout.add_widget(controls_layout)
        
        # Zeichenfläche
        self.paint_widget = PaintWidget()
        
        # Hintergrund für die Zeichenfläche
        with self.paint_widget.canvas.before:
            Color(1, 1, 1, 1)  # Weiß
            self.bg_rect = Rectangle(pos=self.paint_widget.pos, size=self.paint_widget.size)
        
        self.paint_widget.bind(pos=self.update_bg, size=self.update_bg)
        
        main_layout.add_widget(self.paint_widget)
        
        return main_layout
    
    def update_bg(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size
    
    def on_size_change(self, instance, value):
        self.paint_widget.set_brush_size(int(value))
        self.size_label.text = str(int(value))
    
    def set_color(self, color):
        self.paint_widget.set_brush_color(color)
    
    def clear_canvas(self, instance):
        self.paint_widget.clear_canvas()
        # Hintergrund neu zeichnen
        with self.paint_widget.canvas.before:
            Color(1, 1, 1, 1)
            self.bg_rect = Rectangle(pos=self.paint_widget.pos, size=self.paint_widget.size)
    
    def draw_random(self, instance):
        # Zeichne zufällige Formen
        with self.paint_widget.canvas:
            for _ in range(10):
                # Zufällige Farbe
                Color(random.random(), random.random(), random.random(), 1)
                
                # Zufällige Position und Größe
                x = random.randint(0, int(self.paint_widget.width - 50))
                y = random.randint(0, int(self.paint_widget.height - 50))
                size = random.randint(10, 50)
                
                # Zeichne Kreis oder Rechteck
                if random.choice([True, False]):
                    Ellipse(pos=(x, y), size=(size, size))
                else:
                    Rectangle(pos=(x, y), size=(size, size))


if __name__ == '__main__':
    CanvasApp().run()
