from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, send, emit



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('message')
def handle_message(data):
    sender = data["sender"]
    message = data["message"]
    print('received message from {}: {}'.format(sender, message))
    socketio.emit('message', {"sender": sender, "message": message})



if __name__ == '__main__':
    socketio.run(app, host="192.168.100.193")
