#!/usr/bin/env python

# Open Pixel Control version of the "measuring_stick" Arduino sketch:
# For each group of 64 LEDs (one strip), lights all LEDs with every
# multiple of 10 lit green.

import opc, time

numStrings = 8
client = opc.Client('localhost:7890')

string = [0x00ff00 if (i+1)%10 == 0 else 0x7f7f7f for i in range(64)]

# Immediately display new frame
pixels = string * numStrings
client.put_pixels(pixels)
client.put_pixels(pixels)
