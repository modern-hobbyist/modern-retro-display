import time
import adafruit_requests
import gc
import wifi
import socketpool
import ssl


class YouTubeAnalytics:
    def __init__(self, secrets) -> None:
        # Don't commit this, it's secret...
        self._wifi_ssid = secrets['ssid']
        self._wifi_pass = secrets['password']
        self._yt_key = secrets['youtube_token']
        self._yt_channel_id = secrets['youtube_channel_id']

        # Connect to Wi-Fi
        while not wifi.radio.ipv4_address:
            try:
                wifi.radio.connect(self._wifi_ssid, self._wifi_pass)
            except ConnectionError as e:
                print("Connection Error:", e)
            time.sleep(10)
            gc.collect()

        # Initialize WiFi Pool (There can be only 1 pool & top of script)
        self.pool = socketpool.SocketPool(wifi.radio)

        # self.pool = pool
        self.requests = adafruit_requests.Session(self.pool, ssl.create_default_context())
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
            response = self.requests.get(self.YT_SOURCE).json()
            self.YT_subsCount = response["items"][0]["statistics"]["subscriberCount"]
            gc.collect()
            return self.YT_subsCount
        except ConnectionError as e:
            print("Connection Error:", e)
            self.YT_subsCount = 0
            return 0
