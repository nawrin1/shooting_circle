from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

W_Width, W_Height = 500, 800


global_y_position_reciever = -240

dNE = 0
dE = 0



randx = 0
pause = False
score = 0
t=0
move=0
project_pos=0
bubble_score=0
reciever_center=0
reciever_radius=0
reciever_center_y=0




speed = 0.1
game_over = False


rx=[]

bubbles=[]
projectiles=[]
missed=0
projectile_missed=0




def convertZone(x1, y1, x2, y2, zone):
    # all are converted for zero zone

    if (zone == 1):
        return [y1, x1, y2, x2]
    elif (zone == 2):
        return [y1, abs(x1), y2, abs(x2)]
    elif (zone == 3):
        return [abs(x1), y1, abs(x2), y2]
    elif (zone == 4):
        return [abs(x1), y1, abs(x2), abs(x2)]
    elif (zone == 5):
        return [abs(y1), abs(x1), abs(y2), abs(x2)]
    elif(zone == 6):
        return [abs(y1), abs(x2), abs(y2), abs(x2)]
    elif(zone == 7):
        return [x1, -y1, x2, -y2]




def findZone(x1,y1,x2,y2,red,green,blue):
    global zone,drawx1,drawx2,drawy1,drawy2,red1,green1,blue1
    red1=red
    green1=green
    blue1=blue
    dx=x2-x1
    dy=y2-y1
    # print(dx,dy,"from 114")
    if(dx>=0 and dy>=0 and (abs(dx)>=abs(dy))):
        # print("inside 0")
        zone=0
        drawx1=x1
        drawy1=y1
        drawx2=x2
        drawy2=y2
        drawLine()



    elif (dx>=0 and dy>=0 and (abs(dx)<=abs(dy))):
        zone = 1
        drawx1=y1
        drawy1=x1
        drawx2=y2
        drawy2=x2
        drawLine()
    elif (dx<=0 and dy>=0 and (abs(dx)<=abs(dy))):
        zone = 2
        drawx1=y1
        drawy1=-x1
        drawx2=y2
        drawy2=-x2
        drawLine()
    elif (dx<=0 and dy>=0 and (abs(dx)>=abs(dy))):
        zone = 3
        drawx1=-x1
        drawy1=y1
        drawx2=-x2
        drawy2=y2
        drawLine()
    elif (dx<=0 and dy<=0 and (abs(dx)>=abs(dy))):
        zone = 4
        drawx1=-x1
        drawy1=-y1
        drawx2=-x2
        drawy2=-y2
        drawLine()
    elif (dx<=0 and dy<=0 and (abs(dx)<=abs(dy))):
        zone = 5
        drawx1=-y1
        drawy1=-x1
        drawx2=-y2
        drawy2=-x2
        drawLine()
    elif (dx>=0 and dy<=0 and (abs(dx)<=abs(dy))):
        zone = 6
        drawx1=-y1
        drawy1=x1
        drawx2=y2
        drawy2=-x2
        drawLine()
    elif (dx>=0 and dy<=0 and (abs(dx)>=abs(dy))):
        zone = 7
        drawx1=x1
        drawy1=-y1
        drawx2=x2
        drawy2=-y2
        drawLine()


def change_points(x,y):
    if(zone==0):

        newx=x
        newy=y
        return[newx,newy]
    elif(zone==1):

        newx=y
        newy=x
        return[newx,newy]
    elif(zone==2):

        newx=-y
        newy=x
        return[newx,newy]
    elif(zone==3):

        newx=-x
        newy=y
        return[newx,newy]
    elif(zone==4):

        newx=-x
        newy=-y
        return[newx,newy]
    elif(zone==5):

        newx=-y
        newy=-x
        return[newx,newy]
    elif(zone==6):

        newx=y
        newy=-x
        return[newx,newy]
    elif(zone==7):

        newx=x
        newy=-y
        return[newx,newy]

def drawLine():
    global drawx1,drawx2,drawy1,drawy2,red1,green1,blue1
    
    [drawnewx1, drawnewy1] = change_points(drawx1, drawy1)
    # print(drawnewx1,drawnewy1,"first point draw")
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3f(red1,green1,blue1)
    glVertex2f(drawnewx1, drawnewy1)
    glEnd()


     # finding all param
    dx = drawx2 - drawx1
    dy = drawy2 - drawy1
    dinit=2*dy-dx

    dNE=2*dy-2*dx
    dE=2*dy
   
    while(drawx1<=drawx2):
        if(dinit)>0:
            drawy1+=1
            drawx1+=1
            dinit=dinit+dNE
            # print(drawx1,drawy1,dinit)
        elif(dinit<=0):
            drawx1 += 1
            dinit = dinit + dE
            # print(drawx1,drawy1,dinit)

        # converting the pixel to previous zone
        [drawnewx1,drawnewy1]=change_points(drawx1,drawy1)
        # print(drawnewx1,drawnewy1,"final")
        glPointSize(3)
        glBegin(GL_POINTS)
        glColor3f(red1, green1, blue1)
        glVertex2f(drawnewx1, drawnewy1)
        glEnd()






def draw_play():

    findZone(-20, 230, -20, 250, 1.0,1.0,0.0)
    findZone(-20, 230, 20, 240, 1.0, 1.0, 0.0)
    findZone(-20, 250, 20, 240, 1.0, 1.0, 0.0)
    

def draw_pause():
   
    findZone(-10, 230, -10, 250, 1.0, 1.0, 0.0)
    findZone(10, 230, 10, 250, 1.0, 1.0, 0.0)


def backButton():
    
       findZone(-250, 240, -240, 250, 0.0, 1.0, 1.0)
       findZone(-250, 240, -230, 240, 0.0, 1.0, 1.0)  # line2

       findZone(-240, 230, -250, 240, 0.0, 1.0, 1.0)

def shooting_collisions():
    global bubble_score,projectiles,bubbles
    for i in projectiles:
        project_x=i["x"]-10
        project_y=i["y"]
        radius_projectile=i['radius']
        for j in bubbles:
            bubble_x=j["x"]
            bubble_y=j["y"]
            radius_bubble=j['rad']
            distance= math.sqrt((project_x-bubble_x)**2+(project_y-bubble_y)**2)
            radius_sum=radius_projectile+radius_bubble
            if (distance<=radius_sum):
                bubble_score+=1
                bubbles.remove(j)
                projectiles.remove(i)
                print("Score:",bubble_score)
            


                 
            

def checkingRecieverCollisions():
    #checing falling bbuble clash with reciever
    global reciever_radius,reciever_center,reciever_center_y,game_over,bubble_score,pause
    for j in bubbles:
            bubble_x=j["x"]
            bubble_y=j["y"]
            radius_bubble=j['rad']
            distance= math.sqrt((reciever_center-bubble_x)**2+(reciever_center_y-bubble_y)**2)
            radius_sum=reciever_radius+radius_bubble
            # print(bubble_x,bubble_y)
            if (distance<=radius_sum):
                print("Game Over!")
                print("Score:",bubble_score)
                game_over=True
                pause=True


def checkingBubbleScreen():
    #checking buble went out of screen
    global missed,game_over,bubble_score,pause
    for j in bubbles:
            bubble_x=j["x"]
            bubble_y=j["y"]
            # print(bubble_y)
            if (bubble_y<=-240):
                
                bubbles.remove(j)
                missed+=1
                # print(missed)
                if(missed ==3 ):
                    game_over = True
                    pause=True
                    print("Game over!")
                    print("Score:",bubble_score)
                



def projectileOutOfScreen():
    global projectiles,projectile_missed,game_over,bubble_score,pause
    for i in projectiles:
        if (i['y']>250):
             projectiles.remove(i)
             projectile_missed+=1
            #  print(projectile_missed)
             if (projectile_missed==3):
                 game_over=True
                 pause=True

                 print("Game Over")
                 print("Score:",bubble_score)
    
def animate():
    global t, bubbles,game_over,pause

    if(pause==False):
        if(game_over==False):
                t += 0.01
                if t >= 5:
                    t = 0
                    
                    rand_x = random.randint(-235, 235)
                    rad=random.randint(10,20)
                    bubbles.append({'x': rand_x, 'y': 200,"rad":rad})
                
                


                for bubble in bubbles:
                    bubble['y'] -= speed

                

                for projectile in projectiles:
                    
                    projectile['y'] += 1 

                shooting_collisions()
                checkingRecieverCollisions()
                checkingBubbleScreen()
                projectileOutOfScreen()
                

                    
                glutPostRedisplay()
    



def drawProjectiles():
    for projectile in projectiles:
        x = projectile['x']
        y = projectile['y']
        radius = projectile['radius']
        drawcircle2(x, y, radius, 0.0, 1.0, 0.0)

def draw_bubbles():
    global bubbles
    for bubble in bubbles:
        x = bubble['x']
        y = bubble['y']
        rad=bubble['rad']
        drawcircle2(x, y, rad, 1.0, 1.0, 0.0)


def plot_circle_points(x_axis_center, y_axis_center, x, y, red,green,blue):
    
    global move,project_pos,reciever_center,reciever_center_y
    project_pos=x+move
    reciever_center=x+move
    reciever_center_y=y_axis_center+y
    
    glPointSize(2)
    glBegin(GL_POINTS)
    glColor3f(red, green, blue)
    
    #zone - 1
    glVertex2f(+x+move, y_axis_center + y)
    #zone - 2 
    glVertex2f(-x+move, y_axis_center + y) 
    #zone - 6
    glVertex2f(+x+move, y_axis_center - y) 
    #zone - 5
    glVertex2f(-x+move, y_axis_center - y) 
    #zone - 0
    glVertex2f(+y+move, y_axis_center + x) 
    #zone - 3
    glVertex2f(-y+move, y_axis_center + x) 
    #zone - 7
    glVertex2f(+y+move, y_axis_center -  x) 
    #zone - 4
    glVertex2f(-y+move, y_axis_center - x) 
    glEnd()

def plot_circle_points2(x_axis_center, y_axis_center, x, y, red,green,blue):
    
    glPointSize(2)
    glBegin(GL_POINTS)
    glColor3f(red, green, blue)
    glVertex2f(x_axis_center + x, y_axis_center + y)
    glVertex2f(x_axis_center - x, y_axis_center + y)
    glVertex2f(x_axis_center + x, y_axis_center - y)
    glVertex2f(x_axis_center - x, y_axis_center - y)
    glVertex2f(x_axis_center + y, y_axis_center + x)
    glVertex2f(x_axis_center - y, y_axis_center + x)
    glVertex2f(x_axis_center + y, y_axis_center - x)
    glVertex2f(x_axis_center - y, y_axis_center - x)
    glEnd()

def drawcircle(x_axis_center, y_axis_center, radius, red,green,blue, x):
    global reciever_radius
    reciever_radius=radius

    y = radius
    d = 1 - radius
    plot_circle_points(x_axis_center, y_axis_center, x, y, red,green,blue)
   
    while x < y:
        if d < 0:
            d += 2*x + 3
            x += 1
        else:
            d += 2*x - 2*y+ 5
            y -= 1
            x += 1
       

        plot_circle_points(x_axis_center, y_axis_center, x, y, red,green,blue)


def drawcircle2(x_axis_center, y_axis_center, radius, red,green,blue):
    x = 0
    y = radius
    d = 1 - radius
    plot_circle_points2(x_axis_center, y_axis_center, x, y, red,green,blue)
    while x < y:
        if d < 0:
            d += 2 * x + 3
            x += 1
        else:
            d += 2*x - 2*y + 5
            y -= 1
            x += 1
        
        plot_circle_points2(x_axis_center, y_axis_center, x, y, red,green,blue)

def shooter():

    drawcircle(0, global_y_position_reciever, 15, 1.0, 0.0, 0.0, 0)


def cross():
    



    findZone(220, 230, 250, 250, 1.0, 0.0, 0.0)
    findZone(220, 250, 250, 230, 1.0, 0.0, 0.0)

   
def display():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 0, 0, 0);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    glMatrixMode(GL_MODELVIEW)

    cross()
   
    backButton()
    shooter()



        
    if(pause):
        draw_play()
    else:

        draw_pause()

       
       
   
    if(game_over):
        pass
    else:
        draw_bubbles()
        drawProjectiles()
 
    glutSwapBuffers()


def init():

    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    gluPerspective(104, 1 , 1, 1000.0)
def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y
    return a,b







def mouseListener(button, state, x, y):
        global pause,game_over,speed,bubble_score,projectiles,bubbles


        if button == GLUT_LEFT_BUTTON:
            if (state == GLUT_DOWN):
                c_X, c_y = convert_coordinate(x, y)
                click_x = c_X
                click_y = c_y
                # print(click_x,click_y,"clicked")

                if((click_x<25.0 and click_x>-25.0) and (click_y<400.0 and click_y>360.0)):
                    if (game_over == False):
                        pause=not pause
                elif ((click_x < 250.0 and click_x > 208.0) and (click_y < 400.0 and click_y > 360.0)):
                    print("GoodBye! Score:",bubble_score)
                    speed=1
                    glutLeaveMainLoop()
                elif ((click_x > -250.0 and click_x < -220.0) and (click_y < 400.0 and click_y > 360.0)):
                    print("Starting Over!")
                    bubble_score=0
                    projectiles=[]
                    bubbles=[]
                   
                    game_over=False
                     #so that tings doesnt reamin pause
                    pause=False
                   
                    speed=0.1






                    # glutPostRedisplay()
def keyboardListener(key, x, y):
    global move,projectiles,project_pos
    if pause:
        return
    if not game_over:
        if key == b'a':
            
            if move > -230:  
                move -= 10
               
        elif key == b'd':
            
            if move < 230:  
                move += 10

        elif key == b' ':
            
            y = global_y_position_reciever + 15
            projectiles.append({'x': project_pos-10, 'y': y, 'radius': 5})
                
            
        glutPostRedisplay()



glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
wind = glutCreateWindow(b"assignment-3")
init()

glutIdleFunc(animate)
glutDisplayFunc(display)
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouseListener)
glutMainLoop()
