import os
import shutil
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

class InstallerApp(App):
    def build(self):
        self.selected_modules = []
        self.install_path = ""
        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        self.path_label = Label(text="Schritt 1: Wählen Sie den Installationspfad:")
        self.layout.add_widget(self.path_label)
        #Label hinzugefügt
        self.select_path_button = Button(text="Pfad auswählen", size_hint=(1, 1))
        self.select_path_button.bind(on_press=self.open_filechooser_for_path)
        self.layout.add_widget(self.select_path_button)
        #Ordnerauswahl Button hinzugefügt
        self.path_input = TextInput(hint_text="Installationspfad wird hier angezeigt", readonly=True, multiline=False)
        self.layout.add_widget(self.path_input)
        #Pfadfeld hinzugefügt
        self.next_button = Button(text="Weiter: Module auswählen", disabled=True)
        self.next_button.bind(on_press=self.go_to_module_selection)
        self.layout.add_widget(self.next_button)
        #Weiter Button hinzugefügt   
        return self.layout

    def open_filechooser_for_path(self, instance):
        # Öffnet den Dateiexplorer zum Auswählen des Installationspfads (nur Ordner)
        filechooser = FileChooserIconView(dirselect=True)  # dirselect=True für Ordnerauswahl
        filechooser.path = os.path.expanduser("~")  # Startverzeichnis (Home-Verzeichnis)

        # Erstelle einen Button, der bestätigt, dass der Ordner ausgewählt wurde
        confirm_button = Button(text="Ordner auswählen", size_hint=(1, 0.2))
        confirm_button.bind(on_press=lambda x: self.on_path_selected(filechooser.selection))

        # Erstelle ein Layout mit dem FileChooser und dem Bestätigungsbutton
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(filechooser)
        layout.add_widget(confirm_button)

        # Zeige den Popup an
        self.file_popup = Popup(title="Wählen Sie den Installationspfad", content=layout, size_hint=(1, 1))
        self.file_popup.open()

    def on_path_selected(self, selection):
        # Wenn der Benutzer einen Installationspfad (Ordner) ausgewählt hat
        if selection:
            print(f"Path selected {selection}")
            self.install_path = selection[0]
            self.path_input.text = self.install_path
            self.next_button.disabled = False
            self.file_popup.dismiss()  # Popup ablöschen

    def go_to_module_selection(self, instance):
        # Wechselt zum nächsten Schritt: Modulauswahl
        self.layout.clear_widgets()

        # Schritt 2: Module-Auswahl
        self.module_label = Label(text="Schritt 2: Wählen Sie die zu installierenden Module:")
        self.layout.add_widget(self.module_label)

        self.modules_list = BoxLayout(orientation="vertical", size_hint_y=None)
        self.modules_list.bind(minimum_height=self.modules_list.setter('height'))

        modules = ["Modul A", "Modul B", "Modul C", "Modul D"]
        for module in modules:
            checkbox = CheckBox()
            checkbox.bind(active=self.on_checkbox_active)
            module_label = Label(text=module)
            checkbox_layout = BoxLayout(orientation="horizontal")
            checkbox_layout.add_widget(checkbox)
            checkbox_layout.add_widget(module_label)
            self.modules_list.add_widget(checkbox_layout)

        self.scrollview = ScrollView(size_hint=(1, None), size=(400, 200))
        self.scrollview.add_widget(self.modules_list)
        self.layout.add_widget(self.scrollview)

        # Installieren Button
        self.install_button = Button(text="Installieren")
        self.install_button.bind(on_press=self.start_installation)
        self.layout.add_widget(self.install_button)

    def on_checkbox_active(self, checkbox, value):
        # Wenn ein Modul ausgewählt oder abgewählt wird
        module = checkbox.parent.children[1].text
        if value:
            self.selected_modules.append(module)
        else:
            self.selected_modules.remove(module)

    def start_installation(self, instance):
        if not self.install_path:
            popup = Popup(title="Fehler", content=Label(text="Bitte wählen Sie einen Installationspfad aus."), size_hint=(0.6, 0.4),size=0.2)
            popup.open()
            return

        if not self.selected_modules:
            popup = Popup(title="Fehler", content=Label(text="Bitte wählen Sie mindestens ein Modul aus."), size_hint=(0.6, 0.4),size=0.2)
            popup.open()
            return

        # Führe Installation durch (dies ist nur ein Platzhalter)
        popup = Popup(title="Installation", content=Label(text=f"Installiere {', '.join(self.selected_modules)} nach {self.install_path}..."), size_hint=(0.6, 0.4))
        popup.open()

        # Hier kannst du deine Installationslogik implementieren.
        # Zum Beispiel Kopieren von Dateien in den Installationspfad:
        # for module in self.selected_modules:
        #     shutil.copy(module, os.path.join(self.install_path, module))

        # Bei erfolgreicher Installation
        popup = Popup(title="Erfolgreich", content=Label(text="Die Installation war erfolgreich!"), size_hint=(0.6, 0.4))
        popup.open()

if __name__ == '__main__':
    InstallerApp().run()
