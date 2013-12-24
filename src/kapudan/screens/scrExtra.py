# -*- coding: utf-8 -*-
#
# Copyright (C) 2012, The Chakra Developers
#
# This is a fork of Pardus's Kaptan, which is
# Copyright (C) 2005-2009, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

from PyQt4 import QtGui

from PyKDE4.kdecore import i18n, KConfig

#from PyKDE4 import kdeui

from kapudan.screen import Screen
from kapudan.screens.ui_scrExtra import Ui_extraWidget
from kapudan.tools.repos import Repos


isUpdateOn = False


class Widget(QtGui.QWidget, Screen):
    title = i18n("GTK")
    desc = i18n("GTK Integration and [extra]")

    screenSettings = {}
    screenSettings["hasChanged"] = False

    def __init__(self, *args):
        QtGui.QWidget.__init__(self, None)
        self.ui = Ui_extraWidget()
        self.ui.setupUi(self)

        # check the current config
        self.config = Repos()

        # set initial states
        self.ui.enableExtra.setChecked(self.config.isEnabled())

    def applySettings(self):
        # update hasChanged
        if self.ui.enableExtra.isChecked():
            # was [extra] enabled before?
            if self.config.isEnabled():
                self.__class__.screenSettings["hasChanged"] = False
            else:
                self.__class__.screenSettings["hasChanged"] = True

        else:
            # was [extra] enabled before?
            if self.config.isEnabled():
                self.__class__.screenSettings["hasChanged"] = True
            else:
                self.__class__.screenSettings["hasChanged"] = False

    def shown(self):
        pass

    def execute(self):
        self.applySettings()
        return True