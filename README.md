

# Pyham
## HAM Radio with Python
*This pair of programs is under development and no working version is released yet.*

### About
The server program connects distant HAM radios together trough the Internet, thus giving them more range / coverage. The computer needs to be connected to real HAM radio hardware. Instructions are coming later...

The client program is for using your PC as it would be a HAM radio. No real radio needed - just connect to some server on the Internet and start talking with people, some of them having a PC client program, some of them having a real radio.

Both are to be compatible with [eQSO](https://en.wikipedia.org/wiki/Radio_over_IP#eQSO), [FRN](http://www.freeradionetwork.eu/) and [Echolink](http://www.echolink.org/). Pyham also introduces its own protocol.

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
Start with graphical user interface:

> python pyham_client.py

Start with command line user interface:

> python pyham_client.py --nogui

Get help on command line parameters:

> python pyham_client.py --help

### How to run server:
Start with graphical user interface:

> python pyham_server.py

Start with command line user interface:

> python pyham_server.py --nogui

Get help on command line parameters:

> python pyham_server.py --help

### Configuration
Configuration can be changed and saved at runtime. It is saved in files **pyham_client.conf** and **pyham_server.conf**.

You'll find commented configuration file templates in files **pyham_client.conf.template** and **pyham_server.conf.template**. 

#### Screenshots:

![alt text](http://titanix.net/~japek/pyham-client-0001.png)

Ver. 0.001
