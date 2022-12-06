import tkinter as tk
from MazeGenerator import MazeGenerator
from Maze import W
import tkinter.messagebox as messagebox
from Maze import Maze
from MazeSolver import MazeSolver

class  MazeApp:
    def __init__(self):
        window = tk.Tk()
        window.title("Maze Generator and Solver")

        scrollbar = tk.Scrollbar(window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.mazeFrame = tk.Frame(window)
        self.mazeCanvas = tk.Canvas(self.mazeFrame)
        self.changeCanvasSize()
        self.mazeCanvas.pack(fill=tk.BOTH, expand=True)
        self.mazeFrame.pack(fill=tk.BOTH, expand=True)

        self.optionFrame = tk.Frame(window)
        self.optionFrame.pack(fill=tk.BOTH, expand=True)

        self.mazeSizeLabel = tk.Label(self.optionFrame, text="Maze Size")
        self.mazeSizeLabel.pack(side=tk.LEFT)
        self.mazeSizeEntry = tk.Entry(self.optionFrame)
        self.mazeSizeEntry.pack(side=tk.LEFT)
        self.mazeSizeEntry.insert(0, "10")
        self.u = W / int(self.mazeSizeEntry.get())

        self.currMaze: Maze = None

        def btnGenerateClick():
            w = int(self.mazeSizeEntry.get())
            self.u = self.generateNewMaze(w, w)
            

        self.generateButton = tk.Button(self.optionFrame, text="Generate",
                                            command=btnGenerateClick)
        self.generateButton.pack(side=tk.LEFT)
        self.solveButton = tk.Button(self.optionFrame, text="Solve",
                                            command=self.solveCurrentMaze)
        self.solveButton.pack(side=tk.LEFT)

        # bind mouse click to maze canvas
        self.start = None
        self.end = None
        self.mazeCanvas.bind("<Button-1>", self.mouseClick)
        window.mainloop();

    def mouseClick(self, event):
        x = int(event.x / self.u)
        y = int(event.y / self.u)

        if self.currMaze is None:
            return

        if(x >= self.currMaze.width or y >= self.currMaze.height):
            return

        if self.start is None:
            self.start = (y, x)
            self.startRect = self.mazeCanvas.create_rectangle(
                x * self.u, y * self.u, x * self.u + self.u, y * self.u + self.u, fill="yellow")
        elif self.end is None:
            self.end = (y, x)
            self.endRect = self.mazeCanvas.create_rectangle(
                x * self.u, y * self.u, x * self.u + self.u, y * self.u + self.u, fill="red")
        else:
            self.mazeCanvas.delete(self.startRect)
            self.start = (y, x)
            self.startRect = self.mazeCanvas.create_rectangle(
                x * self.u, y * self.u, x * self.u + self.u, y * self.u + self.u, fill="yellow")
            self.end = None
            self.mazeCanvas.delete(self.endRect)

    def generateNewMaze(self, width, height):
        self.mazeCanvas.delete(tk.ALL)
        self.start = None
        self.end = None
        self.changeCanvasSize()

        maze = MazeGenerator(width, height)
        try:
            maze.generate()
            self.currMaze = Maze(maze.grid)
            self.currMaze.draw(self.mazeCanvas)
        except:
            print('Can\'t generate maze because size is too big')
            self.showMessageBox("Can't generate maze", "Can't generate maze because size is too big")
        return W / width

    def showMessageBox(self, title, message):
        messagebox.showinfo(title, message)

    def changeCanvasSize(self):
        self.mazeCanvas.config(width=W, height=W)

    def solveCurrentMaze(self):
        if self.currMaze is None:
            self.showMessageBox("Can't solve", "Can't solve because no maze is generated")
            return
        if self.start is None or self.end is None:
            self.showMessageBox("Can't solve maze", "Please select start and end points")
            return

        self.currMaze.draw(self.mazeCanvas)
        self.mazeCanvas.create_rectangle(
            self.end[1] * self.u, self.end[0] * self.u, self.end[1] * self.u + self.u, self.end[0] * self.u + self.u, fill="orange")
        self.mazeCanvas.create_rectangle(
            self.start[1] * self.u, self.start[0] * self.u, self.start[1] * self.u + self.u, self.start[0] * self.u + self.u, fill="green")

        maze = MazeSolver(self.currMaze)
        try:
            solution = maze.solve(self.start, self.end, self.mazeCanvas)
        except:
            self.showMessageBox("Can't solve maze", "It's take too many steps to solve this maze")
            return
        if not solution:
            self.showMessageBox("Can't solve maze", "Can't solve because invalid start or end points")