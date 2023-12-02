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


class wxgInboxMessageEAPnl(wx.ScrolledWindow):
	def __init__(self, *args, **kwds):
		# begin wxGlade: wxgInboxMessageEAPnl.__init__
		kwds["style"] = kwds.get("style", 0) | wx.BORDER_NONE | wx.TAB_TRAVERSAL
		wx.ScrolledWindow.__init__(self, *args, **kwds)
		self._TCTRL_subject = wx.TextCtrl(self, wx.ID_ANY, "")
		from Gnumed.wxpython.gmProviderInboxWidgets import cMessageTypePhraseWheel
		self._PRW_type = cMessageTypePhraseWheel(self, wx.ID_ANY, "")
		self._CHBOX_send_to_me = wx.CheckBox(self, wx.ID_ANY, _(u"&Myself \u2026 or:"))
		from Gnumed.wxpython.gmStaffWidgets import cProviderPhraseWheel
		self._PRW_receiver = cProviderPhraseWheel(self, wx.ID_ANY, "")
		self._CHBOX_active_patient = wx.CheckBox(self, wx.ID_ANY, _(u"&Active \u2026 or:"))
		from Gnumed.wxpython.gmPatSearchWidgets import cPersonSearchCtrl
		self._PRW_patient = cPersonSearchCtrl(self, wx.ID_ANY, "")
		self._TCTRL_message = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE)
		from Gnumed.wxpython.gmDateTimeInput import cDateInputPhraseWheel
		self._PRW_due = cDateInputPhraseWheel(self, wx.ID_ANY, "")
		self._PRW_expiry = cDateInputPhraseWheel(self, wx.ID_ANY, "")
		self._RBTN_normal = wx.RadioButton(self, wx.ID_ANY, _("Normal"))
		self._RBTN_high = wx.RadioButton(self, wx.ID_ANY, _("High"))
		self._RBTN_low = wx.RadioButton(self, wx.ID_ANY, _("Low"))

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_CHECKBOX, self._on_send_to_me_checked, self._CHBOX_send_to_me)
		self.Bind(wx.EVT_CHECKBOX, self._on_active_patient_checked, self._CHBOX_active_patient)
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: wxgInboxMessageEAPnl.__set_properties
		self.SetScrollRate(10, 10)
		self._TCTRL_subject.SetToolTip(_("What this message is about."))
		self._PRW_type.SetToolTip(_("The message type."))
		self._CHBOX_send_to_me.SetToolTip(_("Check if this message should (also) be sent to yourself."))
		self._CHBOX_send_to_me.SetValue(1)
		self._PRW_receiver.SetToolTip(_("Whom to (also) send this message to."))
		self._CHBOX_active_patient.SetToolTip(_("Check this if this is about the active patient."))
		self._CHBOX_active_patient.SetValue(1)
		self._PRW_patient.Enable(False)
		self._TCTRL_message.SetToolTip(_("A longer text detailing the message, if needed."))
		self._PRW_due.SetToolTip(_("Optional: Pick a date when this message is due to be acted on."))
		self._PRW_expiry.SetToolTip(_("Optional: Pick a date when this message will no longer be relevant."))
		self._RBTN_normal.SetToolTip(_("Normal (standard) urgency of message."))
		self._RBTN_normal.SetValue(1)
		self._RBTN_high.SetToolTip(_("Higher than normal (standard) urgency of message."))
		self._RBTN_low.SetToolTip(_("Lower than normal (standard) urgency of message."))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: wxgInboxMessageEAPnl.__do_layout
		_gszr_main = wx.FlexGridSizer(8, 2, 1, 3)
		__szr_importance = wx.BoxSizer(wx.HORIZONTAL)
		__szr_patient = wx.BoxSizer(wx.HORIZONTAL)
		__szr_send_to = wx.BoxSizer(wx.HORIZONTAL)
		__lbl_subject = wx.StaticText(self, wx.ID_ANY, _("Subject"))
		__lbl_subject.SetForegroundColour(wx.Colour(255, 0, 0))
		_gszr_main.Add(__lbl_subject, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		_gszr_main.Add(self._TCTRL_subject, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__lbl_category = wx.StaticText(self, wx.ID_ANY, _("Category"))
		__lbl_category.SetForegroundColour(wx.Colour(255, 0, 0))
		_gszr_main.Add(__lbl_category, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		_gszr_main.Add(self._PRW_type, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__lbl_receiver = wx.StaticText(self, wx.ID_ANY, _("Audience"))
		__lbl_receiver.SetForegroundColour(wx.Colour(255, 127, 0))
		_gszr_main.Add(__lbl_receiver, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_send_to.Add(self._CHBOX_send_to_me, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.RIGHT, 5)
		__szr_send_to.Add(self._PRW_receiver, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		_gszr_main.Add(__szr_send_to, 1, wx.EXPAND, 0)
		__lbl_patient = wx.StaticText(self, wx.ID_ANY, _("Patient"))
		__lbl_patient.SetForegroundColour(wx.Colour(255, 127, 0))
		_gszr_main.Add(__lbl_patient, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_patient.Add(self._CHBOX_active_patient, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.RIGHT, 5)
		__szr_patient.Add(self._PRW_patient, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		_gszr_main.Add(__szr_patient, 1, wx.EXPAND, 0)
		__lbl_message = wx.StaticText(self, wx.ID_ANY, _("Message"))
		_gszr_main.Add(__lbl_message, 0, wx.TOP, 3)
		_gszr_main.Add(self._TCTRL_message, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__lbl_due = wx.StaticText(self, wx.ID_ANY, _("Due"))
		_gszr_main.Add(__lbl_due, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		_gszr_main.Add(self._PRW_due, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__lbl_expires = wx.StaticText(self, wx.ID_ANY, _("Expires"))
		_gszr_main.Add(__lbl_expires, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		_gszr_main.Add(self._PRW_expiry, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__lbl_urgency = wx.StaticText(self, wx.ID_ANY, _("Urgency"))
		_gszr_main.Add(__lbl_urgency, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_importance.Add(self._RBTN_normal, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.RIGHT, 5)
		__szr_importance.Add(self._RBTN_high, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.RIGHT, 5)
		__szr_importance.Add(self._RBTN_low, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__szr_importance.Add((20, 20), 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		_gszr_main.Add(__szr_importance, 1, wx.EXPAND, 0)
		self.SetSizer(_gszr_main)
		_gszr_main.Fit(self)
		_gszr_main.AddGrowableRow(4)
		_gszr_main.AddGrowableCol(1)
		self.Layout()
		# end wxGlade

	def _on_send_to_me_checked(self, event):  # wxGlade: wxgInboxMessageEAPnl.<event_handler>
		print("Event handler '_on_send_to_me_checked' not implemented!")
		event.Skip()

	def _on_active_patient_checked(self, event):  # wxGlade: wxgInboxMessageEAPnl.<event_handler>
		print("Event handler '_on_active_patient_checked' not implemented!")
		event.Skip()

# end of class wxgInboxMessageEAPnl