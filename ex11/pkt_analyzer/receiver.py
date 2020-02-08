import socket
HOST = 'localhost'
PORT = 34567

# Display content of the received frames in form of :
#   ['PARAM1=Value', 'PARAM2=Value', .....]


def create_client_receiver(host, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.setblocking(False)

    def _receiver(num_bytes=1, ):
        try:
            data = s.recv(num_bytes)
        except socket.error as e:
            return ''
        
        if data=='':
            print("Connection closed!")
            exit(-1)
            return ''
        
        return data.decode()
    
    return _receiver

def _show_received_data(receiver):
    while True:
        rcv_data = receiver(num_bytes=1)
        if rcv_data:
            print(rcv_data, end='', sep='', flush=True)

receiver = create_client_receiver(HOST, PORT)

_show_received_data(receiver)