from line import Line,Point

class Cell:
    has_left_wall = True
    has_right_wall = True
    has_top_wall = True
    has_bottom_wall = True
    visited = False
    def __init__(self,_x1,_y1,_x2,_y2,win):
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        self._win = win
        
        
    def draw(self):
        bg_color = self._win.canvas["background"] if self._win else "#d9d9d9"
        
       
        color = "black" if self.has_left_wall else bg_color
        line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        self._win.draw_line(line, color)
        
       
        color = "black" if self.has_right_wall else bg_color
        line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        self._win.draw_line(line, color)
        
      
        color = "black" if self.has_top_wall else bg_color
        line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        self._win.draw_line(line, color)
        
        
        color = "black" if self.has_bottom_wall else bg_color
        line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        self._win.draw_line(line, color)


    def draw_move(self, to_cell, undo=False):
        from_center_x = (self._x1 + self._x2) // 2
        from_center_y = (self._y1 + self._y2) // 2
        to_center_x = (to_cell._x1 + to_cell._x2) // 2
        to_center_y = (to_cell._y1 + to_cell._y2) // 2

        line_color = "grey" if undo else "red"

        self._win.draw_line(Line(Point(from_center_x,from_center_y), Point(to_center_x,to_center_y)),line_color)