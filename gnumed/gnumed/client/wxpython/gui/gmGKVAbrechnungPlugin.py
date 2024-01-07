"""
GKV Abrechnung - vorerst Platzhalter
(c) 2024 
"""

__author__ = "Berthold Gehrke <kontakt@simpelmed.de>"
__license__ = 'AGPL v3 or later (details at http://www.gnu.org)'

import logging

import wx

from Gnumed.wxpython import gmPlugin
# gmGKVAbrechnungWidgets »startet« als Kopie von gmBillingWidgets
from Gnumed.wxpython import gmGKVAbrechnungWidgets
from Gnumed.wxpython import gmAccessPermissionWidgets

_log = logging.getLogger('gm.billing')

#======================================================================
class gmGKVAbrechnungPlugin(gmPlugin.cNotebookPlugin):

    tab_name = 'GKV-ABRECHNUNG'
    required_minimum_role = 'full clinical access'

    @gmAccessPermissionWidgets.verify_minimum_required_role (
        required_minimum_role,
        activity = _('loading plugin <%s>') % tab_name,
        return_value_on_failure = False,
        fail_silently = False
    )
    def register(self):
        gmPlugin.cNotebookPlugin.register(self)

    def name(self):
        return 'GKV-ABRECHNUNG'

    def GetWidget(self, parent):
        #self._widget = gmBillingWidgets.cBillingPluginPnl(parent, -1)
        self._widget = gmGKVAbrechnungWidgets.cBillingPluginPnl(parent, -1)
        return self._widget

    def MenuInfo(self):
            return ('emr', 'GKV-ABRECHNUNG')
            #pass

    def can_receive_focus(self):
        if not self._verify_patient_avail():
            return None
        return 1

#======================================================================
if __name__ == '__main__':
    pass
