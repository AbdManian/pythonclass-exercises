import turtle
import drawengine

turtle.speed(0)


X, Y = -100, -70
W, H = 140, 200


#########################################################################
drawengine.box1(X-50, Y-50, X+H+50, Y+W+50, color='gray')
drawengine.set_color()

# Draw Boards
drawengine.fill_box(X-2, Y-2, H+4, W+4)
drawengine.fill_box(X, Y, H, W, color='green')
drawengine.set_color()

# Draw Holes
drawengine.circle(X + 10, Y + 10, 8, width=2, fill=True, fill_color='white')
drawengine.circle(X + H - 10, Y + 10, 8, fill=True)
drawengine.circle(X + H - 10, Y + W - 10, 8, fill=True)
drawengine.circle(X + 10, Y + W - 10, 8, fill=True)

# Draw Connector
drawengine.circle_array(X + 10, Y + 40, 4, 5, dy=15, fill=True)
drawengine.circle_array(X + H - 10, Y + 50, 4, 4, dy=15, fill=True)

# Draw IC
drawengine.set_color()
drawengine.fill_box_array(X + 70, Y + 80, 10, 4, cnt=4, add_y=-12)
drawengine.fill_box_array(X + 100, Y + 80, 10, 4, cnt=4, add_y=-12)


# Draw wires
drawengine.line(-87.00, -30.00, -33.00, -30.00)
drawengine.line(-33.00, -30.00, -27.00, -23.00)
drawengine.line(-88.00, -15.00, -39.00, -15.00)
drawengine.line(-29.00, -11.00, -39.00, -15.00)

# Draw wires
drawengine.multiline((-87.00, 30.00), (-48.00, 30.00), (-36.00, 19.00), (-11.00, 19.00), (-6.00, 13.00), (2.00, 13.00))
drawengine.multiline((3.00, 0.00), (51.00, 0.00), (65.00, 24.00), (86.00, 24.00))
drawengine.multiline((-89.00,16.00),(-46.00,16.00),(-25.00,13.00))
drawengine.multiline((-88.00,-0.00), (-29.00, 0.00))
drawengine.multiline((85.00,11.00),(67.00,11.00),(54.00,-11.00),(5.00,-11.00))
drawengine.multiline((9.00,-24.00),(64.00,-24.00),(73.00,-6.00),(85.00,-6.00))

# Draw Overlay
drawengine.box((-36.00,18.00), (15.00,-31.00), color='yellow', width=2)
drawengine.box((-97.00,36.00), (-83.00,-36.00))
drawengine.box((83.00,32.00), (96.00,-28.00))
#######################################################################################



turtle.color('black', 'white')
turtle.up()
turtle.goto(-300, -300)

turtle.done()
