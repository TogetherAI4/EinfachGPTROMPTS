import os

# Verzeichnisstruktur
folders = [
    "flask_app",
    "flask_app/templates",
    "flask_app/static"
]

# Dateien mit ihrem jeweiligen Inhalt
files = {
    "flask_app/app.py": """\
from flask import Flask, jsonify, request, render_template
import json
import os

app = Flask(__name__)

# Pfad zur JSON-Datei
json_file_path = os.path.join(os.path.dirname(__file__), 'prompts_cleaned_and_corrected.json')

# JSON-Datei laden
with open(json_file_path, 'r', encoding='utf-8') as file:
    prompts_json = json.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prompts', methods=['GET'])
def get_prompts():
    return jsonify(prompts_json)

@app.route('/prompts', methods=['POST'])
def add_prompt():
    new_prompt = request.json
    global prompts_json
    prompts_json.append(new_prompt)
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(prompts_json, file, indent=4, ensure_ascii=False)
    return jsonify(new_prompt), 201

@app.route('/prompts/<string:id>', methods=['PUT'])
def update_prompt(id):
    updated_prompt = request.json
    global prompts_json
    for i, prompt in enumerate(prompts_json):
        if prompt['Prompt ID'] == id:
            prompts_json[i] = updated_prompt
            break
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(prompts_json, file, indent=4, ensure_ascii=False)
    return jsonify(updated_prompt)

@app.route('/prompts/<string:id>', methods=['DELETE'])
def delete_prompt(id):
    global prompts_json
    prompts_json = [prompt for prompt in prompts_json if prompt['Prompt ID'] != id]
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(prompts_json, file, indent=4, ensure_ascii=False)
    return '', 204

@app.route('/chat')
def chat():
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
""",

    "flask_app/templates/index.html": """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prompt Manager</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="{{ url_for('static', filename='scripts.js') }}"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <div class="logo">
            <img src="https://einfachalex.net/wp-content/uploads/2024/02/696f61d7a31edd36aa11414db3ba2854.png" alt="Logo">
        </div>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/prompts">Prompts</a></li>
                <li><a href="/chat">Chat</a></li>
                <li><a href="#" id="toggle-add-prompt">Add New Prompt</a></li>
            </ul>
        </nav>
    </header>
    <div class="container">
        <h1>Prompt Manager</h1>
        <div class="search-chat-container">
            <input type="text" id="search" placeholder="Search prompts...">
            <button id="search-button">Search</button>
            <form id="chat-form" class="chat-form">
                <input type="text" id="chat-input" placeholder="Type a message..." required>
                <button type="submit">Send</button>
            </form>
        </div>
        <div id="loading" class="loading">Loading...</div>
        <div class="content">
            <div id="prompt-list" class="prompt-list"></div>
            <div id="prompt-details" class="prompt-details">
                <h3>Prompt Details</h3>
                <div id="details-content"></div>
                <button id="copy-button">Copy</button>
                <button id="edit-button">Edit</button>
                <button id="save-button" style="display: none;">Save</button>
                <button id="delete-button">Delete</button>
            </div>
        </div>
        <div class="pagination">
            <button id="prev-page">Previous</button>
            <button id="next-page">Next</button>
        </div>
        <div class="bottom-section">
            <div class="add-prompt" id="add-prompt" style="display: none;">
                <h3>Add New Prompt</h3>
                <form id="add-prompt-form">
                    <input type="text" id="new-title" placeholder="Title" required>
                    <textarea id="new-prompt" rows="10" placeholder="Prompt" required></textarea>
                    <button type="submit">Add Prompt</button>
                </form>
            </div>
        </div>
    </div>
</body>
</html>
""",

    "flask_app/templates/chat.html": """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <div class="container">
        <h1>Chat Seite</h1>
        <p>Hier könnte ein interaktiver Chatbot integriert werden.</p>
        <div class="text-center">
            <a href="/" class="btn btn-secondary">Zurück zur Startseite</a>
        </div>
    </div>
</body>
</html>
""",

    "flask_app/static/styles.css": """\
body {
    background-color: #121212;
    color: #e0e0e0;
    font-family: 'Inter', sans-serif;
    margin: 0;
    padding: 0;
}

header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    background-color: #1f1f1f;
}

header .logo img {
    height: 50px;
}

nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    display: flex;
}

nav ul li {
    margin-left: 20px;
}

nav ul li a {
    text-decoration: none;
    color: #bb86fc;
    font-weight: 600;
}

nav ul li a:hover {
    color: #3700b3;
}

.container {
    padding: 20px;
    max-width: 800px;
    margin: auto;
}

h1 {
    text-align: center;
    margin-bottom: 20px;
}

.search-chat-container {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
}

input, textarea, button {
    font-family: 'Inter', sans-serif;
    padding: 10px;
    border: none;
    border-radius: 5px;
    margin-right: 10px;
}

input[type="text"], textarea {
    background-color: #2b2b2b;
    color: #e0e0e0;
    width: 100%;
}

button {
    background-color: #bb86fc;
    color: #fff;
    cursor: pointer;
}

button:hover {
    background-color: #3700b3;
}

.loading {
    text-align: center;
    display: none;
}

.content {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
}

.prompt-list {
    flex: 2;
    margin-right: 20px;
}

.prompt-details {
    flex: 1;
    background-color: #1f1f1f;
    padding: 20px;
    border-radius: 5px;
}

#add-prompt-form input, #add-prompt-form textarea {
    margin-bottom: 10px;
    width: 100%;
}

#add-prompt-form button {
    width: 100%;
}

.pagination {
    text-align: center;
    margin-top: 20px;
}

.bottom-section {
    margin-top: 40px;
}
""",

    "flask_app/static/scripts.js": """\
$(document).ready(function () {
    // Prompt hinzufügen und Formular ein- und ausblenden
    $('#toggle-add-prompt').click(function (e) {
        e.preventDefault();
        $('#add-prompt').slideToggle();
    });

    $('#add-prompt-form').submit(function (e) {
        e.preventDefault();
        // JSON Daten an die Flask-API senden
        const newPrompt = {
            "Prompt ID": Date.now().toString(),
            "Text": $('#new-prompt').val()
        };

        $.ajax({
            url: '/prompts',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(newPrompt),
            success: function (response) {
                alert('Prompt erfolgreich hinzugefügt!');
                $('#add-prompt').slideUp();
                // Hier weitere Aktionen, z.B. Liste aktualisieren
            }
        });
    });

    // Weitere Funktionalitäten können hier implementiert werden
});
""",

    "flask_app/prompts_cleaned_and_corrected.json": """\
[
    {
        "Prompt ID": "1",
        "Text": "Erstes Prompt Beispiel"
    },
    {
        "Prompt ID": "2",
        "Text": "Zweites Prompt Beispiel"
    }
]
""",

    "flask_app/requirements.txt": "Flask==2.1.1\n"
}

# Verzeichnisse erstellen
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Dateien erstellen und Inhalte schreiben
for file_path, content in files.items():
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Flask-App-Struktur erfolgreich erstellt!")
