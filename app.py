from YN import app
from YN import socketio

if __name__=="__main__":
    socketio.run(app,debug=1)