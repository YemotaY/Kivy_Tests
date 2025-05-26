import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
import numpy as np

kivy.require('2.1.0')  # Gebe hier deine Kivy-Version an

class GameOfLifeApp(App):
    def build(self):
        self.rows = 25
        self.cols = 50
        self.grid = np.zeros((self.rows, self.cols), dtype=int)

        # Hauptlayout als FloatLayout, damit Buttons über dem Grid erscheinen
        self.layout = FloatLayout()

        # GridLayout für das Spielfeld
        self.grid_layout = GridLayout(cols=self.cols, padding=[0, 0, 0, 0], spacing=0,
                                      size_hint=(None, None), size=(self.cols * 20, self.rows * 20))

        # Buttons für jedes Feld erstellen
        self.buttons = [[ToggleButton(size_hint=(None, None), size=(20, 20)) for _ in range(self.cols)] for _ in range(self.rows)]

        # Füge ToggleButtons zum GridLayout hinzu
        for i in range(self.rows):
            for j in range(self.cols):
                button = self.buttons[i][j]
                button.bind(on_press=self.on_button_press)
                self.grid_layout.add_widget(button)

        # Buttons für Start/Stop und Step im Overlay
        self.start_button = Button(text="Start", size_hint=(None, None), size=(100, 50))
        self.start_button.bind(on_press=self.toggle_game)
        self.start_button.pos = (10, self.rows * 20 + 10)  # Position über dem Grid
        self.layout.add_widget(self.start_button)

        self.step_button = Button(text="Step", size_hint=(None, None), size=(100, 50))
        self.step_button.bind(on_press=self.next_step)
        self.step_button.pos = (120, self.rows * 20 + 10)  # Position über dem Grid
        self.layout.add_widget(self.step_button)

        # Button für zufälliges Spielfeld
        self.random_button = Button(text="Random", size_hint=(None, None), size=(100, 50))
        self.random_button.bind(on_press=self.randomize_grid)
        self.random_button.pos = (230, self.rows * 20 + 10)  # Position über dem Grid
        self.layout.add_widget(self.random_button)

        # Füge das GridLayout zum FloatLayout hinzu
        self.layout.add_widget(self.grid_layout)

        self.game_running = False
        return self.layout

    def on_button_press(self, button):
        # Wenn der Button gedrückt wird, den Zustand umschalten
        row, col = self.get_button_position(button)
        self.grid[row][col] = 1 - self.grid[row][col]
        button.state = 'down' if self.grid[row][col] == 1 else 'normal'

    def get_button_position(self, button):
        # Findet die Position des gedrückten Buttons
        for i in range(self.rows):
            for j in range(self.cols):
                if self.buttons[i][j] == button:
                    return i, j

    def next_step(self, instance):
        # Berechnet das nächste Spielfeld
        new_grid = self.grid.copy()
        for i in range(self.rows):
            for j in range(self.cols):
                neighbors = self.count_neighbors(i, j)
                if self.grid[i][j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_grid[i][j] = 0
                elif neighbors == 3:
                    new_grid[i][j] = 1
        self.grid = new_grid
        self.update_buttons()

    def count_neighbors(self, row, col):
        # Zählt die benachbarten lebenden Zellen
        neighbors = 0
        for i in range(max(0, row - 1), min(self.rows, row + 2)):
            for j in range(max(0, col - 1), min(self.cols, col + 2)):
                if (i != row or j != col) and self.grid[i][j] == 1:
                    neighbors += 1
        return neighbors

    def update_buttons(self):
        # Aktualisiert den Zustand der Buttons basierend auf dem Grid
        for i in range(self.rows):
            for j in range(self.cols):
                button = self.buttons[i][j]
                if self.grid[i][j] == 1:
                    button.state = 'down'
                else:
                    button.state = 'normal'

    def toggle_game(self, instance):
        # Startet oder stoppt das Spiel
        self.game_running = not self.game_running
        if self.game_running:
            self.start_button.text = "Stop"
            Clock.schedule_interval(self.run_game, 0.1)
        else:
            self.start_button.text = "Start"
            Clock.unschedule(self.run_game)

    def run_game(self, dt):
        # Führt einen Schritt des Spiels aus, wenn es läuft
        self.next_step(None)

    def randomize_grid(self, instance):
        # Füllt das Grid mit zufälligen Werten (0 oder 1)
        self.grid = np.random.randint(2, size=(self.rows, self.cols))
        self.update_buttons()

    def on_touch_move(self, touch):
        # Überprüft, ob der Benutzer die Maus bewegt und gedrückt hält
        if touch.button == 'left':
            # Überprüfen, ob der Touch innerhalb des Layouts liegt
            if self.layout.collide_point(*touch.pos):
                row, col = self.get_button_by_position(touch.pos)
                if row is not None and col is not None:
                    # Umschalten des Zustands des gedrückten Buttons
                    button = self.buttons[row][col]
                    self.grid[row][col] = 1 - self.grid[row][col]
                    button.state = 'down' if self.grid[row][col] == 1 else 'normal'

    def get_button_by_position(self, pos):
        # Wandelt die Touch-Position in die Grid-Position um
        x, y = pos
        col = int(x // 20)
        row = int((self.rows * 20 - y) // 20)
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return row, col
        return None, None

if __name__ == '__main__':
    GameOfLifeApp().run()
