import turtle

# fill_box(x, y, dx, dy, [color=None])
# box((x1,y1), (x2,y2), [color=None], [width=None])
# box(x1,y1,x2,y2, [color=None], [width=None])
# fill_box_array(x, y, dx, dy, cnt, [add_x=0], [add_y=0], [color=None])
# line(x1, y1, x2, y2, [color=None], [width=None])
# multiline((x1,y1), (x2,y2), ...., (xn,yn) , params)
# set_color([color='black'])
# circle(x, y, r, [color=None], [width=None], [fill_color=None], [fill=False])
# circle_array(x, y, r, cnt, [dx=0], [dy=0], [color=None], [width=None], [fill_color=None], [fill=False]):


def fill_box(x, y, dx, dy, color=None):
    turtle.up()
    turtle.goto(x,y)
    if color:
        turtle.color(color, color)

    turtle.down()
    turtle.begin_fill()
    turtle.setx(x + dx)
    turtle.sety(y + dy)
    turtle.setx(x)
    turtle.sety(y)
    turtle.end_fill()


def box1(x1, y1, x2, y2, color=None, width=None):
    turtle.up()
    turtle.goto(x1, y1)

    if width is not None:
        turtle.pen(pensize=width)

    if color:
        turtle.color(color, color)

    turtle.down()
    turtle.setx(x2)
    turtle.sety(y2)
    turtle.setx(x1)
    turtle.sety(y1)


def box(start, end, color=None, width=None):
    turtle.up()
    turtle.goto(start)

    if width is not None:
        turtle.pen(pensize=width)

    if color:
        turtle.color(color, color)

    x1, y1 = start
    x2, y2 = end

    turtle.down()
    turtle.setx(x2)
    turtle.sety(y2)
    turtle.setx(x1)
    turtle.sety(y1)


def fill_box_array(x, y, dx, dy, cnt, add_x=0, add_y=0, color=None):
    for i in range(cnt):
        fill_box(x, y, dx, dy, color=color)
        x += add_x
        y += add_y


def line(x1, y1, x2, y2, color=None, width=None):
    turtle.up()
    turtle.goto(x1, y1)

    if color:
        turtle.color(color, color)

    if width is not None:
        turtle.pen(pensize=width)

    turtle.down()
    turtle.goto(x2, y2)


def multiline(*points, **params):

    if 'color' in params:
        turtle.color(params['color'])

    if 'width' in params:
        turtle.pen(pensize=params['width'])

    turtle.up()
    turtle.goto(points[0])
    turtle.down()
    for x in points[1:]:
        turtle.goto(x)


def set_color(color='black'):
    turtle.color(color)


def circle(x, y, r, color=None, width=None, fill_color=None, fill=False):
    turtle.up()
    turtle.goto(x, y-r)
    turtle.setheading(0)

    if color:
        turtle.pen(pencolor=color)

    if fill_color:
        turtle.pen(fillcolor=fill_color)

    if width is not None:
        turtle.pen(pensize=width)

    if fill:
        turtle.begin_fill()

    turtle.down()

    turtle.circle(r)

    if fill:
        turtle.end_fill()


def circle_array(x, y, r, cnt, dx=0, dy=0, color=None, width=None, fill_color=None, fill=False):
    for i in range(cnt):
        circle(x, y, r, color=color, width=width, fill_color=fill_color, fill=fill)
        x += dx
        y += dy
