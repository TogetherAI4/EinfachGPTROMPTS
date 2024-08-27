
```markdown
# Prompt Manager Flask App

Diese Flask-basierte Webanwendung dient zur Verwaltung und Bearbeitung von Prompts, die in einer JSON-Datei gespeichert sind. Die Anwendung ermöglicht das Anzeigen, Hinzufügen, Bearbeiten und Löschen von Prompts über eine benutzerfreundliche Oberfläche und eine REST-API.

## Projektstruktur

```
flask_app/
│
├── static/
│   ├── styles.css            # Statische CSS-Datei für das Styling
│   └── scripts.js            # Statische JavaScript-Datei für die Interaktivität
│
├── templates/
│   ├── index.html            # Hauptseite der App mit dem Prompt Manager
│   └── chat.html             # Platzhalterseite für eine Chat-Funktion
│
├── user_custom.json          # JSON-Datei mit den Prompts
├── app.py                    # Hauptanwendung in Flask
├── requirements.txt          # Python-Abhängigkeiten
└── README.md                 # Dieses README-Dokument
```

## Voraussetzungen

Stelle sicher, dass Python 3.x installiert ist. Es wird empfohlen, eine virtuelle Umgebung zu verwenden.

## Installation

1. **Repository klonen oder herunterladen**:
   ```bash
   git clone <REPOSITORY_URL>
   cd flask_app
   ```

2. **Virtuelle Umgebung erstellen**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Auf Windows: venv\Scripts\activate
   ```

3. **Abhängigkeiten installieren**:
   ```bash
   pip install -r requirements.txt
   ```

## Anwendung starten

1. **Flask-App starten**:
   ```bash
   python app.py
   ```

2. **App im Browser öffnen**:
   Gehe zu `http://localhost:5000` in deinem Webbrowser, um die App zu verwenden.

## API-Endpunkte

Die App stellt eine REST-API zur Verfügung, um die Prompts zu verwalten:

- `GET /prompts`  
  Gibt eine Liste aller Prompts zurück.

- `POST /prompts`  
  Fügt einen neuen Prompt hinzu. Erfordert JSON-Daten im Body.

- `PUT /prompts/<cmd>`  
  Aktualisiert einen bestehenden Prompt basierend auf dem `cmd`-Wert. Erfordert JSON-Daten im Body.

- `DELETE /prompts/<cmd>`  
  Löscht einen Prompt basierend auf dem `cmd`-Wert.

## Anpassung der JSON-Datei

Die Datei `user_custom.json` enthält die Prompts und kann manuell oder über die Anwendung angepasst werden. Die Struktur jedes Prompts sieht wie folgt aus:

```json
{
  "cmd": "example_command",
  "act": "example_action",
  "prompt": "example_prompt_text",
  "enable": true,
  "tags": ["tag1", "tag2"]
}
```

## Anpassung des Frontends

Die HTML-, CSS- und JavaScript-Dateien im `templates`- und `static`-Ordner können nach Belieben angepasst werden, um das Frontend-Design und die Funktionalität zu erweitern.

## Lizenz

Dieses Projekt ist unter der [MIT Lizenz](LICENSE) lizenziert.
```

### Erklärung:

- **Installation und Start**: Der Abschnitt beschreibt, wie man die App installiert, die Abhängigkeiten lädt und die App startet.
- **API-Endpunkte**: Listet die verfügbaren REST-API-Endpunkte auf.
- **JSON-Dateistruktur**: Beschreibt, wie die JSON-Datei aufgebaut ist, damit Benutzer sie verstehen und anpassen können.

Du kannst diese `README.md` direkt verwenden oder nach Belieben erweitern. Wenn du weitere Funktionen hinzufügen möchtest oder eine spezifische Anpassung benötigst, lass es mich wissen!