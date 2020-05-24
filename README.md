# VFD display clock Using a NanoPi NEO2 (But any SBC with Armbian and SPI Interface should work)

Display model: Noritake-Itron CU20045-UW5J
Datasheet, Footprint (Eagle) and 3D model are available on my other repo - [Noritake VFD Display](https://github.com/yuvalabou/Eagle-Library/tree/master/Noritake_VFD)

Since the display is using 3 wire SPI and the Pi is using 4 an extra step is needed, Please follow the wiring tutorial from [smbaker](https://www.smbaker.com/interfacing-a-vfd-display-to-the-raspberry-pi) which I have also based my program on.


## Notable features:

 - Since the NanoPi does not have an RTC it needs to access the internet to update it's internal time.
 - python2.7/3.8 compatible
 - VFD lib is separeted from the main app so you can use it individually in your own design! just import it and you good to go.

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