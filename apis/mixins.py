import json
from django.http import HttpResponse


class JSONMixin(object):
    """
    A mixin that renders the response as JSON.
    """
    response_class = HttpResponse

    def render_to_response(self, context, **response_kwargs):
        """
        Returns json response.
        """
        response_kwargs['content_type'] = 'application/json'
        return self.response_class(
                json.dumps(context),
                **response_kwargs
                )
