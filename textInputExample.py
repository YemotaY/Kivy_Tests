# pip install kivy
import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button


class TextInputApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Titel
        title = Label(text='Text Input Beispiel', size_hint_y=None, height=40)
        main_layout.add_widget(title)
        
        # Text Input Felder
        self.text_input = TextInput(
            hint_text='Geben Sie hier Text ein...',
            multiline=False,
            size_hint_y=None,
            height=40
        )
        main_layout.add_widget(self.text_input)
        
        # Mehrzeiliges Text Input
        self.multiline_input = TextInput(
            hint_text='Mehrzeiliger Text...',
            multiline=True,
            size_hint_y=None,
            height=100
        )
        main_layout.add_widget(self.multiline_input)
        
        # Button zum Anzeigen des Texts
        show_button = Button(
            text='Text anzeigen',
            size_hint_y=None,
            height=50
        )
        show_button.bind(on_press=self.show_text)
        main_layout.add_widget(show_button)
        
        # Label für die Ausgabe
        self.output_label = Label(text='Ihr Text wird hier angezeigt...', text_size=(None, None))
        main_layout.add_widget(self.output_label)
        
        return main_layout
    
    def show_text(self, instance):
        text1 = self.text_input.text
        text2 = self.multiline_input.text
        self.output_label.text = f'Einzeilig: {text1}\nMehrzeilig: {text2}'


if __name__ == '__main__':
    TextInputApp().run()
