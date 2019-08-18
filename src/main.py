import wx
from app.gui import *
from entities.grid import *

def main():
    grid = Grid(20)

    app = wx.App()

    gui = Gui(None)
    gui.drawGrid(grid)
    gui.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
