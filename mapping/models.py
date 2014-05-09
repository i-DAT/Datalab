from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import paho.mqtt.client as paho
import json

from settings import broker

class Install(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Imp(models.Model):
    name = models.CharField(max_length=100)
    serial = models.CharField(max_length=500, unique=True)
    install = models.ForeignKey(Install)
    lat = models.DecimalField('latitude', max_digits=13, decimal_places=10)
    long = models.DecimalField('longitude', max_digits=13, decimal_places=10)
    notes = models.TextField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    #scale = models.CharField(max_length=100)
    shortcode = models.CharField(max_length=3, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Reading(models.Model):
    imp = models.ForeignKey(Imp)
    sensor = models.ForeignKey(Sensor)
    amount = models.FloatField()
    added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.imp.name + ':' + self.sensor.name


class Device(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    serial = models.CharField(max_length=500, unique=True)
    notes = models.TextField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        #return self.name + ':' + self.serial
        return self.serial


class Comment(models.Model):
    text = models.TextField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    device = models.ForeignKey(Device)

    def __unicode__(self):
        return str(self.added)


class Location(models.Model):
    device = models.ForeignKey(Device)
    lat = models.DecimalField('latitude', max_digits=13, decimal_places=10)
    long = models.DecimalField('longitude', max_digits=13, decimal_places=10)
    
    activity_choices = (
        (0,'IN_VEHICLE'),
        (1,'ON_BICYCLE'),
        (2,'ON_FOOT'),
        (3,'STILL'),
        (5,'TILTING'),
        (4,'UNKNOWN')
    )

    activity = models.IntegerField(choices=activity_choices, blank=True, null=True)
    confidence = models.IntegerField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.device.serial


#TODO - Fix serialisation issues
@receiver(post_save, sender=Location)
def new_location(sender, instance, **kwargs):

    client = paho.Client(broker.CLIENT_ID)
    client.connect(broker.ADDRESS, broker.MQTT_PORT)
    payload = {
        'id': instance.device.id,
        'name': instance.device.name,
        'lat': str(instance.lat),
        'long': str(instance.long),
        'activity': instance.activity,
        'confidence': instance.confidence,
        'added': str(instance.added),
        'type': 'location'
    }
    client.publish("datalab/map/stream", json.dumps(payload), 1)
    client.disconnect()


@receiver(pre_save, sender=Reading)
def new_reading(sender, instance, **kwargs):

    client = paho.Client(broker.CLIENT_ID)
    client.connect(broker.ADDRESS, broker.MQTT_PORT)
    payload = {
        'id': instance.imp.id,
        'serial': instance.imp.serial,
        'lat': str(instance.imp.lat),
        'long': str(instance.imp.long),
        'shortcode': instance.sensor.shortcode,
        'amount': instance.amount,
        'added': str(instance.added),
        'type': 'imp'
    }
    client.publish("datalab/map/stream", json.dumps(payload), 1)
    client.disconnect()