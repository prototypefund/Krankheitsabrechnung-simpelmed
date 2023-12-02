# -*- coding: UTF-8 -*-
#
# generated by wxGlade
#

import wx
import wx.grid

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class wxgMeasurementsByBatteryPnl(wx.Panel):
	def __init__(self, *args, **kwds):
		# begin wxGlade: wxgMeasurementsByBatteryPnl.__init__
		kwds["style"] = kwds.get("style", 0) | wx.BORDER_NONE | wx.TAB_TRAVERSAL
		wx.Panel.__init__(self, *args, **kwds)
		from Gnumed.wxpython.gmMeasurementWidgets import cTestPanelPRW
		self._PRW_panel = cTestPanelPRW(self, wx.ID_ANY, "")
		self._TCTRL_panel_comment = wx.TextCtrl(self, wx.ID_ANY, "")
		self._BTN_manage_panels = wx.Button(self, wx.ID_ANY, _("Manage"), style=wx.BU_EXACTFIT)
		from Gnumed.wxpython.gmMeasurementWidgets import cMeasurementsGrid
		self._GRID_results_battery = cMeasurementsGrid(self, wx.ID_ANY, size=(1, 1))

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_BUTTON, self._on_manage_panels_button_pressed, self._BTN_manage_panels)
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: wxgMeasurementsByBatteryPnl.__set_properties
		self._TCTRL_panel_comment.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
		self._TCTRL_panel_comment.Enable(False)
		self._BTN_manage_panels.SetToolTip(_("Manage test panels."))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: wxgMeasurementsByBatteryPnl.__do_layout
		__szr_main = wx.BoxSizer(wx.VERTICAL)
		__szr_panel_options = wx.BoxSizer(wx.HORIZONTAL)
		__lbl_display = wx.StaticText(self, wx.ID_ANY, _("&Panel:"))
		__szr_panel_options.Add(__lbl_display, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
		__szr_panel_options.Add(self._PRW_panel, 2, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10)
		__szr_panel_options.Add(self._TCTRL_panel_comment, 3, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
		__szr_panel_options.Add(self._BTN_manage_panels, 0, wx.ALIGN_CENTER_VERTICAL, 5)
		__szr_main.Add(__szr_panel_options, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)
		__szr_main.Add(self._GRID_results_battery, 1, wx.EXPAND, 5)
		self.SetSizer(__szr_main)
		__szr_main.Fit(self)
		self.Layout()
		# end wxGlade

	def _on_manage_panels_button_pressed(self, event):  # wxGlade: wxgMeasurementsByBatteryPnl.<event_handler>
		print("Event handler '_on_manage_panels_button_pressed' not implemented!")
		event.Skip()

# end of class wxgMeasurementsByBatteryPnl