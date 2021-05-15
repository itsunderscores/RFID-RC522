<br />
<p align="center">
  <a href="https://github.com/itsunderscores">
    <img src="https://avatars.githubusercontent.com/u/84211119?s=400&u=acc77c1d7fe1d778bdcba08993ba0ca0249fa89f&v=4" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">RFID RC522 Tool by Underscores</h3>
</p>

# RFID-RC522
Python3 RFID RC522 Tool that allows you to read and write with ease
I used this software with my Raspberry Pi 4 Model B


### Installation
1. Enable SPI
```
sudo raspi-config
```
* On here use the arrow keys to select “5 Interfacing Options“. Once you have this option selected, press Enter.
* Now on this next screen, you want to use your arrow keys to select “P4 SPI“, again press Enter to select the option once it is highlighted.
* You will now be asked if you want to enable the SPI Interface, select Yes with your arrow keys and press Enter to proceed. You will need to wait a little bit while the raspi-config tool does its thing in enabling SPI.
* Once the SPI interface has been successfully enabled by the raspi-config tool you should see the following text appear on the screen, “The SPI interface is enabled“.
* Before the SPI Interface is fully enabled we will first have to restart the Raspberry Pi. To do this first get back to the terminal by pressing Enter and then ESC.

2. Reboot
```
reboot
```

3. Modifying config boot file
   ```
   sudo nano /boot/config.txt
   dtparam=spi=on
   ```
   
4. Install packages
  ```sudo apt-get update
  sudo apt-get upgrade
  sudo apt-get install python3-dev python3-pip
  sudo pip3 install spidev
  sudo pip3 install mfrc522
  ```
  
## How to Use
```
python3 main.py
```
