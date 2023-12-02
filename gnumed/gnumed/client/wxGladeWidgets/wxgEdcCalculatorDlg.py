# -*- coding: UTF-8 -*-
#
# generated by wxGlade
#

import wx
import wx.adv

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
from Gnumed.wxpython.gmDateTimeInput import cDateInputPhraseWheel
# end wxGlade


class wxgEdcCalculatorDlg(wx.Dialog):
	def __init__(self, *args, **kwds):
		# begin wxGlade: wxgEdcCalculatorDlg.__init__
		kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.RESIZE_BORDER
		wx.Dialog.__init__(self, *args, **kwds)
		self.SetSize(wx.DLG_UNIT(self, wx.Size(400, 200)))
		self._PRW_lmp = cDateInputPhraseWheel(self, wx.ID_ANY, "")
		self._CHBOX_first_pregnancy = wx.CheckBox(self, wx.ID_ANY, _("&First pregnancy"))
		self._PRW_edc = cDateInputPhraseWheel(self, wx.ID_ANY, "")
		self._TCTRL_details = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_WORDWRAP)
		self._CALCTRL = wx.adv.CalendarCtrl(self, wx.ID_ANY, style=wx.adv.CAL_SHOW_SURROUNDING_WEEKS)
		self._TCTRL_algo = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_WORDWRAP)
		self._BTN_save = wx.Button(self, wx.ID_SAVE, "", style=wx.BU_EXACTFIT)
		self._BTN_cancel = wx.Button(self, wx.ID_CANCEL, "", style=wx.BU_EXACTFIT)

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_CHECKBOX, self._on_first_pregnancy_toggled, self._CHBOX_first_pregnancy)
		self.Bind(wx.adv.EVT_CALENDAR, self._on_lmp_picked_in_calendar, self._CALCTRL)
		self.Bind(wx.EVT_BUTTON, self._on_save_button_pressed, self._BTN_save)
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: wxgEdcCalculatorDlg.__set_properties
		self.SetTitle(_("Due Date Calculator"))
		self.SetSize(wx.DLG_UNIT(self, wx.Size(400, 200)))
		self._PRW_lmp.SetToolTip(_("Required: Enter the 1st day of the Last Menstrual Period."))
		self._CHBOX_first_pregnancy.SetToolTip(_("Check here if this is the first pregnancy."))
		self._CHBOX_first_pregnancy.SetValue(1)
		self._PRW_edc.SetToolTip(_("Expected Date of Confinement.\n\nYou can also just enter a date here if one is known from external sources."))
		self._TCTRL_details.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
		self._TCTRL_algo.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
		self._BTN_save.SetToolTip(_("Save the Expected Due Date."))
		self._BTN_cancel.SetToolTip(_("Close without saving."))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: wxgEdcCalculatorDlg.__do_layout
		__szr_main = wx.BoxSizer(wx.VERTICAL)
		__szr_buttons = wx.BoxSizer(wx.HORIZONTAL)
		__szr_middle = wx.BoxSizer(wx.HORIZONTAL)
		__szr_right = wx.BoxSizer(wx.VERTICAL)
		__szr_left = wx.BoxSizer(wx.VERTICAL)
		__fgszr_input_fields = wx.FlexGridSizer(3, 2, 1, 3)
		__lbl_lmp = wx.StaticText(self, wx.ID_ANY, _("LMP (1st)"))
		__lbl_lmp.SetForegroundColour(wx.Colour(255, 0, 0))
		__fgszr_input_fields.Add(__lbl_lmp, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__fgszr_input_fields.Add(self._PRW_lmp, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__fgszr_input_fields.Add((20, 20), 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__fgszr_input_fields.Add(self._CHBOX_first_pregnancy, 1, wx.ALIGN_CENTER_VERTICAL, 0)
		__lbl_due_date = wx.StaticText(self, wx.ID_ANY, _("EDC"))
		__fgszr_input_fields.Add(__lbl_due_date, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__fgszr_input_fields.Add(self._PRW_edc, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__fgszr_input_fields.AddGrowableCol(1)
		__szr_left.Add(__fgszr_input_fields, 0, wx.EXPAND, 1)
		__szr_left.Add(self._TCTRL_details, 1, wx.EXPAND | wx.TOP, 4)
		__szr_middle.Add(__szr_left, 1, wx.EXPAND, 1)
		__lbl_select_lmp = wx.StaticText(self, wx.ID_ANY, _("or pick 1st day of LMP:"))
		__szr_right.Add(__lbl_select_lmp, 0, wx.ALIGN_CENTER | wx.BOTTOM, 5)
		__szr_right.Add(self._CALCTRL, 0, 0, 10)
		__szr_right.Add(self._TCTRL_algo, 1, wx.EXPAND | wx.TOP, 5)
		__szr_middle.Add(__szr_right, 0, wx.EXPAND | wx.LEFT, 10)
		__szr_main.Add(__szr_middle, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 3)
		__szr_buttons.Add((20, 20), 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__szr_buttons.Add(self._BTN_save, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
		__szr_buttons.Add(self._BTN_cancel, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 5)
		__szr_buttons.Add((20, 20), 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__szr_main.Add(__szr_buttons, 0, wx.ALL | wx.EXPAND, 3)
		self.SetSizer(__szr_main)
		self.Layout()
		# end wxGlade

	def _on_first_pregnancy_toggled(self, event):  # wxGlade: wxgEdcCalculatorDlg.<event_handler>
		print("Event handler '_on_first_pregnancy_toggled' not implemented!")
		event.Skip()

	def _on_lmp_picked_in_calendar(self, event):  # wxGlade: wxgEdcCalculatorDlg.<event_handler>
		print("Event handler '_on_lmp_picked_in_calendar' not implemented!")
		event.Skip()

	def _on_save_button_pressed(self, event):  # wxGlade: wxgEdcCalculatorDlg.<event_handler>
		print("Event handler '_on_save_button_pressed' not implemented!")
		event.Skip()

# end of class wxgEdcCalculatorDlg