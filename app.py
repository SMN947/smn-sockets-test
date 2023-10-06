from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with your secret key
socketio = SocketIO(app, async_mode='gevent')


# Initialize a variable to keep track of connected clients
connected_clients = 0

@app.route("/")
def index():
    return render_template("index.html", connected_clients=connected_clients)

@socketio.on('connect')
def handle_connect():
    global connected_clients
    connected_clients += 1
    emit('update_clients_count', connected_clients, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    global connected_clients
    connected_clients -= 1
    emit('update_clients_count', connected_clients, broadcast=True)

@socketio.on('message')  # Handle incoming WebSocket messages
def handle_message(message):
    # Broadcast the received message to all connected clients
    emit('message', message, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True)
