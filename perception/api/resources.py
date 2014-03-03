from tastypie.resources import ModelResource
from tastypie import fields
from tastypie import utils
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.validation import Validation, FormValidation
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from perception.models import *

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


class CameraResource(ModelResource):
    class Meta:
        queryset = Camera.objects.all()
        authentication = KeyOnlyAuthentication()
        resource_name = 'camera'
        allowed_methods = ['get','post']
        always_return_data = True


class VolumeResource(ModelResource):
    camera = fields.ToOneField('camera.api.resources.CameraResource', 'camera')

    class Meta:
        queryset = Volume.objects.all()
        authentication = KeyOnlyAuthentication()
        resource_name = 'volume'
        allowed_methods = ['get','post']
        always_return_data = True


class MotionResource(ModelResource):
    camera = fields.ToOneField('camera.api.resources.CameraResource', 'camera')

    class Meta:
        queryset = Motion.objects.all()
        authentication = KeyOnlyAuthentication()
        resource_name = 'motion'
        allowed_methods = ['get','post']
        always_return_data = True