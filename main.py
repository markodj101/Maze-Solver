from tkinter import Tk, BOTH, Canvas
from line import Line,Point
from cell import Cell
from maze import Maze


class Window:
    def __init__(self,width,height,title):
        self.width = width
        self.height = height
        self.root= Tk()
        self.title = title
        self.root.title(title)
        self.canvas = Canvas(self.root, width=self.width,height=self.height)
        self.canvas.pack()
        self.isRunning = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def close(self):
        self.isRunning = False

    def wait_for_close(self):
        self.isRunning = True
        while self.isRunning:
            self.redraw()

    def draw_line(self, line,color):
        line.draw(self.canvas,color)
        
def main():
    print("Starting...")
    screen_x = 800
    screen_y = 600
    x1=50
    y1=50
    num_rows=10
    num_cols=10
    cell_size_x= (screen_x - 2 * x1) / num_cols
    cell_size_y= (screen_y - 2 * y1) / num_rows

    win = Window(screen_x,screen_y,"MAze SOlver")


    maze = Maze(
    x1,
    y1,
    num_rows,
    num_cols,
    cell_size_x,
    cell_size_y,
    win
)
    
    maze.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()