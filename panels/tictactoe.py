from __future__ import absolute_import, unicode_literals

import sys
import psutil
import django
from django.apps import apps
from django.utils.translation import ugettext_lazy as _

from debug_toolbar.panels import Panel


class TicTacToeGame(Panel):
    """
    Shows versions of Python, Django, and installed apps if possible.
    """
    @property
    def nav_subtitle(self):
        return 'Django %s' % django.get_version()

    title = _("TIC-TAC-TOE")

    template = 'debug_toolbar/panels/tictactoe.html'
