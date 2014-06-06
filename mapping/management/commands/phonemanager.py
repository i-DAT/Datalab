from django.core.management.base import BaseCommand, CommandError

import paho.mqtt.client as mqtt

from settings import broker

from settings import base_number

import threading

import json
import random

count = 0
threshold = 11
mqttc = mqtt.Client()
devices = []

def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    #if msg.topic == "datalab/perception/camera/data":
    global count

    if msg.topic == "datalab/telephone/collector":
        devices.append(json.loads(msg.payload))
        print devices
    
    if msg.topic == "datalab/telephone":
        
        count+= 1
        print count

    if count >= threshold:
        print 'dialing'
        count = 0

        while len(devices) > 0:
            print devices
            if len(devices) == 1:
                caller = devices.pop()
                mqttc.publish("datalab/telephone/"+caller['serial'], base_number.LEE_NUMBER)
            else:
                caller = devices.pop(random.randint(0,(len(devices)-1)))
                receiver = devices.pop(random.randint(0,(len(devices)-1)))
                mqttc.publish("datalab/telephone/"+str(caller['serial']), str(receiver['number']))


        #mqttc.publish("datalab/telephone", base_number.LEE_NUMBER)


class Command(BaseCommand):
    args = ''
    help = 'Manages Lee Nutbean\'s phone installation'

    def handle(self, *args, **options):

        #context = zmq.Context()
        #sock = context.socket(zmq.REP)
        #sock.bind("tcp://*:5678")
        
        
        mqttc.on_message = on_message
        mqttc.connect(broker.ADDRESS, broker.MQTT_PORT, 60)
        mqttc.subscribe("datalab/telephone/#", 0)
        mqttc.loop_forever()

        while True:
            message = socket.recv()
            print("received: " + str(message))
