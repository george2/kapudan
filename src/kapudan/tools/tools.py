#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import dbus
import glob
import subprocess
from PyQt5.QtWidgets import QDesktopWidget


def DBus():
    if not dbus.get_default_main_loop():
        from dbus.mainloop.qt import DBusQtMainLoop
        DBusQtMainLoop(set_as_default=True)


def importScreen(screenName):
    ''' imports a screen by name '''
    screen = __import__(screenName)
    for s in screenName.split('.')[1:]:
        screen = getattr(screen, s)
    return screen


def loadScreens(screensPath, globals):
    ''' imports all screens in the specified directory '''
    screens = glob.glob(screensPath)
    for screen in screens:
        screenName = screen.split("/")[-1].split(".")[0]
        globals[screenName] = importScreen("kapudan.screens." + screenName)


def isLiveCD():
    return os.path.exists('/var/run/pardus/livemedia')


def getRelease():
    p = subprocess.Popen(["lsb_release", "-ircs"], stdout=subprocess.PIPE)
    release, err = p.communicate()
    return release.decode('utf-8').replace("\n", "")


def killPlasma(self):
    p = subprocess.Popen(["pidof", "-s", "plasma-desktop"], stdout=subprocess.PIPE)
    out, err = p.communicate()
    pidOfPlasma = int(out)

    try:
        os.kill(pidOfPlasma, 15)
        self.startPlasma()
    except OSError as e:
        print("WARNING: failed os.kill: ", e)
        print("Trying SIGKILL")
        os.kill(pidOfPlasma, 9)
        startPlasma()


def startPlasma(self):
    subprocess.Popen(["plasma-desktop"], stdout=subprocess.PIPE)


def centerWindow(window):
    rect = QDesktopWidget().screenGeometry()
    width = 0
    height = 0

    if rect.width() <= 640:
        width = 620
    elif rect.width() <= 800:
        width = 720
    else:
        width = 960

    if rect.height() <= 480:
        height = 450
    elif rect.height() <= 600:
        height = 520
    else:
        height = 680

    window.resize(width, height)
    window.move(rect.width() / 2 - window.width() / 2, rect.height() / 2 - window.height() / 2)
