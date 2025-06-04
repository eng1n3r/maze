from graphics import Line, Point

class Cell:
    def __init__(self,window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self.__centre_point = -1
    
    def draw(self,x1,y1,x2,y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__centre_point = Point((self.__x2-self.__x1)/2, (self.__y2-self.__y1/2))

        if self.has_left_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), "black")
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), "black")
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), "black")
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), "black")
    
    def draw_move(self, to_cell, undo=False):
        if undo:
            self.__win.draw_line(Line(self.__centre_point,to_cell.__centre_point), "Grey")
        self.__win.draw_line(Line(self.__centre_point,to_cell.__centre_point), "Red")