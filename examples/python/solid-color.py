#!/usr/bin/env python

# Open Pixel Control client: All lights to solid white

import opc, time
import sys

numLEDs = 512
client = opc.Client('localhost:7890')

black = [ (0,0,0) ] * numLEDs

if len(sys.argv) == 2:
    c = int(sys.argv[1], 16)
    color = (c >> 16, (c >> 8) & 0xff, c & 0xff)
elif len(sys.argv) == 4:
    color = tuple(int(x, 0) for x in sys.argv[1:4])
else:
    color = (255, 255, 255)

color_arr = [color] * numLEDs

# Fade to white
client.put_pixels(black)
client.put_pixels(black)
time.sleep(0.25)
client.put_pixels(color_arr)
