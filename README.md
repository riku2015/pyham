# Pyham
## HAM Radio with Python
*This pair of programs is under development and no working version is released yet.*

**Current versions:**

Server - 0.016

Client - 0.020

Protocol - 0.05

Config - 0.10

### About
The server program connects distant HAM radios together trough the Internet, thus giving them more range / coverage. The computer needs to be connected to real HAM radio hardware. Instructions are coming later...

The client program is for using your PC as it would be a HAM radio. No real radio needed - just connect to some server on the Internet and start talking with people, some of them having a PC client program, some of them having a real radio.

Both are to be compatible with [eQSO](https://en.wikipedia.org/wiki/Radio_over_IP#eQSO), [FRN](http://www.freeradionetwork.eu/) and [Echolink](http://www.echolink.org/). Pyham also introduces its own protocol.

There are three different user interfaces: Graphical [wxWidgets](https://wxwidgets.org) GUI, [Curses](https://en.wikipedia.org/wiki/Curses_(programming_library)) TUI and a single line command terminal.

You can also control the server and client programs with external programs usins sockets. A web page interface is coming also...

### Software requirements
This program requires [Python](https://www.python.org/) 3.x to be installed. Mandatory.

GUI is made with [wxFormBuilder](https://github.com/wxFormBuilder/wxFormBuilder) and is saved in files **client_gui.fbp** and **server_gui.fbp**. Not mandatory but recommended if you're changing the program.

**Python modules:**

[PyAudio](https://pypi.org/project/PyAudio/) is required for sound. Mandatory.

[wxPython](https://pypi.org/project/wxPython/) is required for graphical interface. Not mandatory if using command line interface.

[ncurses]() is required for interactive text terminal interface. Not mandatory if using single line command interface.

### How to install required libraries
> pip install pyaudio
>
> pip install wx
>
> pip install curses

Or use some other tool to install Python modules/libraries/packages called 'wx' and 'pyaudio'.

### How to run client
Start with graphical user interface:

> python pyham_client.py

Start with command line user interface:

> python pyham_client.py --nogui

Get help on command line parameters:

> python pyham_client.py --help

### How to run server
Start with graphical user interface:

> python pyham_server.py

Start with command line user interface:

> python pyham_server.py --nogui

Get help on command line parameters:

> python pyham_server.py --help

### Configuration
Configuration can be changed and saved at runtime. It is saved in files **pyham_client.conf** and **pyham_server.conf**.

You'll find commented configuration file templates in files **pyham_client.conf.template** and **pyham_server.conf.template**. 

#### Screenshots
![alt text](http://titanix.net/~japek/pyham-client-0020-wx-windows.png)

Client (wx) v. 0.020 (Windows 10)

---

![alt text](http://titanix.net/~japek/pyham-client-settings-0020-wx-windows.png)
Client (wx) v. 0.020 (Windows 10)

---

![alt text](http://titanix.net/~japek/pyham-server-0016-wx-windows.png)
Server (wx) v. 0.016 (Windows 10)

---

![alt text](http://titanix.net/~japek/pyham-server-settings-0016-wx-windows.png)
Server (wx) v. 0.016 (Windows 10)

---

![alt text](http://titanix.net/~japek/pyham-server-stats-0016-wx-windows.png)
Server (wx) v. 0.016 (Windows 10)

---

![alt text](http://titanix.net/~japek/pyham-client-0001.png)
Client (wx) v. 0.001 (GNU/Linux)
