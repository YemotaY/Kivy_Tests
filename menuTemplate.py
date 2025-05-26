import logging
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.treeview import TreeView, TreeViewLabel, TreeViewNode
from kivy.uix.widget import Widget

logging.getLogger("kivy").setLevel(logging.CRITICAL)


class MyApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="horizontal")  # Hauptcontainer
        menu_layout = BoxLayout(
            orientation="vertical", size_hint=(0.2, 1)
        )  # Menücontainer

        # Erstellen eines TreeView-Menüs
        """
        menu_structure = {
            "root": [
                {"Home": [{"General": "funktion1"}, {"Network": "funktion2"}]},
                {"Settings": [{"Dashboard": "funktion3"}, {"Statistics": "funktion4"}]},
                {"About": "none"},
            ]
        }
        """
        tree_view = TreeView()  # Erstellen von knoten
        root_node = tree_view.add_node(TreeViewLabel(text="Root Node", is_open=True))

        # Hinzufügen von Knoten
        node_1 = tree_view.add_node(TreeViewLabel(text="Home"), root_node)
        node_2 = tree_view.add_node(TreeViewLabel(text="Settings"), root_node)
        node_3 = tree_view.add_node(TreeViewLabel(text="About"), root_node)

        # "Settings"
        settings_node_1 = tree_view.add_node(TreeViewLabel(text="General"), node_2)
        settings_node_2 = tree_view.add_node(TreeViewLabel(text="Network"), node_2)

        # "Home"
        home_node_1 = tree_view.add_node(TreeViewLabel(text="Dashboard"), node_1)
        home_node_2 = tree_view.add_node(TreeViewLabel(text="Statistics"), node_1)

        # Inhaltscontainer
        content_layout = BoxLayout(orientation="vertical", size_hint=(0.8, 1))

        # Beispielinhalt
        content_layout.add_widget(Button(text="Main Content"))

        # Hauptlayout füllen
        menu_layout.add_widget(tree_view)
        main_layout.add_widget(menu_layout)
        main_layout.add_widget(content_layout)

        return main_layout


if __name__ == "__main__":
    MyApp().run()
