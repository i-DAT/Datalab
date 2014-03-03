from django.db import models

# Create your models here.

class Camera(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Volume(models.Model):
    camera = models.ForeignKey(Camera)
    decibels = models.DecimalField(max_digits=19, decimal_places=10)
    added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.camera.name + " " + str(self.decibels)


class Motion(models.Model):
    camera = models.ForeignKey(Camera)
    x = models.IntegerField()
    y = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.camera.name + " " + str(self.x) + "/" + str(self.y)
