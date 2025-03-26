# SettingsDemo
Small example of using ini-style QSettings in a PyQt5 application

Run it with
```
$ python settingsdemowindow.py
```
Toggle some stuff, click the toolbuttons, move and resize the window, then quit the app. The next time you open it, everything will be restored to how it was when you last closed the app.

To see the `.ini` file containing the saved settings, look for the filename printed to `stdout` when closing the app. It will contain some lines like this:
```
[Data]
A=true
B=false
C=true
D=false
E=true

[MainWindow]
pos=@Point(2005 25)
size=@Size(1003 1638)

[RMSE]
n=false
rank=true
rw=false

[Spinner]
veryImportantNumber=82

[Tools]
eraser=false
paintbrush=true
```
