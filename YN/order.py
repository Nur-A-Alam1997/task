from YN import app
from YN import socketio
from flask_socketio import SocketIO, send,emit,join_room, leave_room, ConnectionRefusedError
from flask import request, session, render_template,url_for

@app.route('/test')
def test():
    return render_template('index.html')

@app.route('/test',methods=['POST'])
def order():
    name = request.form['room']
    print(name)
    return "confirmation"



@socketio.on('connect')
def test_connect():
    print("connected",request.sid)
    emit('join', {'data': 'Connected'})

@socketio.on('order')
def test_message(message):
    order = message['room']
    join_room(order)
    print('order room',order)
    emit('kit-order', {'data': message['data']},room = order)

@socketio.on('confirmation')
def test_message(message):
    print(message['room'])
    emit('kit-confirmation', {'data': message['data']},to = message['data'])



@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')
    emit('my response', {'data': 'DisConnected'})
