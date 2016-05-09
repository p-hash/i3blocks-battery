#!/usr/bin/env python3
#
# A battery indicator blocklet script for i3blocks

from subprocess import check_output, Popen
import os

def icon(percent):
    if percent > 80:
        return "<span font='FontAwesome'>\uf240</span>"
    if percent > 60:
        return "<span font='FontAwesome'>\uf241</span>"
    if percent > 40:
        return "<span font='FontAwesome'>\uf242</span>"
    if percent > 20:
        return "<span font='FontAwesome'>\uf243</span>"
    return "<span font='FontAwesome'>\uf244</span>"

def color(percent):
    if percent < 5:
        return "#FFFFFF"
    if percent < 10:
        return "#FF0000"
    if percent < 20:
        return "#FF3300"
    if percent < 30:
        return "#FF6600"
    if percent < 40:
        return "#FF9900"
    if percent < 50:
        return "#FFCC00"
    if percent < 60:
        return "#FFFF00"
    if percent < 70:
        return "#99FF00"
    if percent < 80:
        return "#66FF00"
    return "#33FF00"

status = check_output(['acpi'], universal_newlines=True)
state = status.split(": ")[1].split(", ")[0]
commasplitstatus = status.split(", ")
percentleft = int(commasplitstatus[1].rstrip("%\n"))

FA_PLUG = "<span font='FontAwesome'>\uf1e6</span>"

fulltext = ""
timeleft = state + ", time left:"
time = commasplitstatus[-1].split()[0]
time = ":".join(time.split(":")[0:2])
timeleft += " {}".format(time)

if state == "Discharging":
    form = ' <span color="{}">{}</span>'
    fulltext += form.format(color(percentleft), icon(percentleft))
elif state == "Charging":
    # TODO charging animation
    fulltext += " " + icon(percentleft)
else:
    fulltext += " " + FA_PLUG

form =  '<span color="{}">{}%</span>'
percent_string = str(percentleft).rjust(3)
fulltext += form.format(color(percentleft), percent_string)

if os.environ.get('BLOCK_BUTTON'):
    Popen(['notify-send', timeleft])

print(fulltext)
print(fulltext)
if percentleft < 5:
    exit(33)
