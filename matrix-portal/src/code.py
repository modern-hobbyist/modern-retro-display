# TODO add a disclaimer or a description of this project here

import time
import board
import displayio
import framebufferio

from displayManager import DisplayManager
from analytics import YouTubeAnalytics

from rgbmatrix import RGBMatrix

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

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
    width=64, bit_depth=4,
    rgb_pins=[
        board.MTX_R1,
        board.MTX_G1,
        board.MTX_B1,
        board.MTX_R2,
        board.MTX_G2,
        board.MTX_B2
    ],
    addr_pins=[
        board.MTX_ADDRA,
        board.MTX_ADDRB,
        board.MTX_ADDRC,
        board.MTX_ADDRD
    ],
    clock_pin=board.MTX_CLK,
    latch_pin=board.MTX_LAT,
    output_enable_pin=board.MTX_OE
)

# Associate the RGB matrix with a Display so that we can use displayio features
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=True)

display_system = DisplayManager(display)
youtubeAnalytics = YouTubeAnalytics(board, secrets)

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
