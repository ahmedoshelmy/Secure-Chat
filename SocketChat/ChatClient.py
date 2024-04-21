import socketio

# Replace with the server's address and port
SERVER_ADDRESS = 'http://localhost:5000'
event_received = False  # Flag to track event reception


# Function to handle the event
def handle_server_event(data):
    """
    Callback function to handle the 'server_event' response.
    """
    global event_received
    print(f'Received server response: {data}')
    event_received = True  # Set flag to indicate event received


# Connect to the server
sio = socketio.Client(logger=True)


@sio.event
def connect():
    """
    Called upon successful connection to the server.
    """
    print('Connected to server!')
    sio.on('server_event', handle_server_event)


# Function to wait for the event
def wait_for_event():
    """
    Waits for the 'server_event' by checking the event_received flag.
    """
    global event_received
    while not event_received:
        pass  # Busy wait (not ideal for large delays)


# Continuously run the client (replace with your main loop logic)
if __name__ == '__main__':
    sio.connect(SERVER_ADDRESS)
    wait_for_event()
    # Rest of your program logic after receiving the event
    sio.wait()
