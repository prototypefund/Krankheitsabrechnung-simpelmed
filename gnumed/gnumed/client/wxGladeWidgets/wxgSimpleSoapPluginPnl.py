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


class wxgSimpleSoapPluginPnl(wx.ScrolledWindow):
	def __init__(self, *args, **kwds):
		# begin wxGlade: wxgSimpleSoapPluginPnl.__init__
		kwds["style"] = kwds.get("style", 0) | wx.BORDER_NONE | wx.TAB_TRAVERSAL
		wx.ScrolledWindow.__init__(self, *args, **kwds)
		self.SetSize(wx.DLG_UNIT(self, wx.Size(400, 216)))
		self._splitter_main = wx.SplitterWindow(self, wx.ID_ANY, style=wx.SP_3D | wx.SP_BORDER)
		self.__pnl_left = wx.Panel(self._splitter_main, wx.ID_ANY, style=wx.BORDER_NONE | wx.TAB_TRAVERSAL)
		from Gnumed.wxpython.gmListWidgets import cReportListCtrl
		self._LCTRL_problems = cReportListCtrl(self.__pnl_left, wx.ID_ANY, style=wx.BORDER_NONE | wx.LC_NO_HEADER | wx.LC_REPORT | wx.LC_SINGLE_SEL)
		self._BTN_add_problem = wx.Button(self.__pnl_left, wx.ID_ANY, _("&Add"), style=wx.BU_EXACTFIT)
		self._BTN_edit_problem = wx.Button(self.__pnl_left, wx.ID_ANY, _("&Edit"), style=wx.BU_EXACTFIT)
		self._BTN_delete_problem = wx.Button(self.__pnl_left, wx.ID_ANY, _("&Delete"), style=wx.BU_EXACTFIT)
		from Gnumed.wxpython.gmTextCtrl import cTextCtrl
		self._TCTRL_soap_problem = wx.TextCtrl(self.__pnl_left, wx.ID_ANY, _("<above, double-click problem to start entering SOAP note>"), style=wx.TE_READONLY)
		self._TCTRL_soap = cTextCtrl(self.__pnl_left, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_WORDWRAP)
		self._BTN_save_soap = wx.Button(self.__pnl_left, wx.ID_ANY, _("&Save"), style=wx.BU_EXACTFIT)
		self._BTN_clear_soap = wx.Button(self.__pnl_left, wx.ID_ANY, _("&Clear"), style=wx.BU_EXACTFIT)
		self.__pnl_right = wx.Panel(self._splitter_main, wx.ID_ANY, style=wx.BORDER_NONE | wx.TAB_TRAVERSAL)
		self._CHBOX_filter_by_problem = wx.CheckBox(self.__pnl_right, wx.ID_ANY, _("&Filter by problem"))
		self._TCTRL_journal = wx.TextCtrl(self.__pnl_right, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_LIST_ITEM_SELECTED, self._on_list_item_selected, self._LCTRL_problems)
		self.Bind(wx.EVT_BUTTON, self._on_add_problem_button_pressed, self._BTN_add_problem)
		self.Bind(wx.EVT_BUTTON, self._on_edit_problem_button_pressed, self._BTN_edit_problem)
		self.Bind(wx.EVT_BUTTON, self._on_delete_problem_button_pressed, self._BTN_delete_problem)
		self.Bind(wx.EVT_BUTTON, self._on_save_soap_button_pressed, self._BTN_save_soap)
		self.Bind(wx.EVT_BUTTON, self._on_clear_soap_button_pressed, self._BTN_clear_soap)
		self.Bind(wx.EVT_CHECKBOX, self._on_filter_by_problem_checked, self._CHBOX_filter_by_problem)
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: wxgSimpleSoapPluginPnl.__set_properties
		self.SetSize(wx.DLG_UNIT(self, wx.Size(400, 216)))
		self.SetScrollRate(10, 10)
		self._BTN_add_problem.SetToolTip(_("Add a problem to the problem list."))
		self._BTN_edit_problem.SetToolTip(_("Edit the selected problem."))
		self._BTN_delete_problem.SetToolTip(_("Delete the selected problem (only possible as long as there are no SOAP notes for it)."))
		self._TCTRL_soap_problem.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
		self._TCTRL_soap_problem.SetFont(wx.Font(8, wx.DEFAULT, wx.ITALIC, wx.NORMAL, 0, ""))
		self._TCTRL_soap.SetToolTip(_("Enter your SOAP note here."))
		self._BTN_save_soap.SetToolTip(_("Save the current SOAP note."))
		self._BTN_clear_soap.SetToolTip(_("Clear the SOAP note."))
		self._CHBOX_filter_by_problem.SetToolTip(_("Check this if you want to filter the journal by the problem selected on the left."))
		self._CHBOX_filter_by_problem.SetValue(1)
		self._TCTRL_journal.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
		self._splitter_main.SetMinimumPaneSize(20)
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: wxgSimpleSoapPluginPnl.__do_layout
		__szr_main = wx.BoxSizer(wx.HORIZONTAL)
		__szr_right = wx.BoxSizer(wx.VERTICAL)
		__szr_right_top = wx.BoxSizer(wx.HORIZONTAL)
		__szr_left = wx.BoxSizer(wx.VERTICAL)
		__szr_left_bottom_buttons = wx.BoxSizer(wx.HORIZONTAL)
		__szr_left_middle_buttons = wx.BoxSizer(wx.HORIZONTAL)
		__szr_left.Add(self._LCTRL_problems, 2, wx.BOTTOM | wx.EXPAND | wx.RIGHT, 2)
		__szr_left_middle_buttons.Add((20, 20), 1, wx.EXPAND, 0)
		__szr_left_middle_buttons.Add(self._BTN_add_problem, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__szr_left_middle_buttons.Add(self._BTN_edit_problem, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__szr_left_middle_buttons.Add(self._BTN_delete_problem, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_left_middle_buttons.Add((20, 20), 1, wx.EXPAND, 0)
		__szr_left.Add(__szr_left_middle_buttons, 0, wx.BOTTOM | wx.EXPAND | wx.RIGHT, 2)
		__szr_left.Add(self._TCTRL_soap_problem, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.EXPAND | wx.RIGHT, 2)
		__szr_left.Add(self._TCTRL_soap, 3, wx.BOTTOM | wx.EXPAND | wx.RIGHT, 2)
		__szr_left_bottom_buttons.Add((20, 20), 1, wx.EXPAND, 0)
		__szr_left_bottom_buttons.Add(self._BTN_save_soap, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__szr_left_bottom_buttons.Add(self._BTN_clear_soap, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_left_bottom_buttons.Add((20, 20), 1, wx.EXPAND, 0)
		__szr_left.Add(__szr_left_bottom_buttons, 0, wx.EXPAND | wx.RIGHT, 2)
		self.__pnl_left.SetSizer(__szr_left)
		__szr_right_top.Add(self._CHBOX_filter_by_problem, 1, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_right.Add(__szr_right_top, 0, wx.BOTTOM | wx.EXPAND | wx.LEFT, 2)
		__szr_right.Add(self._TCTRL_journal, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT, 2)
		self.__pnl_right.SetSizer(__szr_right)
		self._splitter_main.SplitVertically(self.__pnl_left, self.__pnl_right)
		__szr_main.Add(self._splitter_main, 1, wx.ALL | wx.EXPAND, 2)
		self.SetSizer(__szr_main)
		self.Layout()
		# end wxGlade

	def _on_list_item_selected(self, event):  # wxGlade: wxgSimpleSoapPluginPnl.<event_handler>
		print("Event handler '_on_list_item_selected' not implemented!")
		event.Skip()

	def _on_add_problem_button_pressed(self, event):  # wxGlade: wxgSimpleSoapPluginPnl.<event_handler>
		print("Event handler '_on_add_problem_button_pressed' not implemented!")
		event.Skip()

	def _on_edit_problem_button_pressed(self, event):  # wxGlade: wxgSimpleSoapPluginPnl.<event_handler>
		print("Event handler '_on_edit_problem_button_pressed' not implemented!")
		event.Skip()

	def _on_delete_problem_button_pressed(self, event):  # wxGlade: wxgSimpleSoapPluginPnl.<event_handler>
		print("Event handler '_on_delete_problem_button_pressed' not implemented!")
		event.Skip()

	def _on_save_soap_button_pressed(self, event):  # wxGlade: wxgSimpleSoapPluginPnl.<event_handler>
		print("Event handler '_on_save_soap_button_pressed' not implemented!")
		event.Skip()

	def _on_clear_soap_button_pressed(self, event):  # wxGlade: wxgSimpleSoapPluginPnl.<event_handler>
		print("Event handler '_on_clear_soap_button_pressed' not implemented!")
		event.Skip()

	def _on_filter_by_problem_checked(self, event):  # wxGlade: wxgSimpleSoapPluginPnl.<event_handler>
		print("Event handler '_on_filter_by_problem_checked' not implemented!")
		event.Skip()

# end of class wxgSimpleSoapPluginPnl