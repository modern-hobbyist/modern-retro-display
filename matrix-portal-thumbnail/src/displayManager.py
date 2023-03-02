from math import floor, log

import adafruit_imageload
import displayio
import adafruit_display_text.label
from adafruit_bitmap_font import bitmap_font

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

        medium_font = bitmap_font.load_font("fonts/spleen-6x12.bdf")

        self.display = display
        self._first_enter_page = True

        line1 = adafruit_display_text.label.Label(medium_font, color=0x0099cc)
        line2 = adafruit_display_text.label.Label(medium_font, color=0x0000CC)
        line3 = adafruit_display_text.label.Label(medium_font, color=0x0099cc)

        self._line1 = line1
        self._line1.text = "DIY"

        self._line2 = line2
        self._line2.text = "Tidbyt"

        self._line3 = line3
        self._line3.text = "Display"

        self._line_group = displayio.Group()
        self._line_group.append(self)
        self.append(self._line1)
        self.append(self._line2)
        self.append(self._line3)
        display.show(self._line_group)

    def display_logo(self):
        tile_grid = get_logo(0, 1)
        youtube_tile_grid = get_youtube_logo(3, 22)
        group = displayio.Group()

        # TODO center this using the width attribute
        self._line1.x = 30
        self._line1.y = 5

        self._line2.x = 22
        self._line2.y = 14

        self._line3.x = 18
        self._line3.y = 24

        group.append(tile_grid)
        group.append(youtube_tile_grid)

        self._line_group.append(group)

        self.display.show(self._line_group)
