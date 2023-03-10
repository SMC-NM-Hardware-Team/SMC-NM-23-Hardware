#!/usr/bin/env python

'''BrickPi dependencies'''
from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers
'''BrickPi dependencies'''

BP = brickpi3.BrickPi3()
BP.reset_all()