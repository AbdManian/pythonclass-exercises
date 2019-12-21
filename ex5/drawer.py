import turtle
f = open('Tracing.tc', 'r')


def line_to_points(lp):
    ret = []

    for point in lp.split():
        sx, sy = point.split(',')
        ret.append((float(sx), float(sy)))
    return ret


def rp(point):
    cur_pos = turtle.pos()
    return point[0]+cur_pos[0], point[1]+cur_pos[1]


for line in f:
    line = line.strip()

    if not line:
        continue

    if line[0] == 'M':
        points = line_to_points(line[1:])
        origin, segments = points[0], points[1:]
        turtle.penup()
        turtle.goto(origin)
        turtle.pendown()
        for p in segments:
            turtle.goto(p)

    elif line[0] == 'm':
        points = line_to_points(line[1:])
        origin, segments = points[0], points[1:]
        turtle.penup()
        turtle.goto(rp(origin))
        turtle.pendown()
        for p in segments:
            turtle.goto(rp(p))



    if line[0].upper() in 'VH':
        print(line)


f.close()


turtle.forward(330)
turtle.left(90)
turtle.forward(330)
turtle.done()
