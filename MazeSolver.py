from Maze import Maze
import tkinter as tk
from typing import Tuple
import time

class MazeSolver:
    def __init__(self, maze:Maze):
        self.maze = maze
        self.width = maze.width
        self.height = maze.height

        self.solution = [[0 for i in range(self.width)]
                         for j in range(self.height)]
        self.visited = []
        print(self.visited)
        self.u = maze.u

    

    def solve(self, start: Tuple[int, int], end: Tuple[int, int], canvas: tk.Canvas):
        if not self.maze.isSafe(start[0], start[1]) or not self.maze.isSafe(end[0], end[1]):
            return False
        self.solution[start[0]][start[1]] = 1

        def backtracking(x, y, end: Tuple[int, int]):
            time.sleep(0.0001)

            def isGoal(x, y):
                return x == end[0] and y == end[1]
            
            if isGoal(x, y):
                self.solution[x][y] = 1
                return True

            if (x, y) in self.visited:
                return False

            if self.maze.isSafe(x, y):
                self.solution[x][y] = 1
                self.visited.append((x, y))

                currRect = canvas.create_rectangle(
                    y * self.u, x * self.u, y * self.u + self.u, x * self.u + self.u, fill="blue")
                canvas.update()
                if backtracking(x + 1, y, end):
                    return True
                if backtracking(x - 1, y, end):
                    return True
                if backtracking(x, y + 1, end):
                    return True
                if backtracking(x, y - 1, end):
                    return True

                self.solution[x][y] = 0
                canvas.delete(currRect)
                canvas.update()
                return False

            return False
        return backtracking(start[0], start[1], end)

    def draw(self, canvas: tk.Canvas):
        for x in range(self.height):
            for y in range(self.width):
                if self.maze.grid[x][y] == 1:
                    canvas.create_rectangle(
                        y * self.u, x * self.u, y * self.u + self.u, x * self.u + self.u, fill="black")
                else:
                    canvas.create_rectangle(
                        y * self.u, x * self.u, y * self.u + self.u, x * self.u + self.u, fill="white")
                if self.solution[x][y] == 1:
                    canvas.create_rectangle(
                        y * self.u, x * self.u, y * self.u + self.u, x * self.u + self.u, fill="blue")
