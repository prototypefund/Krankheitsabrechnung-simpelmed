# -*- coding: UTF-8 -*-
#
# generated by wxGlade
#

import wx

import gettext

from Gnumed.wxpython.gmPatPicWidgets import cPatientPicture
from Gnumed.wxpython.gmPatSearchWidgets import cActivePatientSelector
from Gnumed.wxpython.gmDemographicsWidgets import cImageTagPresenterPnl
from Gnumed.wxpython.gmEncounterWidgets import cActiveEncounterPnl


class wxgTopPnl(wx.Panel):
	def __init__(self, *args, **kwds):
		kwds["style"] = kwds.get("style", 0) | wx.BORDER_RAISED
		wx.Panel.__init__(self, *args, **kwds)

		__szr_main = wx.BoxSizer(wx.HORIZONTAL)

		self._BMP_patient_picture = cPatientPicture(self, wx.ID_ANY, wx.Bitmap(50, 54))
		self._BMP_patient_picture.SetMinSize((50, 54))
		__szr_main.Add(self._BMP_patient_picture, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 2)

		__szr_stacked_rows = wx.BoxSizer(wx.VERTICAL)
		__szr_main.Add(__szr_stacked_rows, 1, 0, 0)

		__szr_top_row = wx.BoxSizer(wx.HORIZONTAL)
		__szr_stacked_rows.Add(__szr_top_row, 0, wx.BOTTOM | wx.EXPAND, 2)

		self._TCTRL_patient_selector = cActivePatientSelector(self, wx.ID_ANY, "")
		self._TCTRL_patient_selector.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
		__szr_top_row.Add(self._TCTRL_patient_selector, 2, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 3)

		self._LBL_age = wx.StaticText(self, wx.ID_ANY, _("<age>"))
		self._LBL_age.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
		self._LBL_age.SetToolTip(_("The age."))
		__szr_top_row.Add(self._LBL_age, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10)

		self._LBL_allergies = wx.StaticText(self, wx.ID_ANY, _("Caveat"))
		self._LBL_allergies.SetForegroundColour(wx.Colour(255, 0, 0))
		self._LBL_allergies.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
		__szr_top_row.Add(self._LBL_allergies, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 2)

		self._TCTRL_allergies = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
		self._TCTRL_allergies.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
		self._TCTRL_allergies.SetForegroundColour(wx.Colour(255, 0, 0))
		self._TCTRL_allergies.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
		__szr_top_row.Add(self._TCTRL_allergies, 3, wx.ALIGN_CENTER_VERTICAL, 0)

		__szr_bottom_row = wx.BoxSizer(wx.HORIZONTAL)
		__szr_stacked_rows.Add(__szr_bottom_row, 0, wx.EXPAND, 0)

		__szr_bottom_row_left = wx.BoxSizer(wx.HORIZONTAL)
		__szr_bottom_row.Add(__szr_bottom_row_left, 2, wx.EXPAND, 0)

		self._PNL_tags = cImageTagPresenterPnl(self, wx.ID_ANY, style=wx.BORDER_NONE)
		__szr_bottom_row_left.Add(self._PNL_tags, 0, wx.ALIGN_CENTER_VERTICAL, 3)

		self._LBL_lab = wx.StaticText(self, wx.ID_ANY, "", style=wx.ALIGN_CENTER_HORIZONTAL)
		self._LBL_lab.SetToolTip(_("Vitals"))
		__szr_bottom_row_left.Add(self._LBL_lab, 1, wx.ALIGN_CENTER_VERTICAL, 0)

		self._PNL_enc = cActiveEncounterPnl(self, wx.ID_ANY, style=wx.BORDER_SIMPLE)
		__szr_bottom_row.Add(self._PNL_enc, 1, wx.ALIGN_CENTER_VERTICAL, 0)

		self.SetSizer(__szr_main)
		__szr_main.Fit(self)

		self.Layout()
