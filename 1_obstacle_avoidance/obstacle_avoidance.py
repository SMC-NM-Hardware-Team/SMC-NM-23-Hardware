#!/usr/bin/env python

'''BrickPi dependencies'''
from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers
'''BrickPi dependencies'''


'''Grove Base Hat dependencies'''
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
'''Grove Base Hat dependencies'''

def convert_cm_to_in(cm):
    return cm*0.393701

def test_ultrasonic_sensor():
    # from grove.helper import SlotHelper
    # sh = SlotHelper(SlotHelper.GPIO)
    #pin = 5 #sh.argv2pin()

    mounted = GroveUltrasonicRanger(5)
    #hanging = GroveUltrasonicRanger(16)

    print('Detecting distance...')
    while True:
        print('mounted: {}'.format(convert_cm_to_in(mounted.get_distance())))# + ' , hanging: {}'.format(convert_cm_to_in(hanging.get_distance())))
        time.sleep(0.25)



def get_dist():
    mounted = GroveUltrasonicRanger(5)
    return convert_cm_to_in(mounted.get_distance())


def there_is_space_to_move(dist, min_dist):
    if dist > min_dist:
        return True
    else:
        return False





def brickpi_initialize_motors():
    BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.










def get_total_forward_distance():
    something = 0       #placeholder
    #return distance    # code for getting the distance from the sensors





def calculate_forward_clearance(limit):
    something = 0       #placeholder
    # distance =  # /* code for getting the distance from the sensors */
    # return distance-limit

def move_forward():
    something = 0       #placeholder
    #/* v(motor power in %) = length of 1 rev of treads/time to complete one revolution at power % */
    #// start a table of values

def turn_left_90():
    something = 0       #placeholder
    #// rover motors move in opposite directions
    #// right -> forward
    #// left -> reverse


def turn_right_90():
    something = 0       #placeholder
    #// rover motors move in opposite directions
    #// right -> reverse
    #// left -> forward


def move_turn(left_or_right):
    #// Needs a more elegant solution, but a working solution comes first.


    #// turn 90 degrees
        #// but which direction? It must be specified.
    width_of_rover = 40    #// cm
    if left_or_right == "left":
        turn_left_90()
        if get_total_forward_distance() >= width_of_rover:
            move_forward(width_of_rover)
            turn_left_90()
        else:
            turn_left_90()
    else:
        turn_right_90()
        if get_total_forward_distance() >= width_of_rover:
            move_forward(width_of_rover)
            turn_right_90()
        else:
            turn_right_90()




# # Begin Main Body
# t = 1000;                                            #// time in s
# room_sweep_direction = "left"                    #// "left" or "right"        // quotes are needed
# minimum_allowable_distance_from_obstacle = 20       #// distance in cm

# while (t > 0):
#     if get_total_forward_distance() > minimum_allowable_distance_from_obstacle:
#         move_forward(get_total_forward_distance() - minimum_allowable_distance_from_obstacle)
#     else:
#         move_turn(room_sweep_direction)


turn_direction = "right"
BP = brickpi3.BrickPi3()
BP.reset_all()
print("Motors reset")
#BP.reset_motor_encoder(BP.PORT_A) # reset encoder A
#BP.reset_motor_encoder(BP.PORT_D)
##print(BP.get_motor_encoder(BP.PORT_A))
#while True:
#    if (there_is_space_to_move(get_dist(), 5)):
#        BP.set_motor_dps(BP.PORT_A, -50)
#        BP.set_motor_dps(BP.PORT_D, -50)
#        print("Motor dpses set to 50")
#        time.sleep(0.25)
#    else:
#        BP.set_motor_dps(BP.PORT_A, 0)
#        BP.set_motor_dps(BP.PORT_D, 0)
#        print("Motor dpses set to zero")
#        time.sleep(5)
#        print("Turning...")

def turn_90(turn_direction):
    subtimer = 2
    while subtimer >= 0:
        if turn_direction == "right":
            BP.set_motor_dps(BP.PORT_A, -177)
            BP.set_motor_dps(BP.PORT_D, 177)
        else:
            BP.set_motor_dps(BP.PORT_A, 177)
            BP.set_motor_dps(BP.PORT_D, -177)
        print(subtimer)
        time.sleep(1)
        subtimer-=1
        
        
timer = 60
while timer >= 0:
    if (there_is_space_to_move(get_dist(), 10)):
        BP.set_motor_dps(BP.PORT_A, -250)
        BP.set_motor_dps(BP.PORT_D, -250)
    else:
        turn_90(turn_direction)
            
        subtimer = 5
        while subtimer >= 0:
            if (there_is_space_to_move(get_dist(), 10)):
                BP.set_motor_dps(BP.PORT_A, -250)
                BP.set_motor_dps(BP.PORT_D, -250)
            print(subtimer)
            time.sleep(1)
            subtimer-=1
            
        turn_90(turn_direction)
            
            
    print(timer)
    time.sleep(1)
    timer-=1
            
        
            
BP.reset_all()

#BP.set_motor_dps(BP.PORT_A, 0)
#BP.set_motor_dps(BP.PORT_D, 0)
#print("Motor dpses set to zero")
#BP.reset_all()
#print("Motors reset")
#while there_is_space_to_move(get_dist(), 5):
    #move_forward()
    # brickpi motor code here

#BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
#
##counter = 10
##while counter >=0:
###while True:
###    BP.offset_motor_encoder(BP.PORT_A, BP.get_motor_encoder(BP.PORT_A)) # reset encoder A
###    BP.offset_motor_encoder(BP.PORT_D, BP.get_motor_encoder(BP.PORT_D)) # reset encoder A
###    BP.set_motor_dps(BP.PORT_A, 50)
###    BP.set_motor_dps(BP.PORT_D, 50)
###    BP.set_motor_power(BP.PORT_A, 50)
###    BP.set_motor_power(BP.PORT_D, 50)
##    counter-=counter
##    print(counter)
#BP.reset_all()

