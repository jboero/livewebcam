# LiveWebCam
Open source wxPython systray tool to monitor your webcam activation and control external lights or notification for others.

# Dependencies
python3-wx

# Usage
LiveWebCam will reside in your systray and monitor the uvcvideo driver being used by a device ever 1s.  If one or more webcams goes active, it will run the script you place in your home directory at `~/bin/webcam_activated.sh`.  If deactivated it will run `~/bin/webcam_deactivated.sh`.  Be very careful what you place in those scripts at your own risk.  Otherwise copy the script and replace their call with the task of your choice.

This can be used to control smart lights, switch USB power on/off with `uhubctl` and supported hubs, or just pop up notifications in your taskbar.
