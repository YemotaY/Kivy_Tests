# pip install kivy
import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListView
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton


class ListViewApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Titel
        title = Label(text='ListView Beispiel', size_hint_y=None, height=40)
        main_layout.add_widget(title)
        
        # Input Bereich
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        
        self.text_input = TextInput(hint_text='Neuen Eintrag hinzufügen...')
        input_layout.add_widget(self.text_input)
        
        add_button = Button(text='Hinzufügen', size_hint_x=None, width=100)
        add_button.bind(on_press=self.add_item)
        input_layout.add_widget(add_button)
        
        main_layout.add_widget(input_layout)
        
        # Lösch-Button
        delete_button = Button(text='Ausgewählten Eintrag löschen', size_hint_y=None, height=40)
        delete_button.bind(on_press=self.delete_item)
        main_layout.add_widget(delete_button)
        
        # Liste von Einträgen
        self.items = ['Beispiel Eintrag 1', 'Beispiel Eintrag 2', 'Beispiel Eintrag 3']
        
        # ListView mit Adapter erstellen
        self.list_adapter = ListAdapter(
            data=self.items,
            cls=ListItemButton,
            selection_mode='single',
            allow_empty_selection=False
        )
        
        self.list_view = ListView(adapter=self.list_adapter)
        main_layout.add_widget(self.list_view)
        
        # Status Label
        self.status_label = Label(text='Bereit...', size_hint_y=None, height=30)
        main_layout.add_widget(self.status_label)
        
        return main_layout
    
    def add_item(self, instance):
        new_item = self.text_input.text.strip()
        if new_item:
            self.items.append(new_item)
            self.list_adapter.data = self.items[:]  # Liste aktualisieren
            self.text_input.text = ''
            self.status_label.text = f'"{new_item}" hinzugefügt'
        else:
            self.status_label.text = 'Bitte geben Sie einen Text ein'
    
    def delete_item(self, instance):
        if self.list_adapter.selection:
            selected_item = self.list_adapter.selection[0].text
            self.items.remove(selected_item)
            self.list_adapter.data = self.items[:]  # Liste aktualisieren
            self.status_label.text = f'"{selected_item}" gelöscht'
        else:
            self.status_label.text = 'Bitte wählen Sie einen Eintrag aus'


if __name__ == '__main__':
    ListViewApp().run()
