# pip install kivy
import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch


class TabsApp(App):
    def build(self):
        # Hauptcontainer für Tabs
        tab_panel = TabbedPanel(do_default_tab=False)
        
        # Tab 1: Willkommen
        welcome_tab = TabbedPanelItem(text='Willkommen')
        welcome_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        welcome_layout.add_widget(Label(
            text='Willkommen bei der Tabs Demo!',
            font_size=24,
            size_hint_y=None,
            height=50
        ))
        welcome_layout.add_widget(Label(
            text='Diese Anwendung demonstriert die Verwendung von Tabs in Kivy.\n'
                 'Klicken Sie auf die verschiedenen Tabs oben, um deren Inhalte zu erkunden.',
            text_size=(None, None),
            halign='center'
        ))
        
        welcome_tab.content = welcome_layout
        tab_panel.add_widget(welcome_tab)
        
        # Tab 2: Eingabe Formular
        form_tab = TabbedPanelItem(text='Formular')
        form_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        form_layout.add_widget(Label(text='Benutzer Informationen', font_size=20, size_hint_y=None, height=40))
        
        # Name Eingabe
        name_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        name_layout.add_widget(Label(text='Name:', size_hint_x=None, width=100))
        self.name_input = TextInput(hint_text='Ihr Name...')
        name_layout.add_widget(self.name_input)
        form_layout.add_widget(name_layout)
        
        # Email Eingabe
        email_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        email_layout.add_widget(Label(text='Email:', size_hint_x=None, width=100))
        self.email_input = TextInput(hint_text='ihre.email@beispiel.de')
        email_layout.add_widget(self.email_input)
        form_layout.add_widget(email_layout)
        
        # Alter Slider
        age_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        age_layout.add_widget(Label(text='Alter:', size_hint_x=None, width=100))
        self.age_slider = Slider(min=18, max=100, value=25)
        age_layout.add_widget(self.age_slider)
        self.age_label = Label(text='25', size_hint_x=None, width=50)
        age_layout.add_widget(self.age_label)
        form_layout.add_widget(age_layout)
        
        self.age_slider.bind(value=self.on_age_change)
        
        # Newsletter Switch
        newsletter_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        newsletter_layout.add_widget(Label(text='Newsletter:', size_hint_x=None, width=100))
        self.newsletter_switch = Switch()
        newsletter_layout.add_widget(self.newsletter_switch)
        form_layout.add_widget(newsletter_layout)
        
        # Submit Button
        submit_btn = Button(text='Absenden', size_hint_y=None, height=50)
        submit_btn.bind(on_press=self.submit_form)
        form_layout.add_widget(submit_btn)
        
        # Ausgabe Label
        self.form_output = Label(text='Füllen Sie das Formular aus und klicken Sie auf Absenden.')
        form_layout.add_widget(self.form_output)
        
        form_tab.content = form_layout
        tab_panel.add_widget(form_tab)
        
        # Tab 3: Einstellungen
        settings_tab = TabbedPanelItem(text='Einstellungen')
        settings_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        settings_layout.add_widget(Label(text='Anwendungseinstellungen', font_size=20, size_hint_y=None, height=40))
        
        # Theme Switch
        theme_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        theme_layout.add_widget(Label(text='Dunkles Theme:', size_hint_x=None, width=150))
        self.theme_switch = Switch()
        theme_layout.add_widget(self.theme_switch)
        settings_layout.add_widget(theme_layout)
        
        # Lautstärke Slider
        volume_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        volume_layout.add_widget(Label(text='Lautstärke:', size_hint_x=None, width=150))
        self.volume_slider = Slider(min=0, max=100, value=50)
        volume_layout.add_widget(self.volume_slider)
        self.volume_label = Label(text='50%', size_hint_x=None, width=50)
        volume_layout.add_widget(self.volume_label)
        settings_layout.add_widget(volume_layout)
        
        self.volume_slider.bind(value=self.on_volume_change)
        
        # Auto-Save Switch
        autosave_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        autosave_layout.add_widget(Label(text='Auto-Speichern:', size_hint_x=None, width=150))
        self.autosave_switch = Switch(active=True)
        autosave_layout.add_widget(self.autosave_switch)
        settings_layout.add_widget(autosave_layout)
        
        # Reset Button
        reset_btn = Button(text='Einstellungen zurücksetzen', size_hint_y=None, height=50)
        reset_btn.bind(on_press=self.reset_settings)
        settings_layout.add_widget(reset_btn)
        
        # Settings Status
        self.settings_status = Label(text='Einstellungen geladen.')
        settings_layout.add_widget(self.settings_status)
        
        settings_tab.content = settings_layout
        tab_panel.add_widget(settings_tab)
        
        # Tab 4: Info
        info_tab = TabbedPanelItem(text='Info')
        info_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        info_layout.add_widget(Label(
            text='Über diese Anwendung',
            font_size=20,
            size_hint_y=None,
            height=40
        ))
        
        info_layout.add_widget(Label(
            text='Dies ist eine Beispielanwendung für Kivy Tabs.\n\n'
                 'Features:\n'
                 '• Mehrere Tabs mit verschiedenen Inhalten\n'
                 '• Formulareingabe mit verschiedenen Widgets\n'
                 '• Einstellungsseite mit Switches und Slidern\n'
                 '• Responsive Design\n\n'
                 'Entwickelt mit Kivy Framework',
            text_size=(None, None),
            halign='left'
        ))
        
        version_btn = Button(text='Version anzeigen', size_hint_y=None, height=40)
        version_btn.bind(on_press=self.show_version)
        info_layout.add_widget(version_btn)
        
        self.version_label = Label(text='')
        info_layout.add_widget(self.version_label)
        
        info_tab.content = info_layout
        tab_panel.add_widget(info_tab)
        
        return tab_panel
    
    def on_age_change(self, instance, value):
        self.age_label.text = str(int(value))
    
    def on_volume_change(self, instance, value):
        self.volume_label.text = f'{int(value)}%'
    
    def submit_form(self, instance):
        name = self.name_input.text
        email = self.email_input.text
        age = int(self.age_slider.value)
        newsletter = self.newsletter_switch.active
        
        if name and email:
            newsletter_text = 'Ja' if newsletter else 'Nein'
            self.form_output.text = (
                f'Formular abgesendet!\n\n'
                f'Name: {name}\n'
                f'Email: {email}\n'
                f'Alter: {age}\n'
                f'Newsletter: {newsletter_text}'
            )
        else:
            self.form_output.text = 'Bitte füllen Sie alle Pflichtfelder aus!'
    
    def reset_settings(self, instance):
        self.theme_switch.active = False
        self.volume_slider.value = 50
        self.autosave_switch.active = True
        self.settings_status.text = 'Einstellungen wurden zurückgesetzt.'
    
    def show_version(self, instance):
        self.version_label.text = 'Version 1.0.0\nKivy Tabs Demo\nErstellt mit Python und Kivy'


if __name__ == '__main__':
    TabsApp().run()
