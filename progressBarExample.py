# pip install kivy
import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import threading
import time


class ProgressBarApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Titel
        title = Label(text='Progress Bar Beispiel', size_hint_y=None, height=40)
        main_layout.add_widget(title)
        
        # Einfache Progress Bar
        self.simple_progress = ProgressBar(max=100, value=0, size_hint_y=None, height=30)
        main_layout.add_widget(self.simple_progress)
        
        # Label für Progress Anzeige
        self.progress_label = Label(text='0%', size_hint_y=None, height=30)
        main_layout.add_widget(self.progress_label)
        
        # Buttons für Progress Control
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        
        start_btn = Button(text='Start Progress')
        start_btn.bind(on_press=self.start_progress)
        button_layout.add_widget(start_btn)
        
        reset_btn = Button(text='Reset')
        reset_btn.bind(on_press=self.reset_progress)
        button_layout.add_widget(reset_btn)
        
        fast_btn = Button(text='Schnell füllen')
        fast_btn.bind(on_press=self.fast_fill)
        button_layout.add_widget(fast_btn)
        
        main_layout.add_widget(button_layout)
        
        # Unbestimmte Progress Bar (spinning)
        main_layout.add_widget(Label(text='Unbestimmter Progress:', size_hint_y=None, height=30))
        
        self.infinite_progress = ProgressBar(max=100, size_hint_y=None, height=30)
        main_layout.add_widget(self.infinite_progress)
        
        # Button für unbestimmten Progress
        infinite_button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        
        self.infinite_btn = Button(text='Unbestimmten Progress starten')
        self.infinite_btn.bind(on_press=self.toggle_infinite_progress)
        infinite_button_layout.add_widget(self.infinite_btn)
        
        main_layout.add_widget(infinite_button_layout)
        
        # Status Label
        self.status_label = Label(text='Bereit...', size_hint_y=None, height=30)
        main_layout.add_widget(self.status_label)
        
        # Variablen für Progress Control
        self.progress_active = False
        self.infinite_active = False
        self.progress_event = None
        self.infinite_event = None
        
        return main_layout
    
    def start_progress(self, instance):
        if not self.progress_active:
            self.progress_active = True
            self.simple_progress.value = 0
            self.status_label.text = 'Progress gestartet...'
            
            # Simuliere längeren Prozess in separatem Thread
            def progress_worker():
                for i in range(101):
                    if not self.progress_active:
                        break
                    # UI Update muss im Hauptthread passieren
                    Clock.schedule_once(lambda dt, val=i: self.update_progress(val), 0)
                    time.sleep(0.05)  # Simuliere Arbeit
                
                Clock.schedule_once(lambda dt: self.progress_finished(), 0)
            
            thread = threading.Thread(target=progress_worker)
            thread.daemon = True
            thread.start()
    
    def update_progress(self, value):
        self.simple_progress.value = value
        self.progress_label.text = f'{value}%'
    
    def progress_finished(self):
        self.progress_active = False
        self.status_label.text = 'Progress abgeschlossen!'
    
    def reset_progress(self, instance):
        self.progress_active = False
        self.simple_progress.value = 0
        self.progress_label.text = '0%'
        self.status_label.text = 'Progress zurückgesetzt'
    
    def fast_fill(self, instance):
        self.progress_active = False
        self.simple_progress.value = 100
        self.progress_label.text = '100%'
        self.status_label.text = 'Progress sofort gefüllt'
    
    def toggle_infinite_progress(self, instance):
        if not self.infinite_active:
            self.infinite_active = True
            self.infinite_btn.text = 'Unbestimmten Progress stoppen'
            self.status_label.text = 'Unbestimmter Progress läuft...'
            
            # Animiere unbestimmten Progress
            def animate_infinite(dt):
                if self.infinite_active:
                    current = self.infinite_progress.value
                    current += 2
                    if current > self.infinite_progress.max:
                        current = 0
                    self.infinite_progress.value = current
                    return True  # Wiederhole
                return False  # Stoppe
            
            self.infinite_event = Clock.schedule_interval(animate_infinite, 0.05)
        else:
            self.infinite_active = False
            self.infinite_btn.text = 'Unbestimmten Progress starten'
            self.status_label.text = 'Unbestimmter Progress gestoppt'
            if self.infinite_event:
                self.infinite_event.cancel()
            self.infinite_progress.value = 0


if __name__ == '__main__':
    ProgressBarApp().run()
