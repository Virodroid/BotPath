from tkinter import Canvas

class Grid:

    def __init__(self, dim, obst=[], bots=[]):
        self.dim = dim
        self.bots = bots
        self.obst = obst
        self.initGridInfo()

    def initGridInfo(self):
        self.gridInfo = []
        for i in range(self.dim[0]):
            self.gridInfo.append([])
            for j in range(self.dim[1]):
                self.gridInfo[i].append(-1)
        
        for pos in self.obst:
            self.gridInfo[pos["x"]][pos["y"]] = 0

    def makeGrid(self, window):
        self.canvas = Canvas(window, width=(self.dim[0]*100), height=(self.dim[1]*100))
        self.canvas.pack()

    def updateGrid(self, squareSize=100):
        for j in range(self.dim[1]):
            augJ = j*squareSize
            for i in range(self.dim[0]):
                augI = i*squareSize
                if self.gridInfo[i][j]==0:
                    self.canvas.create_rectangle(augI, augJ, augI+squareSize, augJ+squareSize, fill="black")
                else:
                    self.canvas.create_rectangle(augI, augJ, augI+squareSize, augJ+squareSize)