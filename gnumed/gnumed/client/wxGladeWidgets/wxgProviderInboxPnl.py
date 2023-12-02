# -*- coding: UTF-8 -*-
#
# generated by wxGlade
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
from Gnumed.wxpython.gmListWidgets import cReportListCtrl
# end wxGlade


class wxgProviderInboxPnl(wx.ScrolledWindow):
	def __init__(self, *args, **kwds):
		# begin wxGlade: wxgProviderInboxPnl.__init__
		kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
		wx.ScrolledWindow.__init__(self, *args, **kwds)
		self.SetScrollRate(10, 10)

		__szr_main = wx.BoxSizer(wx.VERTICAL)

		self._msg_welcome = wx.StaticText(self, wx.ID_ANY, _("Programmer must override this text."))
		self._msg_welcome.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, 0, ""))
		__szr_main.Add(self._msg_welcome, 0, 0, 0)

		__line_top = wx.StaticLine(self, wx.ID_ANY)
		__szr_main.Add(__line_top, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 5)

		__szr_items = wx.BoxSizer(wx.HORIZONTAL)
		__szr_main.Add(__szr_items, 0, wx.BOTTOM | wx.EXPAND, 5)

		__lbl_items = wx.StaticText(self, wx.ID_ANY, _("Messages:"))
		__szr_items.Add(__lbl_items, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 3)

		self._RBTN_relevant_messages = wx.RadioButton(self, wx.ID_ANY, _("&Relevant"), style=wx.RB_GROUP)
		self._RBTN_relevant_messages.SetToolTip(_("Show relevant messages only (excludes expired and not-yet-due messages)."))
		self._RBTN_relevant_messages.SetValue(1)
		__szr_items.Add(self._RBTN_relevant_messages, 0, wx.EXPAND | wx.RIGHT, 5)

		self._RBTN_all_messages = wx.RadioButton(self, wx.ID_ANY, _("A&ll"))
		self._RBTN_all_messages.SetToolTip(_("Show all (but expired) messages."))
		__szr_items.Add(self._RBTN_all_messages, 0, wx.EXPAND | wx.RIGHT, 5)

		self._RBTN_overdue_messages = wx.RadioButton(self, wx.ID_ANY, _("&Overdue"))
		self._RBTN_overdue_messages.SetToolTip(_("Show overdue messages only."))
		__szr_items.Add(self._RBTN_overdue_messages, 0, wx.EXPAND | wx.RIGHT, 5)

		self._RBTN_scheduled_messages = wx.RadioButton(self, wx.ID_ANY, _("&Scheduled"))
		self._RBTN_scheduled_messages.SetToolTip(_("Show scheduled (future-due) messages only."))
		__szr_items.Add(self._RBTN_scheduled_messages, 0, wx.EXPAND | wx.RIGHT, 5)

		self._RBTN_unscheduled_messages = wx.RadioButton(self, wx.ID_ANY, _("&Unscheduled"))
		self._RBTN_unscheduled_messages.SetToolTip(_("Show unscheduled (no due date) messages only."))
		__szr_items.Add(self._RBTN_unscheduled_messages, 0, wx.EXPAND | wx.RIGHT, 5)

		self._RBTN_expired_messages = wx.RadioButton(self, wx.ID_ANY, _("&Expired"))
		self._RBTN_expired_messages.SetToolTip(_("Show expired (expiry date has passed) messages only."))
		__szr_items.Add(self._RBTN_expired_messages, 0, wx.EXPAND, 5)

		__vline1_options = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
		__szr_items.Add(__vline1_options, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 3)

		__lbl_audience = wx.StaticText(self, wx.ID_ANY, _("Limit to:"))
		__szr_items.Add(__lbl_audience, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)

		self._CHBOX_active_patient = wx.CheckBox(self, wx.ID_ANY, _("Active patient"))
		self._CHBOX_active_patient.SetToolTip(_("Include only messages about the active patient."))
		self._CHBOX_active_patient.Enable(False)
		__szr_items.Add(self._CHBOX_active_patient, 0, wx.EXPAND | wx.RIGHT, 5)

		self._CHBOX_active_provider = wx.CheckBox(self, wx.ID_ANY, _("Yours"))
		self._CHBOX_active_provider.SetToolTip(_("Include only messages explicitly for you (rather than also to all providers)."))
		self._CHBOX_active_provider.SetValue(1)
		__szr_items.Add(self._CHBOX_active_provider, 0, wx.EXPAND, 3)

		__vline2_options = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
		__szr_items.Add(__vline2_options, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 3)

		__szr_items.Add((20, 20), 1, wx.EXPAND, 0)

		self._BTN_add = wx.Button(self, wx.ID_ANY, _("&Add"), style=wx.BU_EXACTFIT)
		self._BTN_add.SetToolTip(_("Add a new message."))
		__szr_items.Add(self._BTN_add, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)

		self._LCTRL_provider_inbox = cReportListCtrl(self, wx.ID_ANY, style=wx.BORDER_SIMPLE | wx.LC_REPORT | wx.LC_SINGLE_SEL)
		self._LCTRL_provider_inbox.SetFocus()
		__szr_main.Add(self._LCTRL_provider_inbox, 3, wx.EXPAND, 0)

		self._TXT_inbox_item_comment = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.HSCROLL | wx.TE_BESTWRAP | wx.TE_MULTILINE | wx.TE_READONLY)
		__szr_main.Add(self._TXT_inbox_item_comment, 2, wx.EXPAND, 0)

		self.SetSizer(__szr_main)
		__szr_main.Fit(self)

		self.Layout()

		self.Bind(wx.EVT_RADIOBUTTON, self._on_message_range_radiobutton_selected, self._RBTN_relevant_messages)
		self.Bind(wx.EVT_RADIOBUTTON, self._on_message_range_radiobutton_selected, self._RBTN_all_messages)
		self.Bind(wx.EVT_RADIOBUTTON, self._on_message_range_radiobutton_selected, self._RBTN_overdue_messages)
		self.Bind(wx.EVT_RADIOBUTTON, self._on_message_range_radiobutton_selected, self._RBTN_scheduled_messages)
		self.Bind(wx.EVT_RADIOBUTTON, self._on_message_range_radiobutton_selected, self._RBTN_unscheduled_messages)
		self.Bind(wx.EVT_RADIOBUTTON, self._on_message_range_radiobutton_selected, self._RBTN_expired_messages)
		self.Bind(wx.EVT_CHECKBOX, self._on_active_patient_checkbox_ticked, self._CHBOX_active_patient)
		self.Bind(wx.EVT_CHECKBOX, self._on_active_provider_checkbox_ticked, self._CHBOX_active_provider)
		self.Bind(wx.EVT_BUTTON, self._on_add_button_pressed, self._BTN_add)
		# end wxGlade

	def _on_message_range_radiobutton_selected(self, event):  # wxGlade: wxgProviderInboxPnl.<event_handler>
		print("Event handler '_on_message_range_radiobutton_selected' not implemented!")
		event.Skip()

	def _on_active_patient_checkbox_ticked(self, event):  # wxGlade: wxgProviderInboxPnl.<event_handler>
		print("Event handler '_on_active_patient_checkbox_ticked' not implemented!")
		event.Skip()

	def _on_active_provider_checkbox_ticked(self, event):  # wxGlade: wxgProviderInboxPnl.<event_handler>
		print("Event handler '_on_active_provider_checkbox_ticked' not implemented!")
		event.Skip()

	def _on_add_button_pressed(self, event):  # wxGlade: wxgProviderInboxPnl.<event_handler>
		print("Event handler '_on_add_button_pressed' not implemented!")
		event.Skip()

# end of class wxgProviderInboxPnl