import tkinter as tk

W = 600
class Maze:
    def __init__(self,grid):
        self.grid = grid
        self.width = len(grid[0])
        self.height = len(grid)
        self.u = W/self.width
    
    def isSafe(self,row,col):
        return row >= 0 and row < self.height and col >= 0 and col < self.width and self.grid[row][col] == 0

    def draw(self, canvas: tk.Canvas):
        for x in range(self.height):
            for y in range(self.width):
                if self.grid[x][y] == 1:
                    canvas.create_rectangle(
                        y * self.u, x * self.u, y * self.u + self.u, x * self.u + self.u, fill="black")
                else:
                    canvas.create_rectangle(
                        y * self.u, x * self.u, y * self.u + self.u, x * self.u + self.u, fill="white")
