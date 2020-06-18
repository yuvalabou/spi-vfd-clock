# VFD display examples Using a NanoPi NEO2 (But any SBC with Armbian and SPI Interface should work)

Display model: Noritake-Itron CU20045-UW5J
Datasheet, Footprint (Eagle) and 3D model are available on my other repo - [Noritake VFD Display](https://github.com/yuvalabou/Eagle-Library/tree/master/Noritake_VFD)

Since the display is using 3 wire SPI and the Pi is using 4 an extra step is needed, Please follow the wiring tutorial from [smbaker](https://www.smbaker.com/interfacing-a-vfd-display-to-the-raspberry-pi) which I have also based my program on.

The VFD library is a mishmash between [smbaker](https://github.com/sbelectronics) library and the library used by bob [thisoldgeek](https://github.com/thisoldgeek) in his [RPi-boombox](https://github.com/thisoldgeek/RPi-boombox).

Please note that since the NanoPi does not have an RTC it needs to access the internet to update it's internal time.

## Notable features:

 - python 3 only
 - VFD lib is separeted from the main app so you can use it individually in your own design! just import it and you good to go.

## Installation:

Configure your Pi SPI interface (Instructions may vary depends on manufacturer and OS), and reboot.

```
sudo apt-get update
sudo apt-get install -y python3 python-dev python-pip
pip3 install spidev psutil urllib2

git clone https://github.com/yuvalabou/spi-vfd-clock
cd spi-vfd-clock
```

## Running the app:

```
python3 clock.py
```
***Run the script in the background***
please note the process id so you could kill it later when needed.
```
python3 clock.py &
```
***Run your script at boot***
```
sudo nano /etc/rc.local
#add this line with a path to your script. Don't forget the '&' symbol
python3 /path/to/spi-vfd-clock/clock.py &
```

## For running the PiHole app instructions are obviously the same, Just change the app name.
---
<a href="https://www.buymeacoffee.com/HMa8m26" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>