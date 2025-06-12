# Kivy Boilerplate

Dieses Repository enthält Beispiel- und Template-Dateien für Kivy-Anwendungen.

## Dateien

### Grundlegende Beispiele
- `simpleLabel.py`: Einfaches Label-Beispiel mit Kivy.
- `textInputExample.py`: Beispiel für Texteingabe mit verschiedenen TextInput-Widgets.
- `sliderExample.py`: Slider-Widgets und Farbänderung mit RGB-Slidern.
- `popupExample.py`: Verschiedene Arten von Popup-Fenstern (Info, Eingabe, Bestätigung).

### UI-Komponenten
- `floatingButton.py`: Beispiel für eine schwebende Schaltfläche in Kivy.
- `listViewExample.py`: ListView mit dynamischem Hinzufügen und Löschen von Einträgen.
- `progressBarExample.py`: Progress Bars (bestimmt und unbestimmt) mit Threading.
- `tabsExample.py`: Tab-Navigation mit verschiedenen Inhalten (Formular, Einstellungen).

### Erweiterte Beispiele
- `canvasExample.py`: Zeichnen auf Canvas mit Pinsel, Farben und zufälligen Formen.
- `conway.py`: Beispiel für eine Kivy-Anwendung (Conway's Game of Life).
- `menuTemplate.py`: Vorlage für ein Menü in Kivy mit TreeView.
- `installerTemplate.py`: Vorlage für einen Installer mit Kivy.

## Beispiel-Beschreibungen

### Grundlegende Widgets
- **simpleLabel.py**: Zeigt ein einfaches Label-Widget
- **textInputExample.py**: Demonstriert einzeilige und mehrzeilige Texteingabe
- **sliderExample.py**: Slider-Widgets für Werte und RGB-Farbmischung

### Interaktive Elemente
- **popupExample.py**: Verschiedene Popup-Typen (Information, Eingabe, Bestätigung)
- **listViewExample.py**: Dynamische Liste mit Hinzufügen/Löschen-Funktionalität
- **progressBarExample.py**: Fortschrittsbalken mit Threading für Hintergrundprozesse

### Layout und Navigation
- **tabsExample.py**: Tab-basierte Navigation mit Formular und Einstellungen
- **menuTemplate.py**: TreeView-basiertes Menüsystem
- **floatingButton.py**: Material Design schwebende Buttons (erfordert kivymd)

### Grafik und Zeichnen
- **canvasExample.py**: Zeichenanwendung mit Canvas, verschiedenen Pinseln und Farben
- **conway.py**: Conway's Game of Life Implementation

### Templates
- **installerTemplate.py**: Grundgerüst für Installer-Anwendungen

## Nutzung

1. **Virtuelle Umgebung anlegen (optional):**
   ```powershell
   python -m venv venvKivy
   .\venvKivy\Scripts\Activate.ps1
   ```
2. **Kivy installieren:**
   ```powershell
   pip install kivy
   ```
   
   **Für erweiterte Funktionen (MDFloatingActionButton):**
   ```powershell
   pip install kivymd
   ```
3. **Beispiel ausführen:**
   ```powershell
   python <dateiname.py>
   ```

## Hinweise

- Die Dateien dienen als Ausgangspunkt für eigene Kivy-Projekte.
- Für weiterführende Informationen siehe die [Kivy Dokumentation](https://kivy.org/doc/stable/).
