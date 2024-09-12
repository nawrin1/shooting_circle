from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 500,500
ballx=0
bally=0
points=[]
speed=0.01
blink=False
freeze_points=False
def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y
    return a,b
def mouseListener(button, state, x, y):
    global points, ballx, bally, blink
    if(not freeze_points):
        if button == GLUT_RIGHT_BUTTON:
            if (state == GLUT_DOWN):
                c_X, c_y = convert_coordinate(x, y)
                ballx = c_X
                bally = c_y
                xdirection = random.choice([1, -1])
                ydirection = random.choice([1, -1])
                color_red = random.choice([0, 1])
                color_green = random.choice([0, 1])
                color_blue = random.choice([0, 1])
                points.append([ballx, bally, xdirection, ydirection, color_red, color_green, color_blue])
                # print(points, "what")
                glutPostRedisplay()
        if button == GLUT_LEFT_BUTTON:
            if (state == GLUT_DOWN):
                blink = True
                print(blink)
            else:
                blink =False
        glutPostRedisplay()



   # glutPostRedisplay()
def drawPoints():

    global points,blink
    glPointSize(10)
    glBegin(GL_POINTS)

    for i in points:
        if blink:
            glColor3f(0.0, 0.0, 0.0)
        else:
            glColor3d(i[4], i[5], i[6])

        glVertex2f(i[0], i[1])
        # blink=False

    glEnd()
    # blink = not blink





def points_move():
    glutPostRedisplay()
    global points, speed, freeze_points
    if (not freeze_points):

       for i in points:
        # print(i[0])
            [ballx, bally, xdirection, ydirection, color_red, color_green, color_blue]=i

            ballx += xdirection*speed
            bally += ydirection*speed


            if ballx >= W_Width / 2:
                # ballx = W_Width / 2

                xdirection = -xdirection
                ballx+=xdirection
            elif ballx <= -W_Width / 2:

                xdirection = -xdirection
                ballx  +=xdirection


            if bally >= W_Height / 2:

                ydirection = -ydirection
                bally +=ydirection
            elif bally <= -W_Height / 2:

                ydirection = -ydirection
                bally +=ydirection


            i[0] = ballx
            i[1] = bally
            i[2] = xdirection
            i[3] = ydirection

       glutPostRedisplay()

def changespeed(key, x, y):
    global speed

    if key==GLUT_KEY_UP:
        speed += 0.1
    if key== GLUT_KEY_DOWN:
        if(speed >=0.0):
            speed -= 0.1
        if speed<=0.0:
            speed=0.0
    glutPostRedisplay()


def freeze(key,x,y):
    global freeze_points
    if key == b' ':
        freeze_points = not freeze_points


def display():

    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)


    drawPoints()


    glutSwapBuffers()


def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance




glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"assignment-1 task2")
init()

glutDisplayFunc(display)
glutMouseFunc(mouseListener)

glutIdleFunc(points_move)
glutSpecialFunc(changespeed)
glutKeyboardFunc(freeze)

glutMainLoop()