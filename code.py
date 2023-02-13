# This project is my attempt at building a simple, cheap, and super cool retro style display!
# I wanted to copy the Tidbyt displays (which I think are awesome and totally worth the price), but I wanted to see how
# cheap I could make it.
#
# It is designed for a Raspberry Pi Pico W, which means it is bare-boned by necessity. The pico doesn't have much space
# for fancy libraries or anything, so I had to do several things the hard way.


import time
import board
import displayio
import framebufferio

from displayManager import DisplayManager
from analytics import YouTubeAnalytics

from rgbmatrix import RGBMatrix

bit_depth_value = 1
base_width = 64
base_height = 32
chain_across = 1
tile_down = 1
serpentine_value = True

width_value = base_width * chain_across
height_value = base_height * tile_down

displayio.release_displays()

matrix = RGBMatrix(
    width=width_value, height=height_value, bit_depth=bit_depth_value,
    rgb_pins=[board.GP2, board.GP3, board.GP4, board.GP5, board.GP8, board.GP9],
    addr_pins=[board.GP10, board.GP16, board.GP18, board.GP20],
    clock_pin=board.GP11, latch_pin=board.GP12, output_enable_pin=board.GP13,
    tile=tile_down, serpentine=serpentine_value,
    doublebuffer=True,
)

# Associate the RGB matrix with a Display so that we can use displayio features
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=True)

display_system = DisplayManager(display)
youtubeAnalytics = YouTubeAnalytics()

display_system.display_logo()

# Update every 10 minutes (let's be honest I don't get that many new subs...)
recheck_delay = 600
last_recheck = 0

while True:
    if time.time() - last_recheck > recheck_delay:
        # Blocking call which returns when the get_analytics() http request is done
        # Tried async, but not enough room on pico
        sub_count = youtubeAnalytics.get_analytics()
        display_system.update_sub_count(sub_count)
        last_recheck = time.time()

    display_system.update()
