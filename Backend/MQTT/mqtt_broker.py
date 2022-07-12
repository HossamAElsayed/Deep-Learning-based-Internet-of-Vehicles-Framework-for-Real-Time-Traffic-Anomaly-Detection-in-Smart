import os
import subprocess
import shlex
import paho.mqtt.client as mqtt



# os.system('mosquitto_sub -h localhost -t "obu/connect"')
process = subprocess.run(['mosquitto_sub', '-h', 'localhost', '-t', 'obu/connect'], 
                         stdout=subprocess.PIPE, 
                         universal_newlines=True)
process
