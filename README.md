# AutoTDM
AutoTDM will automatically start Target Display Mode when connecting a Thunderbolt cable to your iMac or MacBook. Works when devices have gone to sleep and when you reboot your iMac host.

The script polls your network interfaces and checks for when an established Thunderbolt bridge connection is assigned an IP. It then fires off the CMD+F2 keyboard command to your host machine (iMac) to start the Target Display Mode.

## Setup
Place thunderbolt_TDM.py and thunderbolt_TDM.command in your home directory

## Running via command line
```python
python ~/thunderbolt_TDM.py
```

## Running on Startup
If you want to have the script execute on iMac startup, add the shell file to your start up list:
- Apple Icon (top left) > System Preferences > Users and Groups > Login Items (right hand side)
- Click the + button and select the thunderbolt_TDM.command file located in your home directory (/Users/yourUserAccount)
- Enjoy :)



