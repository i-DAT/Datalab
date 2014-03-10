from django.contrib import admin
from models import *

admin.site.register(Camera)


class MotionAdmin(admin.ModelAdmin):
    list_filter = ['camera']

class VolumeAdmin(admin.ModelAdmin):
    list_filter = ['camera']

admin.site.register(Volume, VolumeAdmin)
admin.site.register(Motion, MotionAdmin)



class MyAdmin(admin.ModelAdmin):
    actions = [export_as_xls]

admin.site.add_action(export_as_xls)