# python3.6

import os
import random
import subprocess
import time

from paho.mqtt import client as mqtt_client



broker = 'localhost'
port = 1883
topic = "obu/connect"
# generate client ID with pub prefix randomly
client_id = f'obu-connect-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


def is_port_in_use(port: int) -> bool:
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!\nwaiting from message to come...")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        if(msg.payload.decode() == 'StopDetectionAlgorithm'):
            print("Turning algo. off")
            client.publish(topic, 'AlgorithmTurnedOffSuccessfully')
        elif(msg.payload.decode() == 'StartDetectionAlgorithm'):
            print("Turning algo. on")
            client.publish(topic, 'AlgorithmTurnedOnSuccessfully')
        elif(msg.payload.decode() == 'HaltMachine'):
            print("Turing OBU Off in 3 seconds")
            client.publish(topic, 'HaltingIn3Sec')
            # os.system('sudo halt')
        elif(msg.payload.decode() == 'OpenLiveFeedHost'):
            if not is_port_in_use(80):
                print("Opening Live Feed Host")
                x = subprocess.call(['lxterminal', '-e', 'sudo python3 CAM/Live_Feed.py'])
                time.sleep(3)
                client.publish(topic, 'HostisLive')
                # client.publish(topic, 'UnableToOpenLiveFeedHost')
            else:
                 print("Live Feed Host is already open")
                 client.publish(topic, 'HostisLive')
                
    client.subscribe(topic)
    client.on_message = on_message


def run_mqtt_server():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

# if __name__ == '__main__':
#     run_mqtt_server()
