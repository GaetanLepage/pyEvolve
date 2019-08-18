import wx

class Gui(wx.Frame):

    def __init__(self, *args, **kw):
        super(Gui, self).__init__(*args, **kw)
        self.initUI()

    def initUI(self):
        self.SetTitle("Bouh")
        self.Centre()

    def drawGrid(self, grid):
        print("Size : ", self.GetSize())
        print("Grid size : ", grid.size)

