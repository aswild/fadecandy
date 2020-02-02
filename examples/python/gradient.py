#!/usr/bin/env python

import opc
import random
import sys
import time

from gradient_data import *
GRADIENT = GRADIENT_RED

if len(sys.argv) > 1:
    arg = sys.argv[1].lower()
    if arg == 'red':
        GRADIENT = GRADIENT_RED
    elif arg == 'blue':
        GRADIENT = GRADIENT_BLUE
    elif arg == 'rainbow' or arg == 'rain':
        GRADIENT = GRADIENT_RAINBOW
    else:
        sys.exit('invalid parameter')

N_LED = 128
STEP_TIME = 0.005
N_STEPS   = 250

pixels = [0]*N_LED

client = opc.Client('localhost:7890')
client.set_interpolation(False)
client.put_pixels(pixels)
time.sleep(STEP_TIME)

try:
    cstart = [random.randint(0, len(GRADIENT)-1) for _ in range(N_LED)]
    while True:
        cstop  = [random.randint(0, len(GRADIENT)-1) for _ in range(N_LED)]
        for step in range(N_STEPS):
            for i in range(N_LED):
                gc = cstart[i] + ((step * (cstop[i] - cstart[i])) // (N_STEPS-1))
                pixels[i] = GRADIENT[gc]
            client.put_pixels(pixels)
            time.sleep(STEP_TIME)
        cstart = cstop
except KeyboardInterrupt:
    client.put_pixels([0]*N_LED)
