from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_triangle():
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(100, 100)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(150, 200)
    glColor3f(.0, 0.0, 1.0)
    glVertex2f(200, 100)



    #jekhane show korbe pixel
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_triangle()


    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()