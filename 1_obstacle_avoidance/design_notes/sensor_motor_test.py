from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''

import sys
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
import time
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
#speed = 0
#adder = 1
#sonar = GroveUltrasonicRanger(5)
#sonar_left = GroveUltrasonicRanger(18)
#print(sonar_right.get_distance())


#BP.set_motor_power(BP.PORT_B + BP.PORT_C + BP.PORT_D, 100)
#BP.set_motor_position(BP.PORT_C, 720)
while True:
    #print('{} cm'.format(int(sonar_left.get_distance())))

    #print("Battery voltage: %6.3f  9v voltage: %6.3f  5v voltage: %6.3f  3.3v voltage: %6.3f" % (BP.get_voltage_battery(), BP.get_voltage_9v(), BP.get_voltage_5v(), BP.get_voltage_3v3())) # read and display the current voltages
    
    BP.set_motor_power(BP.PORT_A, 50)
  #  BP.set_motor_power(BP.PORT_C, speedB)
  #  BP.set_motor_power(BP.PORT_B, speedC)

  #  if int(sonar_right.get_distance()) < 25:
     #   speedB -= 10
     #   speedA = 0
        # if the touch sensor is pressed
    
    
    
    if KeyboardInterrupt:
        BP.reset_all() 
    
        #BP.set_motor_power(BP.PORT_B + BP.PORT_C, 100)
    # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.

#except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
#    BP.reset_all()        # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.
