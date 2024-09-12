from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 500,500
move=0
change_value=0

def drawRain(move):
    glLineWidth(1)

    num_raindrops = 300


    raindrops = [(random.randint(-250, 250), random.randint(0, 250)) for i in range(num_raindrops)]
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    print(raindrops)
    for x, y in raindrops:
        glVertex2f(x, y)
        glVertex2f(x+move, y - 20)
    glEnd()
    glutPostRedisplay()
def moveRainDirection(key,x,y):
    global move
    if (key==GLUT_KEY_LEFT):
        move = -5
    if (key==GLUT_KEY_RIGHT):
        move = 5
def day_night_change(key,x,y):
    global change_value
    if key == b'n':
        if(change_value<=1.0):
            change_value += 0.1
        print(key)
    if key == b'd':
        if (change_value >= 0):
            change_value -= 0.1

    glutPostRedisplay()
def drawHouse():
    glLineWidth(5)
    glBegin(GL_TRIANGLES)
    glColor3f(0.0,1.0,1.0)
    #triangle1
    glVertex2d(-200, 0)
    glVertex2d(200, 0)
    glVertex2d(0, 100)
    #triangle 2
    glColor3f(1.0,1.0,0.0)
    glVertex2d(-180, 5)
    glVertex2d(180, 5)
    glVertex2d(0, 95)
    glEnd()
    #home boorder
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(0.0,1.0,1.0)
    glVertex2d(-180, 0)
    glVertex2d(-180, -150)
    glVertex2d(180, 0)
    glVertex2d(180, -150)

    glVertex2d(-180, 0)
    glVertex2d(180, 0)

    glVertex2d(-181, -150)
    glVertex2d(181, -150)
    glEnd()

    #triangles inside home

    glBegin(GL_TRIANGLES)
    glColor3f(1.0,1.0,0.0)
    #triangle1
    glVertex2d(-179, 0)
    glVertex2d(-179, -148)
    glVertex2d(179, -148)
    glEnd()

    #triangle-2
    glBegin(GL_TRIANGLES)
    glColor3f(1.0,1.0,0.0)
    #triangle1
    glVertex2d(-179, 0)
    glVertex2d(179, -148)
    glVertex2d(179, 0)
    glEnd()

    #door
    glBegin(GL_LINES)

    glColor3f(0.0, 0.0, 1.0)
    glVertex2d(-150, -148)
    glVertex2d(-150, -70)

    glVertex2d(-110, -148)
    glVertex2d(-110, -70)

    glVertex2d(-109, -70)
    glVertex2d(-151, -70)

    glEnd()
    glPointSize(5)
    glBegin(GL_POINTS)

    glColor3f(0.0, 0.0, 1.0)
    glVertex2d(-120, -120)
    glEnd()

    #window
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2d(150, -20)
    glVertex2d(150, -60)

    glVertex2d(90, -20)
    glVertex2d(90, -60)

    glVertex2d(89, -20)
    glVertex2d(151, -20)
    glVertex2d(89, -60)
    glVertex2d(151, -60)

    #grill
    glVertex2d(120, -20)
    glVertex2d(120, -60)
    glVertex2d(90, -40)
    glVertex2d(151, -40)

    glEnd()



def display():
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(1-change_value,1-change_value,1-change_value,1-change_value);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()

    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)

    drawRain(move)
    drawHouse()

    glutSwapBuffers()


def init():
    #//clear the screen
    glClearColor(1,1,1,1)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)



glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)


wind = glutCreateWindow(b"assignment-1 task1")
init()

glutDisplayFunc(display)
glutIdleFunc(drawRain(move))
glutSpecialFunc(moveRainDirection)
glutKeyboardFunc(day_night_change)


glutMainLoop()