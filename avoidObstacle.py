#To use this file, all you have to do is import this file in PythonWin.
"""Here are the full instructions actually:
1) Turn on the robot
2) Plug the robot USB into your laptop
3) Run PythonWin
4) Press CTRL + i
5) Choose this file

And everything should work automatically
"""
import time
import create
import math
r = create.Create(3)

#This part has the robot move towards an obstacle, hit it with its bumper sensors then retrieve the position. Then it turns around and goes back to the starting position.
#It moves toward the obstacle again but this time not touching it, but only nearing it.
#Once nearing it, it will go around the object.
def moveFunc():
    r.turn(90,45)
    r.move(30)
    r.turn(-90)  #Values here may need to be edited for accuracy.
    r.move(90)
    r.turn(-90)
    r.move(30)
    r.turn(90,45)
    r.move(30)
    
def scanner():  
    sensors = r.sensors([create.LEFT_BUMP, create.RIGHT_BUMP])
    start = r.getPose()#This is its starting place
    while sensors[create.LEFT_BUMP] == 0 and sensors[create.RIGHT_BUMP] == 0:  #It keeps going till its bumper sensors are touched"""
        sensors = r.sensors([create.LEFT_BUMP, create.RIGHT_BUMP])
        r.go(10,0)
    else:
        if sensors[create.LEFT_BUMP] == 1 and sensors[create.RIGHT_BUMP] == 0: #There are cases for every sensor possiblity, (left,right, both)"""
                r.playSong( [ (65,16),(69,16) ] )
                Obstacle = r.getPose() #Position of the obstacle
                difference = math.fabs(Obstacle[0] - start[0])  #Absolute value of the difference of the X positions
                r.turn(180,45)   #Once obstacle position is taken, go back to starting position
                time.sleep(0.3)
                r.move(difference,30)
                r.turn(180,45)
                r.move(difference-10,30) #Now move towards obstacle again but come close and not hit it
                moveFunc()  #This little function tells it what to do after coming close to an object but not hitting it.
        if sensors[create.LEFT_BUMP] == 0 and sensors[create.RIGHT_BUMP] == 1:
                r.playSong( [ (71,24),(65,16) ] )
                Obstacle = r.getPose()
                difference = math.fabs(Obstacle[0] - start[0])
                r.turn(180,45)
                time.sleep(0.3)
                r.move(difference,30)
                r.turn(180,45)
                r.move(difference-10,30)
                moveFunc()
        if sensors[create.LEFT_BUMP] == 1 and sensors[create.RIGHT_BUMP] == 1:
                r.playSong( [ (69,16),(71,24) ] )
                Obstacle = r.getPose()
                difference = math.fabs(Obstacle[0] - start[0])
                r.turn(180,45)
                time.sleep(0.3)
                r.move(difference,30)
                r.turn(180,45)
                r.move(difference-10,30)
                moveFunc()
