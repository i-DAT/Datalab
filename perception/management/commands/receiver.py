from django.core.management.base import BaseCommand, CommandError
from perception.models import *
import json

import paho.mqtt.client as mqtt

from settings import broker

def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    if msg.topic == "datalab/perception/camera/data":
        payload = json.loads(msg.payload)

        camera = Camera.objects.get(id=payload['id'])

        volume = Volume()
        volume.camera = camera
        volume.decibels = payload['loudness']
        volume.save()

        motion = Motion()
        motion.camera = camera
        motion.x = payload['motionX']
        motion.y = payload['motionY']
        motion.save()


class Command(BaseCommand):
    args = ''
    help = 'Saves data from MQTT'

    def handle(self, *args, **options):
        mqttc = mqtt.Client()
        mqttc.on_message = on_message
        mqttc.connect(broker.ADDRESS, broker.MQTT_PORT, 60)
        mqttc.subscribe("datalab/perception/camera/data", 0)
        mqttc.loop_forever()
