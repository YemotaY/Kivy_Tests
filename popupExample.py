# pip install kivy
import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class PopupApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Titel
        title = Label(text='Popup Beispiele', size_hint_y=None, height=40)
        main_layout.add_widget(title)
        
        # Button für einfaches Popup
        simple_popup_btn = Button(text='Einfaches Popup öffnen', size_hint_y=None, height=50)
        simple_popup_btn.bind(on_press=self.show_simple_popup)
        main_layout.add_widget(simple_popup_btn)
        
        # Button für Eingabe Popup
        input_popup_btn = Button(text='Eingabe Popup öffnen', size_hint_y=None, height=50)
        input_popup_btn.bind(on_press=self.show_input_popup)
        main_layout.add_widget(input_popup_btn)
        
        # Button für Bestätigungs Popup
        confirm_popup_btn = Button(text='Bestätigungs Popup öffnen', size_hint_y=None, height=50)
        confirm_popup_btn.bind(on_press=self.show_confirm_popup)
        main_layout.add_widget(confirm_popup_btn)
        
        # Status Label
        self.status_label = Label(text='Klicken Sie auf einen Button...', text_size=(None, None))
        main_layout.add_widget(self.status_label)
        
        return main_layout
    
    def show_simple_popup(self, instance):
        # Einfaches Popup mit nur einem OK Button
        content = BoxLayout(orientation='vertical', spacing=10)
        content.add_widget(Label(text='Dies ist ein einfaches Popup!'))
        
        close_btn = Button(text='Schließen', size_hint_y=None, height=40)
        content.add_widget(close_btn)
        
        popup = Popup(
            title='Information',
            content=content,
            size_hint=(0.6, 0.4)
        )
        
        close_btn.bind(on_press=popup.dismiss)
        popup.open()
        
        self.status_label.text = 'Einfaches Popup wurde geöffnet'
    
    def show_input_popup(self, instance):
        # Popup mit Texteingabe
        content = BoxLayout(orientation='vertical', spacing=10)
        content.add_widget(Label(text='Geben Sie Ihren Namen ein:'))
        
        text_input = TextInput(hint_text='Name...', multiline=False, size_hint_y=None, height=40)
        content.add_widget(text_input)
        
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        ok_btn = Button(text='OK')
        cancel_btn = Button(text='Abbrechen')
        button_layout.add_widget(cancel_btn)
        button_layout.add_widget(ok_btn)
        content.add_widget(button_layout)
        
        popup = Popup(
            title='Name eingeben',
            content=content,
            size_hint=(0.6, 0.5)
        )
        
        def on_ok(btn_instance):
            name = text_input.text.strip()
            if name:
                self.status_label.text = f'Hallo {name}!'
            else:
                self.status_label.text = 'Kein Name eingegeben'
            popup.dismiss()
        
        def on_cancel(btn_instance):
            self.status_label.text = 'Eingabe abgebrochen'
            popup.dismiss()
        
        ok_btn.bind(on_press=on_ok)
        cancel_btn.bind(on_press=on_cancel)
        
        popup.open()
    
    def show_confirm_popup(self, instance):
        # Bestätigungs Popup
        content = BoxLayout(orientation='vertical', spacing=10)
        content.add_widget(Label(text='Sind Sie sicher, dass Sie fortfahren möchten?'))
        
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        yes_btn = Button(text='Ja')
        no_btn = Button(text='Nein')
        button_layout.add_widget(no_btn)
        button_layout.add_widget(yes_btn)
        content.add_widget(button_layout)
        
        popup = Popup(
            title='Bestätigung',
            content=content,
            size_hint=(0.5, 0.3)
        )
        
        def on_yes(btn_instance):
            self.status_label.text = 'Aktion bestätigt!'
            popup.dismiss()
        
        def on_no(btn_instance):
            self.status_label.text = 'Aktion abgebrochen'
            popup.dismiss()
        
        yes_btn.bind(on_press=on_yes)
        no_btn.bind(on_press=on_no)
        
        popup.open()


if __name__ == '__main__':
    PopupApp().run()
