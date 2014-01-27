from django.conf.urls import patterns, include, url

from mapping.api.resources import *

from tastypie.api import Api

from django.contrib import admin
admin.autodiscover()

mapping_api = Api(api_name='mapping')
mapping_api.register(InstallResource())
mapping_api.register(ImpResource())
mapping_api.register(SensorResource())
mapping_api.register(ReadingResource())
mapping_api.register(DeviceResource())
mapping_api.register(LocationResource())

urlpatterns = patterns('',
    (r'^api/', include(mapping_api.urls)),
    url(r'api/doc/', include('tastypie_swagger.urls', namespace='tastypie_swagger')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^collector/', 'mapping.api.collector.collect_location'),
)
