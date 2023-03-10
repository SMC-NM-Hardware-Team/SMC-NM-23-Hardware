#!/usr/bin/env python


'''From /OEM Starter Code/BrickPi/BrickPi3 (Dexter Repo)/Software/Python/Examples/NXT-Ultrasonic_Sensor.py'''
from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers
'''From /OEM Starter Code/BrickPi/BrickPi3 (Dexter Repo)/Software/Python/Examples/NXT-Ultrasonic_Sensor.py'''











def get_total_forward_distance():
    something = 0       #placeholder
    #return distance    # code for getting the distance from the sensors


def there_is_space_to_move(distance, limit):
    if distance > limit: # in cm
        return True
    else:
        return False


def calculate_forward_clearance(limit):
    something = 0       #placeholder
    # distance =  # /* code for getting the distance from the sensors */
    # return distance-limit

def move_forward(distance):
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




# Begin Main Body
t = 1000;                                            #// time in s
room_sweep_direction = "left"                    #// "left" or "right"        // quotes are needed
minimum_allowable_distance_from_obstacle = 20       #// distance in cm

while (t > 0):
    if get_total_forward_distance() > minimum_allowable_distance_from_obstacle:
        move_forward(get_total_forward_distance() - minimum_allowable_distance_from_obstacle)
    else:
        move_turn(room_sweep_direction)

