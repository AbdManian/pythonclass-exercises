import socket
import time
HOST = 'localhost'
PORT = 34567



def frame_decoder(receiver):

    while True:
        start_seen = False
        

        # Search for start of the frame
        while not start_seen:
            data = receiver(1)
            if data == '':
                yield [] #Socket is empty. Yield back cpu to the caller
            elif data == '<':
                # Start of frame detected. Continue
                start_seen = True
        
        # Wait for frame body and end of frame
        frame_body = ''
        stop_seen = False

        while not stop_seen:
            data = receiver(1)
            if data == '':
                yield []
            elif data == '>':
                # Frame is finish
                stop_seen = True
            else:
                frame_body += data
        
        # Frame is completed here
        yield frame_body.split(',')



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



receiver = create_client_receiver(HOST, PORT)



last_frame=time.time()
last_info_display=last_frame

for frame in frame_decoder(receiver):
    if frame:
        print()
        print(frame)
        last_frame = time.time()
        last_info_display = last_frame
    else:
        cur_time=time.time()
        if cur_time - last_info_display > 0.2:  # Display elapsed time every 200 ms
            elapsed_time = cur_time - last_frame
            print(f'\rElapsed={elapsed_time:.3f} sec', sep='', end='', flush=True)
            last_info_display = cur_time
        