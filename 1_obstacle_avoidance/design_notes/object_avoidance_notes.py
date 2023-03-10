#!/usr/bin/env python

# Libraries

# Grove - Ultrasonic sensor
from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       # use python 3 syntax but make it compatible with python 2

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers





# Q1. When to perform unit conversion?
# A1. Maybe later to avoid converting over and over.

def get_distance(port, units) {

    BP = brickpi3.BrickPi3()    # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
    BP.set_sensor_type("BP.PORT_"+port, BP.SENSOR_TYPE.NXT_ULTRASONIC)
    distance_to_nearest_obstacle = BP.get_sensor("BP.PORT_"+port)
    BP.reset_all()              # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.
    return distance_to_nearest_obstacle
}

def is_too_close(distance_to_nearest_obstacle, limit, units) {

    if (distance_to_nearest_obstacle <= limit) {
        return true
    }

    else {return false}
}


def move_forward(travel_distance) {
    #function needed to calculate rotations -> distance
    #

}

def move_turn() {
    # turn 90 deg
        # function needed to alternate turning direction
        # parameter needed to specify sweep direction (e.g left, right)
    # move forward a distance equal to the width of the rover
    # turn another 90 deg in the same direction as the first 90 deg turn
}


int main() {
    #original
    # loop
        # get distance
        # evaluate against limit
            # 1. greater than limit - keep going
            # 2. at or lower than limit


    #new
    # get distance
    # evaluate against limit
        # greater than limit - travel distance d = input - 5in
            # calculate distance d
            # run motors for the time needed to travel distance d
            # turn 90 degrees
                # return to start of loop



    get_distance





    #timer
    do {

        if(!is_too_close(get_distance(16), 5, cm)) {
            move_forward(get_distance(16), 5, cm)
            move_turn()
        }


    } while (time < 15min)


}














    try:
        while True:
            # read and display the sensor value
            # BP.get_sensor retrieves a sensor value.
            # BP.PORT_1 specifies that we are looking for the value of sensor port 1.
            # BP.get_sensor returns the sensor value (what we want to display).
            try:
                value = BP.get_sensor(BP.PORT_16)
                print(value)                         # print the distance in CM
            except brickpi3.SensorError as error:
                print(error)
            
            time.sleep(0.02)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        BP.reset_all()        # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.





    try:
        while True:
            # read and display the sensor value
            # BP.get_sensor retrieves a sensor value.
            # BP.PORT_1 specifies that we are looking for the value of sensor port 1.
            # BP.get_sensor returns the sensor value (what we want to display).
            try:
                value = BP.get_sensor(BP.PORT_16)
                print(value)                         # print the distance in CM
            except brickpi3.SensorError as error:
                print(error)
            
            time.sleep(0.02)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        BP.reset_all()        # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.



}

