# Musical-Enigma
Python MQTT CPU RAM Usage

# Dependencies
* [Python3](https://www.python.org/)
* [pip](https://pip.pypa.io/en/stable/)
* [psutil](https://github.com/giampaolo/psutil/blob/master/INSTALL.rst)
* [Paho-MQTT](https://eclipse.org/paho/clients/python/)

# Installation
```
sudo apt install python3
sudo apt install python3-pip

pip install psutil
pip install paho-mqtt

git clone https://github.com/gzsierra/musical-enigma.git
```


# Usage
### Client Side
By default, the client will send the information every second
```
./pyClient.py
```

To change the default sending rate go in the file [pyClient.py](../master/pyClient.py) and change `interval=1` by `interval=[YOUR_NEW_RATE]`

### Server Side
Please check my other repo [PyTT](https://github.com/gzsierra/pytt) to see on how to configure your server to listen on the client.
Also, if you don't know on how to configure a OpenHAB server, [here](https://github.com/gzsierra/cautious-waffle.git) you will find a simple script that does everything for you!


# LICENCE
MIT
