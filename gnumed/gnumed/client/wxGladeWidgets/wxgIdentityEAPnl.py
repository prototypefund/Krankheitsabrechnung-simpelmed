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


class wxgIdentityEAPnl(wx.ScrolledWindow):
	def __init__(self, *args, **kwds):
		# begin wxGlade: wxgIdentityEAPnl.__init__
		kwds["style"] = kwds.get("style", 0) | wx.BORDER_NONE | wx.TAB_TRAVERSAL
		wx.ScrolledWindow.__init__(self, *args, **kwds)
		self._LBL_info = wx.StaticText(self, wx.ID_ANY, "")
		from Gnumed.wxpython.gmDateTimeInput import cDateInputPhraseWheel
		self._PRW_dob = cDateInputPhraseWheel(self, wx.ID_ANY, "")
		self._CHBOX_estimated_dob = wx.CheckBox(self, wx.ID_ANY, _(u"\u2248"))
		self._TCTRL_tob = wx.TextCtrl(self, wx.ID_ANY, "")
		from Gnumed.wxpython.gmDateTimeInput import cDateInputPhraseWheel
		self._PRW_dod = cDateInputPhraseWheel(self, wx.ID_ANY, "")
		from Gnumed.wxpython.gmDemographicsWidgets import cGenderSelectionPhraseWheel
		self._PRW_gender = cGenderSelectionPhraseWheel(self, wx.ID_ANY, "")
		self._PRW_ethnicity = wx.TextCtrl(self, wx.ID_ANY, "")
		from Gnumed.wxpython.gmDemographicsWidgets import cTitlePhraseWheel
		self._PRW_title = cTitlePhraseWheel(self, wx.ID_ANY, "")
		self._TCTRL_comment = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE)

		self.__set_properties()
		self.__do_layout()
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: wxgIdentityEAPnl.__set_properties
		self.SetScrollRate(10, 10)
		self._PRW_dob.SetToolTip(_("The date of birth for this person."))
		self._CHBOX_estimated_dob.SetToolTip(_("Check this if the date of birth is estimated rather than known precisely."))
		self._TCTRL_tob.SetToolTip(_("The time of birth if known."))
		self._PRW_dod.SetToolTip(_("The date of death."))
		self._PRW_ethnicity.Enable(False)
		self._TCTRL_comment.SetToolTip(_("A free-text comment on this person."))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: wxgIdentityEAPnl.__do_layout
		__gzszr_main = wx.FlexGridSizer(7, 2, 1, 3)
		__szr_dob = wx.BoxSizer(wx.HORIZONTAL)
		__lbl_name = wx.StaticText(self, wx.ID_ANY, _("Status"))
		__gzszr_main.Add(__lbl_name, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__gzszr_main.Add(self._LBL_info, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__lbl_dob = wx.StaticText(self, wx.ID_ANY, _("Born"))
		__gzszr_main.Add(__lbl_dob, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_dob.Add(self._PRW_dob, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND | wx.RIGHT, 5)
		__szr_dob.Add(self._CHBOX_estimated_dob, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
		__vline_dob = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
		__szr_dob.Add(__vline_dob, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 2)
		__lbl_tob = wx.StaticText(self, wx.ID_ANY, _("Time:"))
		__szr_dob.Add(__lbl_tob, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)
		__szr_dob.Add(self._TCTRL_tob, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__gzszr_main.Add(__szr_dob, 1, wx.EXPAND, 0)
		__lbl_dod = wx.StaticText(self, wx.ID_ANY, _("Deceased"))
		__gzszr_main.Add(__lbl_dod, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__gzszr_main.Add(self._PRW_dod, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__lbl_gender = wx.StaticText(self, wx.ID_ANY, _("Gender"))
		__gzszr_main.Add(__lbl_gender, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__gzszr_main.Add(self._PRW_gender, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__lbl_ethnicity = wx.StaticText(self, wx.ID_ANY, _("Ethnicity"))
		__gzszr_main.Add(__lbl_ethnicity, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__gzszr_main.Add(self._PRW_ethnicity, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__lbl_title = wx.StaticText(self, wx.ID_ANY, _("Title"))
		__gzszr_main.Add(__lbl_title, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__gzszr_main.Add(self._PRW_title, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__lbl_comment = wx.StaticText(self, wx.ID_ANY, _("Comment"))
		__gzszr_main.Add(__lbl_comment, 0, 0, 0)
		__gzszr_main.Add(self._TCTRL_comment, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		self.SetSizer(__gzszr_main)
		__gzszr_main.Fit(self)
		__gzszr_main.AddGrowableRow(6)
		__gzszr_main.AddGrowableCol(1)
		self.Layout()
		# end wxGlade

# end of class wxgIdentityEAPnl