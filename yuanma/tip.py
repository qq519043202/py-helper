# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 08:25:10 2015

@author: admin
"""

import wx

if __name__ == "__main__":
    app = wx.PySimpleApp()
    provider = wx.CreateFileTipProvider("tips.txt", 0)
    wx.ShowTip(None, provider, True)