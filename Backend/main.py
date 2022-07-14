import sys
import threading

from bluetooth import *
from BT.bluetooth import bt_init
from MQTT.mqtt_subscribe import run_mqtt_server

sys.path.insert(0, '/home/pi/Documents/DB/')

from DB.modify import *

# Main Driver 
if __name__ == "__main__":
    print("OBU is Online ... ")
    run_mqtt_server()
