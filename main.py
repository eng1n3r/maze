from graphics import Window, Point, Line
from cell import Cell


def main():
    win = Window(800, 600)
    
    p1 = Point(10,10)
    p2 = Point(200, 200)
    l1 = Line(p1,p2)
    win.draw_line(l1, "Black")
    c1 = Cell(win)
    c1.has_left_wall = False
    c1.draw(100,100,200,200)
    c2 = Cell(win)
    c2.draw(200,100,300,200)
    c1.draw_move(c2)
    a = c1.__centre_point
    print(a)


    win.wait_for_close()

main()