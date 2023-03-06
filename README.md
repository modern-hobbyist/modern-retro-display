# modern-retro-display
A DIY Take on the Retro-Style Tidbyt Display

# Intro
First off, I want to say that I think the Tidbyt displays are awesome, and this project is my attempt at making one of my own. However, I do want to mention that this version of the project is far simpler and therefore, can't do nearly as much as the Tidbyt displays. This limitation (for the most part) is simply because I don't have enough time to build out all the apps, but that's where you come in!

Also, unlike the Tidbyt displays, you can't push new apps to this version and there isn't an existing library of apps for you to choose from. No, this project is DIY through and through, so if you want to, say, install a weather app, you better get coding!

In the end, this project turned out awesome, and I was able to display a little logo for my channel, add some scrolling text, and display my subscriber count, in human-format which ended up looking great!

If you want to get one of these set up yourself, follow the instructions below!

One last quick note before you get started though! I ended up completing this project with two different Microcontrollers, for a couple reasons. First, I used a Raspberry Pi Pico W because they are fairly cheap, Waveshare has a baseboard that makes setup with a Matrix display super easy, AND because, to be honest, Pico's are super cool and I wanted to give them a shot.

However, the Pico only had about 500kb of space to work with once I had flashed CircuitPython onto it, so that got me looking for an alternative solutions, which led me to the MatrixPortal M4. 

Setup is not quite as simple as the Pico + baseboard, but it's definitely not hard. However, the main benefit is that the MatrixPortal comes with a WiFi coprocessor and 2mb of QSPI flash storage, most of which was still available after flashing CircuitPython. 

I've included setup steps for both microcontrollers below!

# Setup
## Google Analytics (YouTube) API Key
- Follow these instructions to set up a new API key for the YouTube API V3
[https://insightwhale.com/how-to-set-up-google-analytics-api-step-by-step-guide/](https://insightwhale.com/how-to-set-up-google-analytics-api-step-by-step-guide/)

## MatrixPortal M4 (Best Option IMO)

### Prerequisites
- MatrixPortal M4 board
- USB cable
- Computer running Windows, macOS, or Linux
- Internet connection

### Steps
1. Go to the [CircuitPython download page](https://circuitpython.org/board/matrixportal_m4/) and download the latest CircuitPython firmware for the MatrixPortal M4.
2. Connect your MatrixPortal M4 to your computer using a USB cable.
3. Press the reset button on your MatrixPortal M4 twice. This will put the board into bootloader mode.
4. The MatrixPortal M4 should now appear as a removable drive named `MATRIXBOOT`.
5. Drag and drop the CircuitPython firmware file onto the `MATRIXBOOT` drive.
6. Wait for the file transfer to complete, then eject the `MATRIXBOOT` drive.
7. The MatrixPortal M4 will reboot and CircuitPython should be installed.

## Copying a CircuitPython project to the MatrixPortal M4

### Prerequisites
- MatrixPortal M4 board with CircuitPython installed
- USB cable
- Computer running Windows, macOS, or Linux
- Text editor or Integrated Development Environment (IDE)

### Steps
1. Connect your MatrixPortal M4 to your computer using a USB cable.
2. The MatrixPortal M4 should appear as a removable drive named `CIRCUITPY`.
3. Download this project repo, and drag & drop the `matrix-portal/src` folder contents to the `CIRCUITPY` drive.
4. Rename the `secrets_example.py` file to `secrets.py`
5. Open `secrets.py` in a text editor and update the credentials to yours.

	```python
	'ssid': 'WIFI_NETWORK_NAME', # Your Wifi Networkd
    'password': 'WIFI_PASSWORD', # Your Wifi Password
    'youtube_channel_id': 'UCjgA1ehfjkZ4WMa5Cw9f1LA',  # This is Modern Hobbyist, set to your channel of choice
    'youtube_token': 'YOUTUBE_API_TOKEN', # Your Google Analytics API Token
	```
	
6. Save all project files.
7. The MatrixPortal M4 will automatically detect the new file and run it.

## Raspberry Pi Pico
### Prerequisites
- Raspberry Pi Pico board OR MatrixPortal M4
- Micro USB cable OR USB C cable
- Computer running Windows, macOS, or Linux
- Internet connection

### Steps
1. Go to the [CircuitPython download page](https://circuitpython.org/board/raspberry_pi_pico/) and download the latest CircuitPython firmware for the Raspberry Pi Pico.
2. Connect your Pico to your computer using a USB cable. 
3. Press and hold the BOOTSEL button on your Pico, then plug the USB cable into your computer. Continue to hold the BOOTSEL button until the drive named `RPI-RP2` appears on your computer.
4. Drag and drop the CircuitPython firmware file onto the `RPI-RP2` drive.
5. Wait for the file transfer to complete, then eject the `RPI-RP2` drive.
6. The Raspberry Pi Pico will reboot and CircuitPython should be installed.

## Copying a CircuitPython project to the Raspberry Pi Pico

### Steps
1. Connect your Pico to your computer using a USB cable.
2. The Pico should appear as a removable drive named `CIRCUITPY`.
3. Download this project repo, and drag & drop the `rpi-pico/src` folder contents to the `CIRCUITPY` drive.
4. Rename the `secrets_example.py` file to `secrets.py`
5. Open `secrets.py` in a text editor and update the credentials to yours.

	```python
	'ssid': 'WIFI_NETWORK_NAME', # Your Wifi Networkd
    'password': 'WIFI_PASSWORD', # Your Wifi Password
    'youtube_channel_id': 'UCjgA1ehfjkZ4WMa5Cw9f1LA',  # This is Modern Hobbyist, set to your channel of choice
    'youtube_token': 'YOUTUBE_API_TOKEN', # Your Google Analytics API Token
	```

6. Save all project files.
7. The MatrixPortal M4 will automatically detect the new file and run it.
