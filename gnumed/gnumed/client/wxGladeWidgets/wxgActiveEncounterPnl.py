# -*- coding: UTF-8 -*-
#
# generated by wxGlade
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class wxgActiveEncounterPnl(wx.Panel):
	def __init__(self, *args, **kwds):
		# begin wxGlade: wxgActiveEncounterPnl.__init__
		wx.Panel.__init__(self, *args, **kwds)
		self._BTN_list = wx.Button(self, wx.ID_ANY, _("&L"), style=wx.BU_EXACTFIT)
		self._TCTRL_encounter = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
		self._BTN_new = wx.Button(self, wx.ID_ANY, _("&N"), style=wx.BU_EXACTFIT)

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_BUTTON, self._on_list_button_pressed, self._BTN_list)
		self.Bind(wx.EVT_BUTTON, self._on_new_button_pressed, self._BTN_new)
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: wxgActiveEncounterPnl.__set_properties
		self._BTN_list.SetToolTip(_("List all encounters."))
		self._TCTRL_encounter.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
		self._TCTRL_encounter.SetToolTip(_("The encounter."))
		self._BTN_new.SetToolTip(_("Start a new encounter for the active patient."))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: wxgActiveEncounterPnl.__do_layout
		__szr_main = wx.BoxSizer(wx.HORIZONTAL)
		__szr_main.Add(self._BTN_list, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 2)
		__szr_main.Add(self._TCTRL_encounter, 1, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 2)
		__szr_main.Add(self._BTN_new, 0, wx.ALIGN_CENTER_VERTICAL, 1)
		self.SetSizer(__szr_main)
		__szr_main.Fit(self)
		self.Layout()
		# end wxGlade

	def _on_list_button_pressed(self, event):  # wxGlade: wxgActiveEncounterPnl.<event_handler>
		print("Event handler '_on_list_button_pressed' not implemented!")
		event.Skip()

	def _on_new_button_pressed(self, event):  # wxGlade: wxgActiveEncounterPnl.<event_handler>
		print("Event handler '_on_new_button_pressed' not implemented!")
		event.Skip()

# end of class wxgActiveEncounterPnl