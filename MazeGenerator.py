import enum
import random

class Directions(enum.Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class MazeGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[1 for _ in range(width)] for _ in range(height)]
        self.visited = [[0 for _ in range(width)] for _ in range(height)]

    def generate(self):
        randomX = random.randint(0, self.height - 1)
        randomY = random.randint(0, self.width - 1)
        self.backtracking(randomX, randomY)

    def setWalkable(self, x, y):
        self.grid[x][y] = 0

    def markVisited(self, x, y):
        self.visited[x][y] = 1

    def isVisited(self, x, y):
        return self.visited[x][y] == 1

    def isSafe(self, x, y):
        if x < 0 or x >= self.height or y < 0 or y >= self.width:
            return False
        if self.visited[x][y] == 1:
            return False
        return True

    def backtracking(self, x, y):
        self.markVisited(x, y)
        self.setWalkable(x, y)
        directions = [Directions.UP, Directions.DOWN,
                      Directions.LEFT, Directions.RIGHT]

        random.shuffle(directions)

        for direction in directions:
            if direction == Directions.UP:
                nextX = x - 2
                nextY = y
                adjacentX = x - 1
                adjacentY = y
            elif direction == Directions.DOWN:
                nextX = x + 2
                nextY = y
                adjacentX = x + 1
                adjacentY = y
            elif direction == Directions.LEFT:
                nextX = x
                nextY = y - 2
                adjacentX = x
                adjacentY = y - 1
            elif direction == Directions.RIGHT:
                nextX = x
                nextY = y + 2       
                adjacentX = x
                adjacentY = y + 1

            if self.isSafe(nextX, nextY):
                if not self.isVisited(nextX, nextY):
                    self.setWalkable(adjacentX, adjacentY)
                    self.backtracking(nextX, nextY)
