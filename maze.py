from line import Line,Point
from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win):
        self.x1=x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win =win
        self._cells = []

        self._create_cells()
    
    def _create_cells(self):
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                x1 = self.x1 + j*self.cell_size_x
                y1 = self.y1 + i*self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y

                cell = Cell(x1,y1,x2,y2,self.win)
                row.append(cell)
            self._cells.append(row) 

        
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i,j)
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()


    def _draw_cell(self,i,j):
        cell = self._cells[i][j]
        cell.draw()
        self.win.redraw()
        self._animate()

    def solve(self):
        return self._solver_r(0,0)

    def _solver_r(self,i,j):
        self._animate()
        current = self._cells[i][j]
        current.visited = True

        if i==self.num_rows-1 and j == self.num_cols-1:
            return True
        
        directions = [("left", (i, j-1), "has_left_wall"),
        ("right", (i, j+1), "has_right_wall"),
        ("up", (i-1, j), "has_top_wall"),
        ("down", (i+1, j), "has_bottom_wall")]

        for directions, (ni, nj),wall_attr in directions:
            if 0<=ni < self.num_rows and 0<= nj< self.num_cols:
                neighbor = self._cells[ni][nj]
                if not getattr(current, wall_attr) and not neighbor.visited:
                    current.draw_move(neighbor)
                    if self._solver_r(ni,nj):
                        return True

                    current.draw_move(neighbor,undo=True)

        return False

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited = False

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit = self._cells[-1][-1]
        
        entrance.has_top_wall = False
        entrance.draw()

        exit.has_bottom_wall= False
        exit.draw()

    def _break_walls_r(self, i, j):
        
        current = self._cells[i][j]
        current.visited = True

        while True:
            directions = []
            if j>0 and not self._cells[i][j-1].visited:
                directions.append("left")
            if j< self.num_cols-1 and not self._cells[i][j+1].visited:
                directions.append("right")
            if i>0 and not self._cells[i-1][j].visited:
                directions.append("up")
            if i< self.num_rows-1 and not self._cells[i+1][j].visited:
                directions.append("down")
            
            if not directions:
                self._draw_cell(i,j)
                return
            
            direction = random.choice(directions)

            if direction == "left":
                current.has_left_wall = False
                self._cells[i][j-1].has_right_wall = False
                self._break_walls_r(i,j-1)
            elif direction == "right":
                current.has_right_wall = False
                self._cells[i][j+1].has_left_wall = False
                self._break_walls_r(i,j+1)
            elif direction == 'up':
                current.has_top_wall = False
                self._cells[i-1][j].has_bottom_wall = False
                self._break_walls_r(i-1, j)
            elif direction == 'down':
                current.has_bottom_wall = False
                self._cells[i+1][j].has_top_wall = False
                self._break_walls_r(i+1, j)    
            
            self._draw_cell(i,j)