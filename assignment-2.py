from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

drawx1=0
drawy1=0
drawx2=0
drawy2=0
red1=0
green1=0
blue1=0

#diamond color
gred=0.0
ggreen=1.0
gblue=0.0
W_Width, W_Height = 500,800
zone=0
pause=False
diamond_peak=0
diamond_x=0
diamond_new_x=0
box_w1=-100
box_w2=100
pos=0

diamond_height = 40
diamond_width = 15
catcher_top = -220
catcher_bottom = -230
catcher_left = box_w1
catcher_right = box_w2
points=0
game_over=False

#catcher color
catch_red=1.0
catch_green=1.0
catch_blue=1.0

speed=1


def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y
    return a,b
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
    # print("got points")
    # drawing first line
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
    # print(drawx1,drawy1,drawx2,drawy2,"after shifting")
    # print(dx,dy,dinit,dNE,dE)

    # finding req pixewls
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
    # print(zone,"zone")



    # glPointSize(5)
    # glBegin(GL_POINTS)
    # glColor3f(0, 1.0, 0.0)
    # glVertex2f(x1,y1)
    # glEnd()


def drawDiamond():
    global diamond_peak,gred,ggreen,gblue,diamond_new_x,game_over
    if(gred==0.0 and ggreen==0.0 and gblue==0.0):
        gred=1.0
        ggreen=1.0
        gblue=0.0
    if(game_over==True):#make black when game over
        gred = 0.0
        ggreen = 0.0
        gblue = 0.0


    diamond_new_x=0+diamond_x

    findZone(0+diamond_x, 220+diamond_peak, -15+diamond_x, 200+diamond_peak, gred,ggreen,gblue)
    findZone(15+diamond_x, 200+diamond_peak,0+diamond_x, 220+diamond_peak,  gred,ggreen,gblue)
    findZone(0+diamond_x, 180+diamond_peak,-15+diamond_x, 200+diamond_peak,  gred,ggreen,gblue)
    findZone(0+diamond_x, 180+diamond_peak, 15+diamond_x, 200+diamond_peak, gred,ggreen,gblue)

def draw_play():

    findZone(-20, 230, -20, 250, 1.0,1.0,0.0)
    findZone(-20, 230, 20, 240, 1.0, 1.0, 0.0)
    findZone(-20, 250, 20, 240, 1.0, 1.0, 0.0)
    # findZone(15, 200,0, 220, 0.0,1,1)
    # findZone(0, 180,-15, 200,  0.0,1,1)

def draw_catcher():
    global box_w1,box_w2,pos,catch_red,catch_green,catch_blue
    findZone( box_w1+pos,-220, box_w2+pos, -220, catch_red,catch_green,catch_blue)#top
    findZone(-80+pos, -230, 80+pos, -230, catch_red,catch_green,catch_blue)#bottom
    findZone(-100+pos, -220, -80+pos, -230, catch_red,catch_green,catch_blue)#left
    findZone( 100+pos, -220, 80+pos,-230,catch_red,catch_green,catch_blue)  # right
def draw_pause():
     # pause
    findZone(-10, 230, -10, 250, 1.0, 1.0, 0.0)
    findZone(10, 230, 10, 250, 1.0, 1.0, 0.0)

def mouseListener(button, state, x, y):
        global pause,game_over,points,diamond_peak,catch_red,catch_green,catch_blue,speed


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
                    print("GoodBye! Score",points)
                    speed=1
                    glutLeaveMainLoop()
                elif ((click_x > -250.0 and click_x < -220.0) and (click_y < 400.0 and click_y > 360.0)):
                    print("Starting Over!")
                    points=0
                    diamond_peak = 0 #diamond starting from top
                    game_over=False #so that tings doesnt reamin pause
                    # making catcher white color as restarting
                    catch_red = 1.0
                    catch_green = 1.0
                    catch_blue = 1.0
                    speed=1






                    # glutPostRedisplay()




def display():

    #//clear the display

       glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
       glClearColor(0, 0, 0, 0);  # //color black
       glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
       # //load the correct matrix -- MODEL-VIEW matrix
       glMatrixMode(GL_MODELVIEW)
       # //initialize the matrix
       glLoadIdentity()
      
       gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
       glMatrixMode(GL_MODELVIEW)
       #
      

       # cross
       findZone(220, 230, 250, 250, 1.0, 0.0, 0.0)
       findZone(220, 250, 250, 230, 1.0, 0.0, 0.0)

       # back

       findZone(-250, 240, -240, 250, 0.0, 1.0, 1.0)
       findZone(-250, 240, -230, 240, 0.0, 1.0, 1.0)  # line2

       findZone(-240, 230, -250, 240, 0.0, 1.0, 1.0)

       # findZone(-250, 240,-240, 230, 0.0, 1.0, 1.0)# wierd

       # diamond

       drawDiamond()
       if(pause):
          draw_play()
       else:

          draw_pause()

       # draw catcher
       draw_catcher()


       glutSwapBuffers()




def animate():
    global diamond_peak, gred, ggreen, gblue, diamond_x, diamond_width, diamond_height, points,pause,catcher_left,catcher_right,game_over,catch_red,catch_green,catch_blue,speed

    if(pause==False):
        if(game_over==False):

            red = random.choice([0, 1])
            green = random.choice([0, 1])
            blue = random.choice([0, 1])

            diamond_left = diamond_x - diamond_width / 2
            diamond_right = diamond_x + diamond_width / 2
            diamond_top = diamond_peak + 220
            diamond_bottom = diamond_peak + 180
            catcher_left=-100+pos
            catcher_right=100+pos

            if (diamond_peak < -450):
                diamond_peak = 0
                # gred = red
                # ggreen = green
                # gblue = blue
                # diamond_x = random.randrange(-240, 240)
                print("Game Over! Score: ",points)
                points=0
                # pause=True
                game_over=True
                #making catcher red
                catch_red=1.0
                catch_green=0.0
                catch_blue=0.0

                speed=1


                #making diamond black








            elif (diamond_left < catcher_right and
                  diamond_right > catcher_left and
                  diamond_bottom < catcher_top and
                  diamond_top > catcher_bottom):

                points += 1
                print("Score:", points)
                diamond_peak = 0
                speed+=0.2

                gred = red
                ggreen = green
                gblue = blue
                diamond_x = random.randrange(-240, 240)
            else:
                diamond_peak -= speed

            # diamond_peak-=1
            glutPostRedisplay()
def move(key, x, y):
    global pos
    if(pause==False  ):
        if (game_over==False):

            if key == GLUT_KEY_LEFT:
                # print("left")
                if (pos - 100 <= -250):
                    return

                pos -= 10

            if key == GLUT_KEY_RIGHT:
                # print("roght")
                if (pos + 100 >= 250):
                    return
                pos += 10

            glutPostRedisplay()




def init():
    #//clear the screen
    glClearColor(1,1,1,1)
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
glutInitWindowSize(500,800)

glutInitWindowPosition(0,0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"assignment-2")
init()

glutDisplayFunc(display)
glutMouseFunc(mouseListener)
glutIdleFunc(animate)
glutSpecialFunc(move)


glutMainLoop()