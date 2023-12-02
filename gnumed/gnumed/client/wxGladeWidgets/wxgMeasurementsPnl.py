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


class wxgMeasurementsPnl(wx.Panel):
	def __init__(self, *args, **kwds):
		# begin wxGlade: wxgMeasurementsPnl.__init__
		kwds["style"] = kwds.get("style", 0) | wx.BORDER_NONE | wx.TAB_TRAVERSAL
		wx.Panel.__init__(self, *args, **kwds)
		from Gnumed.wxpython.gmMeasurementWidgets import cTestPanelPRW
		self._PRW_panel = cTestPanelPRW(self, wx.ID_ANY, "")
		self._TCTRL_panel_comment = wx.TextCtrl(self, wx.ID_ANY, "")
		self._BTN_manage_panels = wx.Button(self, wx.ID_ANY, _("Manage panels"), style=wx.BU_EXACTFIT)
		self._BTN_display_mode = wx.Button(self, wx.ID_ANY, _("All: by day"), style=wx.BU_EXACTFIT)
		self._PNL_results_battery_grid = wx.Panel(self, wx.ID_ANY, style=wx.BORDER_NONE)
		from Gnumed.wxpython.gmMeasurementWidgets import cMeasurementsGrid
		self._GRID_results_battery = cMeasurementsGrid(self._PNL_results_battery_grid, wx.ID_ANY, size=(1, 1))
		self._PNL_results_all_grid = wx.Panel(self, wx.ID_ANY, style=wx.BORDER_NONE)
		self._GRID_results_all = cMeasurementsGrid(self._PNL_results_all_grid, wx.ID_ANY, size=(1, 1))
		from Gnumed.wxpython.gmMeasurementWidgets import cMeasurementsByDayPnl
		self._PNL_results_all_listed = cMeasurementsByDayPnl(self, wx.ID_ANY, style=wx.BORDER_NONE | wx.TAB_TRAVERSAL)
		self._BTN_manage_types = wx.Button(self, wx.ID_ANY, _("Manage types"), style=wx.BU_EXACTFIT)
		self._BTN_add = wx.Button(self, wx.ID_ADD, "")
		self._BTN_list = wx.Button(self, wx.ID_ANY, _("&List"))
		self._BTN_select = wx.Button(self, wx.ID_ANY, _("&Select:"), style=wx.BU_EXACTFIT)
		self._RBTN_my_unsigned = wx.RadioButton(self, wx.ID_ANY, _("your unsigned (&Y)"))
		self._RBTN_all_unsigned = wx.RadioButton(self, wx.ID_ANY, _("all unsigned (&A)"))
		self._BTN_review = wx.Button(self, wx.ID_ANY, _("&Actions ... "), style=wx.BU_EXACTFIT)

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_BUTTON, self._on_manage_panels_button_pressed, self._BTN_manage_panels)
		self.Bind(wx.EVT_BUTTON, self._on_display_mode_button_pressed, self._BTN_display_mode)
		self.Bind(wx.EVT_BUTTON, self._on_manage_types_button_pressed, self._BTN_manage_types)
		self.Bind(wx.EVT_BUTTON, self._on_add_button_pressed, self._BTN_add)
		self.Bind(wx.EVT_BUTTON, self._on_list_button_pressed, self._BTN_list)
		self.Bind(wx.EVT_BUTTON, self._on_select_button_pressed, self._BTN_select)
		self.Bind(wx.EVT_BUTTON, self._on_review_button_pressed, self._BTN_review)
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: wxgMeasurementsPnl.__set_properties
		self._TCTRL_panel_comment.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
		self._TCTRL_panel_comment.Enable(False)
		self._BTN_manage_panels.SetToolTip(_("Manage test panels."))
		self._BTN_display_mode.SetToolTip(_("Switch between modes of the full results display."))
		self._PNL_results_all_listed.Hide()
		self._BTN_manage_types.SetToolTip(_("Manage test types."))
		self._BTN_add.SetToolTip(_("Add measurements."))
		self._BTN_list.SetToolTip(_("Show all measurements in a chronological list."))
		self._BTN_select.SetToolTip(_("Select results according to your choice on the right.\n\nThis will override any previous selection.\n\nNote that you can also select cells, rows, or columns manually within the table."))
		self._RBTN_my_unsigned.SetToolTip(_("Apply selection to those unsigned results for which you are to take responsibility."))
		self._RBTN_all_unsigned.SetToolTip(_("Apply selection to all unsigned results."))
		self._BTN_review.SetToolTip(_("Invoke actions on the selected measurements."))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: wxgMeasurementsPnl.__do_layout
		__szr_main = wx.BoxSizer(wx.VERTICAL)
		__szr_bottom = wx.BoxSizer(wx.HORIZONTAL)
		__szr_result_displays = wx.BoxSizer(wx.VERTICAL)
		__szr_results_all_grid = wx.BoxSizer(wx.HORIZONTAL)
		__szr_results_battery_grid = wx.BoxSizer(wx.HORIZONTAL)
		__szr_panel_options = wx.BoxSizer(wx.HORIZONTAL)
		__lbl_display = wx.StaticText(self, wx.ID_ANY, _("Spotlight &Panel:"))
		__szr_panel_options.Add(__lbl_display, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
		__szr_panel_options.Add(self._PRW_panel, 2, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10)
		__szr_panel_options.Add(self._TCTRL_panel_comment, 3, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
		__szr_panel_options.Add(self._BTN_manage_panels, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
		__szr_panel_options.Add(self._BTN_display_mode, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_main.Add(__szr_panel_options, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)
		__szr_results_battery_grid.Add(self._GRID_results_battery, 1, wx.EXPAND, 5)
		self._PNL_results_battery_grid.SetSizer(__szr_results_battery_grid)
		__szr_result_displays.Add(self._PNL_results_battery_grid, 1, wx.EXPAND, 0)
		__szr_results_all_grid.Add(self._GRID_results_all, 1, wx.EXPAND, 5)
		self._PNL_results_all_grid.SetSizer(__szr_results_all_grid)
		__szr_result_displays.Add(self._PNL_results_all_grid, 3, wx.EXPAND, 0)
		__szr_result_displays.Add(self._PNL_results_all_listed, 3, wx.EXPAND, 0)
		__szr_main.Add(__szr_result_displays, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)
		__hline_buttons = wx.StaticLine(self, wx.ID_ANY)
		__szr_main.Add(__hline_buttons, 0, wx.ALL | wx.EXPAND, 5)
		__szr_bottom.Add(self._BTN_manage_types, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_bottom.Add((20, 20), 2, wx.ALIGN_CENTER_VERTICAL, 0)
		__vline_buttons = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
		__szr_bottom.Add(__vline_buttons, 0, wx.EXPAND | wx.RIGHT, 3)
		__lbl_results = wx.StaticText(self, wx.ID_ANY, _("Results:"))
		__szr_bottom.Add(__lbl_results, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__szr_bottom.Add(self._BTN_add, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__szr_bottom.Add(self._BTN_list, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_bottom.Add((20, 20), 1, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_bottom.Add(self._BTN_select, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
		__szr_bottom.Add(self._RBTN_my_unsigned, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__szr_bottom.Add(self._RBTN_all_unsigned, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__szr_bottom.Add(self._BTN_review, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_bottom.Add((20, 20), 1, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_main.Add(__szr_bottom, 0, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
		self.SetSizer(__szr_main)
		__szr_main.Fit(self)
		self.Layout()
		# end wxGlade

	def _on_manage_panels_button_pressed(self, event):  # wxGlade: wxgMeasurementsPnl.<event_handler>
		print("Event handler '_on_manage_panels_button_pressed' not implemented!")
		event.Skip()

	def _on_display_mode_button_pressed(self, event):  # wxGlade: wxgMeasurementsPnl.<event_handler>
		print("Event handler '_on_display_mode_button_pressed' not implemented!")
		event.Skip()

	def _on_manage_types_button_pressed(self, event):  # wxGlade: wxgMeasurementsPnl.<event_handler>
		print("Event handler '_on_manage_types_button_pressed' not implemented!")
		event.Skip()

	def _on_add_button_pressed(self, event):  # wxGlade: wxgMeasurementsPnl.<event_handler>
		print("Event handler '_on_add_button_pressed' not implemented!")
		event.Skip()

	def _on_list_button_pressed(self, event):  # wxGlade: wxgMeasurementsPnl.<event_handler>
		print("Event handler '_on_list_button_pressed' not implemented!")
		event.Skip()

	def _on_select_button_pressed(self, event):  # wxGlade: wxgMeasurementsPnl.<event_handler>
		print("Event handler '_on_select_button_pressed' not implemented!")
		event.Skip()

	def _on_review_button_pressed(self, event):  # wxGlade: wxgMeasurementsPnl.<event_handler>
		print("Event handler '_on_review_button_pressed' not implemented!")
		event.Skip()

# end of class wxgMeasurementsPnl