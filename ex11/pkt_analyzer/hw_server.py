import socket
import time
import random

HOST = 'localhost'
PORT = 34567


sensor_list = [
    'engine1',
    'valve_left',
    'valve_right',
    'temp_a',
    'temp_b',
    'rssi',
    'light-meter',
    'backup_motor',
    'generator_01'
]



def single_sample_generator(sensors=sensor_list, value_range=10.0, msg_id=0):
    num_fields = random.randint(1,len(sensors))

    selected_sensors = set(
        random.choices(sensors, k=random.randint(1,len(sensors)))
    )

    sensor_data_list = [f'msg_id={msg_id}']
    for sensor in selected_sensors:
        value = value_range * (random.random() * 2.0 - 1.0)
        sensor_data_list.append(
            f'{sensor}={value:.3f}'
        )

    return "<" + ",".join(sensor_data_list) + ">"


def traffic_generator():
    msg_id = 0
    while True:
        time_to_next_send_ms = random.randint(200, 4000)

        # apply wait time and send "." each 400ms
        while time_to_next_send_ms>0:
            wait_time_ms = min(time_to_next_send_ms, 400)
            time.sleep(wait_time_ms / 1000)
            yield "."
            time_to_next_send_ms -= wait_time_ms
        

        msg = single_sample_generator(msg_id=msg_id)

        for c in msg:
            time.sleep(random.randint(0,50)/1000)
            yield c

        msg_id +=1

def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        print(f"Listen on {port} ...")
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by ', addr)
            while True:
                for message in traffic_generator():
                    b_message = message.encode()
                    conn.sendall(b_message)





def start_app():
    while True:
        try:
            start_server(HOST, PORT)
        except BrokenPipeError:
            print("Connection is closed by client. Try to restart....")
        except KeyboardInterrupt:
            print("\nHW server closed by user....")
            break

start_app()
