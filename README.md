# VFD display clock Using a NanoPi NEO2 (But any SBC with Armbian and SPI Interface should work)

Display model: Noritake-Itron CUU2045-UW5J
Datasheet, Footprint (Eagle) and 3D model are available on my other repo - [Noritake VFD Display](https://github.com/yuvalabou/Eagle-Library/tree/master/Noritake_VFD)

Since the display is using 3 wire SPI and the Pi is using 4 an extra step is needed, Please follow the wiring tutorial from [smbaker](https://www.smbaker.com/interfacing-a-vfd-display-to-the-raspberry-pi) which I have also based my program on.

## Installation:

Configure your Pi SPI interface (May vary depends on manufacturer and OS) and reboot.

```
sudo apt-get update
sudo apt-get install -y python python-dev python-pip
pip install spidev

git clone https://github.com/yuvalabou/spi-vfd-clock
cd spi-vfd-clock
```

## Running the app:

```
python clock.py
```