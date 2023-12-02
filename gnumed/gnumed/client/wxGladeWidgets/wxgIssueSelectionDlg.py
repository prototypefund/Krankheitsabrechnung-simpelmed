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


class wxgIssueSelectionDlg(wx.Dialog):
	def __init__(self, *args, **kwds):
		# begin wxGlade: wxgIssueSelectionDlg.__init__
		kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.RESIZE_BORDER
		wx.Dialog.__init__(self, *args, **kwds)
		self.SetSize((300, 150))
		self._lbl_message = wx.StaticText(self, wx.ID_ANY, _("Please select a health issue:"))
		from Gnumed.wxpython.gmEMRStructWidgets import cIssueSelectionPhraseWheel
		self._PhWheel_issue = cIssueSelectionPhraseWheel(self, wx.ID_ANY)
		self._BTN_OK = wx.Button(self, wx.ID_OK, _("OK"))
		self._BTN_dismiss = wx.Button(self, wx.ID_CANCEL, _("Close"))

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_BUTTON, self._on_OK_button_pressed, id=wx.ID_OK)
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: wxgIssueSelectionDlg.__set_properties
		self.SetTitle(_("Health issue selector"))
		self.SetSize((300, 150))
		self._PhWheel_issue.SetFocus()
		self._BTN_OK.SetDefault()
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: wxgIssueSelectionDlg.__do_layout
		_szr_main = wx.BoxSizer(wx.VERTICAL)
		_szr_buttons = wx.BoxSizer(wx.HORIZONTAL)
		_szr_main.Add(self._lbl_message, 1, wx.ALL | wx.EXPAND, 3)
		_szr_main.Add(self._PhWheel_issue, 0, wx.EXPAND, 0)
		_szr_buttons.Add(self._BTN_OK, 0, 0, 0)
		_szr_buttons.Add((20, 20), 1, wx.EXPAND, 0)
		_szr_buttons.Add(self._BTN_dismiss, 0, 0, 0)
		_szr_main.Add(_szr_buttons, 0, wx.EXPAND, 0)
		self.SetSizer(_szr_main)
		self.Layout()
		self.Centre()
		# end wxGlade

	def _on_OK_button_pressed(self, event):  # wxGlade: wxgIssueSelectionDlg.<event_handler>
		print("Event handler '_on_OK_button_pressed' not implemented!")
		event.Skip()

# end of class wxgIssueSelectionDlg