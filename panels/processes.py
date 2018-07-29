from __future__ import absolute_import, unicode_literals

import sys
import psutil
import django
from django.apps import apps
from django.utils.translation import ugettext_lazy as _

from debug_toolbar.panels import Panel


class ProcessPanel(Panel):
    """
    Shows versions of Python, Django, and installed apps if possible.
    """
    pass
    @property
    def nav_subtitle(self):
        return 'Django %s' % django.get_version()

    title = _("Process")

    template = 'debug_toolbar/panels/process.html'

    def generate_stats(self, request, response):

        processId = psutil.pids()
        data=[]
        for id in processId:
            temp=dict()
            temp['id']=id
            p =psutil.Process(id)
            temp['name']=p.name()
            temp['memory'] = p.memory_info()[0]
            data.append(temp)
        #data.sort(key= lambda x: x['memory'], reverse=True)
        self.record_stats({
            'paths': sys.path,
            'data':data,
        })
