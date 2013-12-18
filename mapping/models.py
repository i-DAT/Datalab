from django.db import models


class Install(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Imp(models.Model):
    name = models.CharField(max_length=100)
    install = models.ForeignKey(Install)
    lat = models.DecimalField('latitude', max_digits=13, decimal_places=10)
    long = models.DecimalField('longitude', max_digits=13, decimal_places=10)
    notes = models.TextField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    scale =
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Reading(models.Model):
    imp = models.ForeignKey(Imp)
    sensor = models.ForeignKey(Sensor)
    amount =
    added = models.DateTimeField(auto_now_add=True)


class Device(models.Model):
    name = models.CharField(max_length=100)
    serial = 
    notes = models.TextField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Location(models.Model):
    Device = models.ForeignKey(Device)
    lat = models.DecimalField('latitude', max_digits=13, decimal_places=10)
    long = models.DecimalField('longitude', max_digits=13, decimal_places=10)
    activity = 
    confidence = 
    added = models.DateTimeField(auto_now_add=True)
