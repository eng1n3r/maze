from graphics import Line, Point

class Cell:
    def __init__(self,window=None):
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
        self.visited = False
    
    def draw(self,x1,y1,x2,y2):
        if self.__win is None:
            return
        
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__centre_point = Point((self.__x2-self.__x1)/2 + self.__x1, (self.__y2-self.__y1)/2 + self.__y1) #may need to add abs here

        if self.has_left_wall:
            colour = "black"
        else:
            colour = "white"
        self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), colour)
        
        if self.has_top_wall:
            colour = "black"
        else:
            colour = "white"

        self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), colour)
        
        if self.has_right_wall:
            colour = "black"
        else:
            colour = "white"
        self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), colour)

        if self.has_bottom_wall:
            colour = "black"
        else:
            colour = "white"
        self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), colour)

    def draw_move(self, to_cell, undo=False):
        if self.__win is None:
            return
        fill_colour = "Red"
        if undo:
            fill_colour = "Grey"
        self.__win.draw_line(Line(self.__centre_point,to_cell.__centre_point), fill_colour)