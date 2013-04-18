import json
import subprocess

from django.http import HttpResponse
from django.views.generic.base import View

from braces.views import JSONResponseMixin, CsrfExemptMixin

from .mixins import BasicAuthRequiredMixin
from .helpers import parse_parameters


class IptablesReadandWriteView(CsrfExemptMixin,
                               BasicAuthRequiredMixin,
                               JSONResponseMixin,
                               View):
    """
    Serves post and get request on /api/iptables/
    """
    def get(self, request):
        """
        Return the existing iptables rules.
        """
        p = subprocess.Popen(['sudo', 'iptables', '-nvL'],
                                  stdout=subprocess.PIPE)
        out, err = p.communicate()
        return self.render_json_response({'response': out})

    def post(self, request):
        """
        Parse out the get parameters, validate it and run the command to add
        new iptables rules.
        """
        post_data = json.loads(request.raw_post_data)
        parameters = parse_parameters(post_data)
        iptables_command = ['sudo', 'iptables', ]
        iptables_command.extend(parameters)
        retcode = subprocess.call(iptables_command)
        response = HttpResponse()
        if retcode != 0:
            response.status_code = 400 # Bad Request
        else:
            response.status_code = 201 # Created
        return response
            
        
        

