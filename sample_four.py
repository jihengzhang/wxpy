# sample_four.py

"""

Link : https://matplotlib.org/3.3.1/gallery/user_interfaces/embedding_in_wx5_sgskip.html

"""

import os
import sys
import wx
import wx.lib.agw.aui as aui
import matplotlib as mpl
from matplotlib.backends.backend_wxagg import (
    FigureCanvasWxAgg as FigureCanvas,
    NavigationToolbar2WxAgg as NavigationToolbar)

# class MyPlot
# class MyPlotNotebook
# class Myframe
# class MyApp

#---------------------------------------------------------------------------

class MyPlot(wx.Panel):
    def __init__(self, parent, id=-1, dpi=None, **kwargs):
        wx.Panel.__init__(self, parent, id=id, **kwargs)

        #------------
        
        self.figure = mpl.figure.Figure(dpi=dpi, figsize=(2, 2))

        #------------
        
        self.canvas = FigureCanvas(self, -1, self.figure)

        #------------
        
        self.toolbar = NavigationToolbar(self.canvas)
        self.toolbar.Realize()

        #------------
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.canvas, 1, wx.EXPAND)
        sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.SetSizer(sizer)

#---------------------------------------------------------------------------
        
class MyPlotNotebook(wx.Panel):
    def __init__(self, parent, id=-1):
        wx.Panel.__init__(self, parent, id=id)
        
        #------------
        
        self.nb = aui.AuiNotebook(self)

        #------------
        
        sizer = wx.BoxSizer()
        sizer.Add(self.nb, 1, wx.EXPAND)
        self.SetSizer(sizer)

    #-----------------------------------------------------------------------
        
    def Add(self, name="plot"):
        """
        ...
        """
        
        page = MyPlot(self.nb)
        self.nb.AddPage(page, name)
        return page.figure

#---------------------------------------------------------------------------

class MyFrame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, -1,
                          title,
                          size=(450, 350))

        #------------

        # Return icons folder.
        self.icons_dir = wx.GetApp().GetIconsDir()

        #------------
        
        # Simplified init method.
        self.SetProperties()
        self.CreateCtrls()
        
    #-----------------------------------------------------------------------

    def SetProperties(self):
        """
        ...
        """

        self.SetMinSize((450, 350))

        #------------

        frameIcon = wx.Icon(os.path.join(self.icons_dir,
                                         "wxwin.ico"),
                            type=wx.BITMAP_TYPE_ICO)
        self.SetIcon(frameIcon)


    def CreateCtrls(self):
        """
        ...
        """
        
        plotter = MyPlotNotebook(self)
        axes1 = plotter.Add('figure 1').gca()
        axes1.plot([1, 2, 3], [2, 1, 4])
        axes2 = plotter.Add('figure 2').gca()
        axes2.plot([1, 2, 3, 4, 5], [2, 1, 4, 2, 3])
    
#---------------------------------------------------------------------------

class MyApp(wx.App):    
    def OnInit(self):

        #------------

        self.installDir = os.path.split(os.path.abspath(sys.argv[0]))[0]
        
        #------------
        
        frame = MyFrame("Sample four")
        self.SetTopWindow(frame)
        frame.Show(True)

        return True
    
    #-----------------------------------------------------------------------
    
    def GetInstallDir(self):
        """
        Return the installation directory for my application.
        """

        return self.installDir


    def GetIconsDir(self):
        """
        Return the icons directory for my application.
        """

        icons_dir = os.path.join(self.installDir, "icons")
        return icons_dir
    
#---------------------------------------------------------------------------

def main():
    app = MyApp(False)
    app.MainLoop()

#---------------------------------------------------------------------------

if __name__ == "__main__" :
    main()
    
