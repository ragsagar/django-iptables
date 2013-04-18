import json
import base64

from django.http import HttpResponse
from django.contrib.auth import authenticate


class BasicAuthRequiredMixin(object):
    """
    A mixin that will make sure the request is authenticated using BasicAuth.
    """
    def unauthorized(self):
        """
        Return HttpUnauthorized with stuffs needed for basicauth.
        """
        response = HttpResponse()
        response.status_code = 401
        response['WWW-Authenticate'] = 'Basic Realm="djit"'
        return response

    def dispatch(self, request, *args, **kwargs):
        """
        Check for BasicAuth.
        """
        if not request.META.get('HTTP_AUTHORIZATION'):
            return self.unauthorized()

        try:
            (auth_type, data) = request.META['HTTP_AUTHORIZATION'].split()
            if auth_type.lower() != 'basic':
                return self.unauthorized()
            user_pass = base64.b64decode(data)
        except:
            return self.unauthorized()

        try:
            username, password = user_pass.split(':', 1)
        except ValueError:
            return self.unauthorized()

        user = authenticate(username=username, password=password)
        if user is None or not user.is_active:
            return self.unauthorized()

        request.user = user

        return super(BasicAuthRequiredMixin, self).dispatch(
                        request,
                        *args,
                        **kwargs)


