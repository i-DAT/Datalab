from django.db import models


class Install(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Imp(models.Model):
    name = models.CharField(max_length=100)
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
    scale = models.CharField(max_length=100)
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
    serial = models.CharField(max_length=500)
    serial = models.CharField(max_length=500, unique=True)
    notes = models.TextField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name + ':' + self.serial


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
        return self.device.name
