

# pyham
## HAM Radio with Python

### About
*This program is under development and no working version is released yet.*

With this program you can connect many HAM radios together trough the Internet.

You can also use your PC as it would be a HAM radio itself.

Configuration can be changed at runtime. It is saved in files **pyham_client.conf** and **pyham_server.conf**.

You'll find commented configuration file templates in files **pyham_client.conf.template** and **pyham_server.conf.template**. 

### Software requirements
This program requires [Python](https://www.python.org/) 3.x to be installed. Tested with Python 3.6 on Windows.

[wxPython](https://pypi.org/project/wxPython/) is required for graphical interface.

[PyAudio](https://pypi.org/project/PyAudio/) is required for sound in the client. Not required for the server.

### How to install required libraries:
> pip install wx
>
> pip install pyaudio

Or use some other tool to install Python modules/libraries/packages called 'wx' and 'pyaudio'.

### How to run client:
> python pyham_client.py

Get help on command line parameters:

> python pyham_client.py --help

### How to run server:
> python pyham_server.py

Get help on command line parameters:

> python pyham_server.py --help

#### Screenshots:

![alt text](http://titanix.net/~japek/pyham-client-0001.png)

Ver. 0.001
