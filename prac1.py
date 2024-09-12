from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 500, 800

speed = 0.1
game_over = False
t = 0
bubbles = []  # List to hold bubble data

def animate():
    global t, bubbles
    
    t += 0.01
    if t >= 5:
        t = 0
        # Create a new bubble at a random x position
        rand_x = random.randint(-235, 235)
        bubbles.append({'x': rand_x, 'y': 200})
    
    

    # Update the position of each bubble
    for bubble in bubbles:
        bubble['y'] -= speed
        # Remove bubble if it goes off-screen
        if bubble['y'] < -15:
            bubbles.remove(bubble)
    
    glutPostRedisplay()

def plot_circle_points(x_center, y_center, x, y, color):
    red, green, blue = color
    glPointSize(2)
    glBegin(GL_POINTS)
    glColor3f(red, green, blue)
    glVertex2f(x_center + x, y_center + y)
    glVertex2f(x_center - x, y_center + y)
    glVertex2f(x_center + x, y_center - y)
    glVertex2f(x_center - x, y_center - y)
    glVertex2f(x_center + y, y_center + x)
    glVertex2f(x_center - y, y_center + x)
    glVertex2f(x_center + y, y_center - x)
    glVertex2f(x_center - y, y_center - x)
    glEnd()

def draw_circle(x_center, y_center, radius, color):
    x = 0
    y = radius
    d = 1 - radius
    plot_circle_points(x_center, y_center, x, y, color)
    while x < y:
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
        plot_circle_points(x_center, y_center, x, y, color)

def diamond():
    global bubbles
    for bubble in bubbles:
        x = bubble['x']
        y = bubble['y']
        draw_circle(x, y, 15, [1.0, 0.0, 0.0])

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    
    if not game_over:
        diamond()
    
    glutSwapBuffers()

def init():
    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104, 1, 1, 1000.0)

glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
wind = glutCreateWindow(b"Bubble Animation")
init()
glutIdleFunc(animate)
glutDisplayFunc(display)
glutMainLoop()
