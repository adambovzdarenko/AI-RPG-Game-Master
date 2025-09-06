'''
Hey! I would be happy if anyone uses my code for their project. Just let me know if you do, im really curious :P
Contact me: adambovzdarenko@gmail.com
I hope this spaghetti code helps someone!
'''

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from ollama import chat
import socket

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

history = []
selected_language = "English" # Basic language

AVAILABLE_LANGUAGES = ["English", "Spanish", "French", "German", "Russian"] # EXAMPLE! Gemma3 supports over 140 languages ^-^

@app.route("/")
def index():
    return render_template("index.html", languages=AVAILABLE_LANGUAGES)

@socketio.on("select_language")
def handle_language(data):
    global selected_language
    selected_language = data["language"]
    emit("language_selected", {"language": selected_language})

@socketio.on("user_message")
def handle_message(data):
    user_text = data["text"]
    history.append({"role": "user", "content": user_text})

    full_answer = ""
    system_prefix = f"You are an RPG Game Master. Language: {selected_language}. Description:" # Basic info for LLM. After the description goes first user message

    # Generation in chunks
    for chunk in chat(model="gemma3", messages=[{"role":"system","content":system_prefix}]+history, stream=True):
        if "message" in chunk and "content" in chunk["message"]:
            text = chunk["message"]["content"]
            full_answer += text
            emit("bot_stream", {"text": text}, broadcast=False)
    
    history.append({"role": "assistant", "content": full_answer})
    emit("bot_done", {"text": full_answer}, broadcast=False)

# Not important for the code, just for the console output
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # also not important
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

if __name__ == "__main__":
    ip = get_local_ip()
    port = 5000
    print(f"App running! Open on your computer: http://localhost:{port}/")
    print(f"Or open on your phone (same Wi-Fi): http://{ip}:{port}/")
    socketio.run(app, host="0.0.0.0", port=port)
