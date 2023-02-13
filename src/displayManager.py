from math import floor, log

import adafruit_imageload
import terminalio
import displayio
import adafruit_display_text.label
from adafruit_display_text.scrolling_label import ScrollingLabel


def get_logo(x, y):
    logo_bitmap, logo_palette = adafruit_imageload.load("/modHobbyist.bmp",
                                                        bitmap=displayio.Bitmap,
                                                        palette=displayio.Palette)
    logo_palette[1] = 0x0000FF
    logo_palette.make_transparent(0)

    return displayio.TileGrid(logo_bitmap, pixel_shader=logo_palette, x=x, y=y)


def get_youtube_logo(x, y):
    youtube_bitmap, youtube_palette = adafruit_imageload.load("/youtube.bmp",
                                                              bitmap=displayio.Bitmap,
                                                              palette=displayio.Palette)
    youtube_palette.make_transparent(0)

    return displayio.TileGrid(youtube_bitmap, pixel_shader=youtube_palette, x=x, y=y)


def convert_subs_to_text(sub_count):
    # if sub_count % 1000 > 0:
    # TODO make this programmatic\
    units = ['', 'K', 'M']
    k = 1000.0
    magnitude = int(floor(log(int(sub_count), k)))

    if int(sub_count) / k ** magnitude >= 100:
        return '%.0f%s' % (int(sub_count) / k ** magnitude, units[magnitude])

    if int(sub_count) / k ** magnitude >= 10:
        return '%.1f%s' % (int(sub_count) / k ** magnitude, units[magnitude])

    return '%.2f%s' % (int(sub_count) / k ** magnitude, units[magnitude])


class DisplayManager(displayio.Group):
    def __init__(self, display):
        super().__init__()
        display.rotation = 0
        self.display = display
        self._first_enter_page = True
        self._scrolling_label = ScrollingLabel(terminalio.FONT, text="subscribers", max_characters=11, animate_time=0.3,
                                               color=0x00FFFF)

        self._scrolling_label.x = 0
        self._scrolling_label.y = 25
        line1 = adafruit_display_text.label.Label(terminalio.FONT, color=0x0000CC)

        self._line1 = line1
        self._line1.text = " "

        self._line_group = displayio.Group()
        self._line_group.append(self)
        self.append(self._line1)
        self.append(self._scrolling_label)
        display.show(self._line_group)

    def update(self):
        self._scrolling_label.update()

    def update_sub_count(self, sub_count):
        self._line1.text = convert_subs_to_text(sub_count)

    def display_logo(self):
        tile_grid = get_logo(1, 2)
        youtube_tile_grid = get_youtube_logo(51, 9)
        group = displayio.Group()

        # TODO center this using the width attribute
        self._line1.x = 19
        self._line1.y = 12

        group.append(tile_grid)
        group.append(youtube_tile_grid)

        self._line_group.append(group)

        self.display.show(self._line_group)
