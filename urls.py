from django.conf.urls import patterns, include, url

from mapping.api.resources import *

from perception.api.resources import *

from tastypie.api import Api

from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(InstallResource())
v1_api.register(ImpResource())
v1_api.register(SensorResource())
v1_api.register(ReadingResource())
v1_api.register(DeviceResource())
v1_api.register(LocationResource())
v1_api.register(CameraResource())
v1_api.register(VolumeResource())
v1_api.register(MotionResource())

urlpatterns = patterns('',
    (r'^$', 'mapping.views.front_page'),
    (r'^api/', include(v1_api.urls)),
    url(r'api/doc/', include('tastypie_swagger.urls', namespace='tastypie_swagger')),

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^collector/imp/', 'mapping.api.collector.collect_imp_data'),
    url(r'^collector/get/', 'mapping.api.collector.collect_get_location'),
    url(r'^collector/', 'mapping.api.collector.collect_location'),

    url(r'^perception/result/camera/', 'perception.views.motion_result'),

)
