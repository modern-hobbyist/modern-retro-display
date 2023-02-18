import gc
import busio
from digitalio import DigitalInOut
import adafruit_requests as requests
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from adafruit_esp32spi import adafruit_esp32spi


class YouTubeAnalytics:
    def __init__(self, board, secrets) -> None:
        # TODO don't commit this, it's secret...
        self._wifi_ssid = secrets['ssid']
        self._wifi_pass = secrets['password']
        self._yt_key = secrets['youtube_token']
        self._yt_channel_id = secrets['youtube_channel_id']
        self._esp32_cs = DigitalInOut(board.ESP_CS)
        self._esp32_ready = DigitalInOut(board.ESP_BUSY)
        self._esp32_reset = DigitalInOut(board.ESP_RESET)
        self._spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
        self._esp = adafruit_esp32spi.ESP_SPIcontrol(self._spi, self._esp32_cs, self._esp32_ready, self._esp32_reset)

        requests.set_socket(socket, self._esp)

        if self._esp.status == adafruit_esp32spi.WL_IDLE_STATUS:
            print("ESP32 found and in idle mode")
        print("Firmware vers.", self._esp.firmware_version)
        print("MAC addr:", [hex(i) for i in self._esp.MAC_address])

        # for ap in self._esp.scan_networks():
        #     print("\t%s\t\tRSSI: %d" % (str(ap["ssid"], "utf-8"), ap["rssi"]))

        while not self._esp.is_connected:
            try:
                self._esp.connect_AP(secrets["ssid"], secrets["password"])
            except OSError as e:
                # TODO display error on screen
                continue

        # Initialize WiFi Pool (There can be only 1 pool & top of script)
        self.YT_request_kind = ""
        self.YT_response_kind = ""
        self.YT_channel_id = ""
        self.YT_videoCount = ""
        self.YT_viewCount = ""
        self.YT_subsCount = ""

        # https://youtube.googleapis.com/youtube/v3/channels?part=statistics&forUsername=[YOUR_USERNAME]&key=[YOUR_API_KEY]
        self.YT_SOURCE = (
                "https://youtube.googleapis.com/youtube/v3/channels?"
                + "part=statistics"
                + "&id="
                + self._yt_channel_id
                + "&key="
                + self._yt_key
        )

    def get_analytics(self):
        try:
            response = requests.get(self.YT_SOURCE).json()
            self.YT_subsCount = response["items"][0]["statistics"]["subscriberCount"]
            gc.collect()
            return self.YT_subsCount
        except ConnectionError as e:
            print("Connection Error:", e)
            self.YT_subsCount = 0
            return 0
