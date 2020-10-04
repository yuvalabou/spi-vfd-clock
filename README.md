# VFD display examples Using Python

_Here I am using NanoPi NEO2, But any SBC with Armbian and SPI Interface should work_

<img src=
    "https://github.com/yuvalabou/spi-vfd-clock/blob/master/Screenshot.jpg?raw=true"
    width=500>

## Hardware

Display model: Noritake-Itron CU20045-UW5J
Datasheet, Footprint (Eagle) and 3D model are available on my other repo - [Noritake VFD Display](https://github.com/yuvalabou/Eagle-Library/tree/master/Noritake_VFD)

Since the display is using 3 wire SPI and the Pi is using 4 an extra step is needed, Please follow the wiring tutorial from [smbaker](https://www.smbaker.com/interfacing-a-vfd-display-to-the-raspberry-pi) which I have also based my program on.

The VFD library is a mishmash between [smbaker](https://github.com/sbelectronics) library and the library used by bob [thisoldgeek](https://github.com/thisoldgeek) in his [RPi-boombox](https://github.com/thisoldgeek/RPi-boombox).

For the PiHole monitor i'm using an altered code from [bradgillap](https://github.com/bradgillap) in his super simple code in [I2C LCD Display](https://github.com/bradgillap/I2C-LCD-Display).

Please note that since the NanoPi does not have an RTC it needs to access the internet to update it's internal time.

---

## Apps

- PiHole monitor
- Simple clock with system stats

---

## Installation

Configure your Pi SPI interface (Instructions may vary depends on manufacturer and OS), and reboot.

```shell
sudo apt-get update
sudo apt-get install -y python3 python-dev python-pip
pip3 install spidev psutil urllib

git clone https://github.com/yuvalabou/spi-vfd-clock
cd spi-vfd-clock
```

## Running the app

```shell
python3 clock.py
```

***Run the script in the background***
please note the process id so you could kill it later when needed.

```shell
python3 clock.py &
```

***Run your script at boot***

Add this line to your /etc/rc.local file

```shell
python3 /path/to/spi-vfd-clock/clock.py &
```

## For running the PiHole app, Just change the app name

---

<a href="https://www.buymeacoffee.com/HMa8m26" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>