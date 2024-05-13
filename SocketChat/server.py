import socketio
import eventlet

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

users_count = 0


@sio.event
def connect(sid, environ):
    global users_count
    users_count += 1
    if users_count == 2:
        sio.emit('KEY_EXCHANGE', 1)

    print('Client connected:', sid)


@sio.event
def disconnect(sid):
    global users_count
    users_count -= 1
    print('Client disconnected:', sid)


@sio.event
def message(sid, data):
    print('Message received:', data)
    sio.emit('received_message', data, skip_sid=sid)


@sio.event
def ELGAMAL_PK(sid, data):
    print('ELGAMAL_PK received from', sid, ':', data)
    sio.emit('ELGAMAL_PK_BC', data, skip_sid=sid)


@sio.event
def DIFF_HELLMAN_PK(sid, data):
    print('DIFF_HELLMAN_PK received:', data)
    sio.emit('DIFF_HELLMAN_PK_BC', data, skip_sid=sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
