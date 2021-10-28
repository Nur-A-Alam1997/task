from flask import Flask,request, session
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, send,emit,join_room, leave_room, ConnectionRefusedError

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////YN.db'
db = SQLAlchemy(app)
socketio = SocketIO(app)

from YN import route
from YN import order
