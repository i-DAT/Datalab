from tastypie.resources import ModelResource
from tastypie import fields
from tastypie import utils
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.validation import Validation, FormValidation
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from mapping.models import *

from tastypie.authentication import Authentication
from tastypie.http import HttpUnauthorized


class KeyOnlyAuthentication(Authentication):
    '''
    Authorises API calls using just the API Key - Likely not perfect,
    but reduces complexity for end developer.
    '''
    def _unauthorized(self):
        return HttpUnauthorized()


    def is_authenticated(self, request, **kwargs):
        from tastypie.models import ApiKey

        try:
            key = ApiKey.objects.get(key=request.GET.get('api_key'))
            request.user = key.user
        except ApiKey.DoesNotExist:
            return self._unauthorized()

        return True


class InstallResource(ModelResource):
    class Meta:
        queryset = Install.objects.all()
        authentication = KeyOnlyAuthentication()
        resource_name = 'install'
        allowed_methods = ['get','post','patch']
        always_return_data = True


class ImpResource(ModelResource):
    install = fields.ToOneField('mapping.api.resources.InstallResource', 'install')

    class Meta:
        queryset = Imp.objects.all()
        authentication = KeyOnlyAuthentication()
        resource_name = 'imp'
        allowed_methods = ['get','post','patch']
        always_return_data = True


class SensorResource(ModelResource):
    class Meta:
        queryset = Sensor.objects.all()
        authentication = KeyOnlyAuthentication()
        resource_name = 'sensor'
        allowed_methods = ['get','post','patch']
        always_return_data = True


class ReadingResource(ModelResource):
    imp = fields.ToOneField('mapping.api.resources.ImpResource', 'imp')
    sensor = fields.ToOneField('mapping.api.resources.SensorResource', 'sensor')

    class Meta:
        queryset = Reading.objects.all()
        authentication = KeyOnlyAuthentication()
        authorization = DjangoAuthorization()
        resource_name = 'reading'
        allowed_methods = ['get','post']
        always_return_data = True


class DeviceResource(ModelResource):
    class Meta:
        queryset = Device.objects.all()
        authentication = KeyOnlyAuthentication()
        authorization = DjangoAuthorization()
        resource_name = 'device'
        allowed_methods = ['get','post','patch']
        always_return_data = True


class LocationResource(ModelResource):
    device = fields.ToOneField('mapping.api.resources.DeviceResource', 'device')
    #serial = fields.CharField(attribute='serial',required=False)

    class Meta:
        queryset = Location.objects.all()
        authentication = KeyOnlyAuthentication()
        authorization = DjangoAuthorization()
        resource_name = 'location'
        allowed_methods = ['get','post']
        always_return_data = True

