from multiprocessing import set_forkserver_preload
from tkinter.ttk import Style
import wx

class MainWindow(wx.Frame):
    def __init__(self, parent, title):

        super(MainWindow, self).__init__(parent, title = title, size = (1280,800))
        self.Centre()
        mainPanel(self)
        self.CreateStatusBar()
        self.createMenu()

    def createMenu(self):

        menu= wx.Menu()
        menuExit = menu.Append(wx.ID_EXIT, "E&xit", "Quit application")

        menuBar = wx.MenuBar()
        menuBar.Append(menu,"&File")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

    def OnExit(self, event):
        self.Close(True) #Close the frame

class mainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.SetBackgroundColour('gray')
        self.sourcelist = wx.ListCtrl(self, Style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.sourcelist.InsertColumn(0,"Source", width=200)
        self.news_list = wx.ListCtrl(self, size = (-1 , - 1), style=wx.LC_REPORT | wx.BORDER_SUNKEN)
        self.news_list.InsertColumn(0, 'Link')
        self.news_list.InsertColumn(1, 'Title')

        




if __name__ == '__main__':
    app = wx.App()
    window= MainWindow(None, "Newsy - read worldwide news!")
    window.Show()
    app.MainLoop()
