#!/bin/bash
WINDOW_TITLE=$(echo -n $(xdotool getactivewindow getwindowname))
WINDOW_ID=$(wmctrl -l | grep -F "$WINDOW_TITLE" | awk '{printf $1}')
$(/usr/bin/python2.7 /home/ripster/Scripts/borderless/windowtool.py --decorations 0 $WINDOW_ID)
$(/usr/bin/python2.7 /home/ripster/Scripts/borderless/windowtool.py --move 1920,0 $WINDOW_ID)
