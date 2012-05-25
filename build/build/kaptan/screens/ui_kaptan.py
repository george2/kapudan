#!/usr/bin/env python2
# coding=UTF-8
#
# Generated by pykdeuic4 from ui/ui_kaptan.ui on Fri May 25 09:42:09 2012
#
# WARNING! All changes to this file will be lost.
from PyKDE4 import kdecore
from PyKDE4 import kdeui
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_kaptan(object):
    def setupUi(self, kaptan):
        kaptan.setObjectName(_fromUtf8("kaptan"))
        kaptan.setWindowModality(QtCore.Qt.NonModal)
        kaptan.setEnabled(True)
        kaptan.resize(997, 751)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(kaptan.sizePolicy().hasHeightForWidth())
        kaptan.setSizePolicy(sizePolicy)
        kaptan.setMinimumSize(QtCore.QSize(600, 400))
        kaptan.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(10)
        kaptan.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pixmap/cr64-app-kaptan.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        kaptan.setWindowIcon(icon)
        kaptan.setAutoFillBackground(False)
        kaptan.setStyleSheet(_fromUtf8("#kaptanContainer{\n"
"    background-image: url(:/raw/pixmap/bg2.png);\n"
"    /*background-repeat: no-repeat;\n"
"    background-position: left top;*/\n"
"    /*background-color: #642437;*/\n"
"    /*alternate-background-color: gray;\n"
"    selection-background-color: gray;*/\n"
"   background-color: rgb(50, 50, 50);\n"
"    /*background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:0.572, y2:0.688, stop:0 rgba(75, 114, 137, 255), stop:1 rgba(29, 42, 51, 255));*/\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"#description {\n"
"    color:rgb(240, 240, 240);\n"
"}\n"
""))
        self.verticalLayout_2 = QtGui.QVBoxLayout(kaptan)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.kaptanContainer = QtGui.QWidget(kaptan)
        self.kaptanContainer.setObjectName(_fromUtf8("kaptanContainer"))
        self.verticalLayout = QtGui.QVBoxLayout(self.kaptanContainer)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_5 = QtGui.QLabel(self.kaptanContainer)
        self.label_5.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Sans"))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("padding: 5px 5px 5px 5px; \n"
"border:0px;\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(132, 132, 132, 255), stop:0.501481 rgba(70, 70, 70, 255), stop:0.503057 rgba(62, 62, 62, 255), stop:1 rgba(16, 16, 16, 255));\n"
"border-bottom: 1px solid rgba(0,0,0,10)"))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pixmap/cr64-app-kaptan.png")))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setMargin(0)
        self.label_5.setIndent(0)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.screenTitle = QtGui.QLabel(self.kaptanContainer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.screenTitle.sizePolicy().hasHeightForWidth())
        self.screenTitle.setSizePolicy(sizePolicy)
        self.screenTitle.setMinimumSize(QtCore.QSize(0, 40))
        self.screenTitle.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.screenTitle.setFont(font)
        self.screenTitle.setStyleSheet(_fromUtf8("border:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(132, 132, 132, 255), stop:0.501481 rgba(70, 70, 70, 255), stop:0.503057 rgba(62, 62, 62, 255), stop:1 rgba(16, 16, 16, 255));\n"
"/*qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(183, 100, 124, 255), stop:0.0212465 rgba(91, 33, 50, 255), stop:0.521739 rgba(152, 86, 105, 255), stop:0.527174 rgba(155, 98, 115, 255), stop:0.983696 rgba(184, 141, 153, 255), stop:1 rgba(220, 173, 186, 255));*/\n"
"border-bottom: 1px solid rgba(0,0,0,10);\n"
"color:rgb(240, 240, 240)"))
        self.screenTitle.setLineWidth(0)
        self.screenTitle.setMidLineWidth(0)
        self.screenTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.screenTitle.setMargin(0)
        self.screenTitle.setIndent(0)
        self.screenTitle.setObjectName(_fromUtf8("screenTitle"))
        self.horizontalLayout.addWidget(self.screenTitle)
        self.label_4 = QtGui.QLabel(self.kaptanContainer)
        self.label_4.setMaximumSize(QtCore.QSize(90, 50))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(_fromUtf8("padding: 13px 15px 13px 15px;\n"
"border:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(132, 132, 132, 255), stop:0.501481 rgba(70, 70, 70, 255), stop:0.503057 rgba(62, 62, 62, 255), stop:1 rgba(16, 16, 16, 255));\n"
"border-bottom: 1px solid rgba(0,0,0,10)"))
        self.label_4.setLineWidth(0)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pixmap/kaptan-logo.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setMargin(0)
        self.label_4.setIndent(0)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.labelProgress = QtGui.QLabel(self.kaptanContainer)
        self.labelProgress.setMinimumSize(QtCore.QSize(0, 30))
        self.labelProgress.setMaximumSize(QtCore.QSize(50, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(10)
        self.labelProgress.setFont(font)
        self.labelProgress.setAutoFillBackground(False)
        self.labelProgress.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: rgba(0, 0, 0, 70);\n"
""))
        self.labelProgress.setLineWidth(2)
        self.labelProgress.setText(_fromUtf8(""))
        self.labelProgress.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProgress.setWordWrap(False)
        self.labelProgress.setIndent(0)
        self.labelProgress.setObjectName(_fromUtf8("labelProgress"))
        self.horizontalLayout_4.addWidget(self.labelProgress)
        self.labelMenu = QtGui.QLabel(self.kaptanContainer)
        self.labelMenu.setMinimumSize(QtCore.QSize(300, 35))
        self.labelMenu.setMaximumSize(QtCore.QSize(300, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        self.labelMenu.setFont(font)
        self.labelMenu.setAutoFillBackground(False)
        self.labelMenu.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: rgba(0, 0, 0, 70);"))
        self.labelMenu.setLineWidth(2)
        self.labelMenu.setText(_fromUtf8(""))
        self.labelMenu.setScaledContents(False)
        self.labelMenu.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelMenu.setWordWrap(False)
        self.labelMenu.setIndent(0)
        self.labelMenu.setObjectName(_fromUtf8("labelMenu"))
        self.horizontalLayout_4.addWidget(self.labelMenu)
        self.labelMenu_2 = QtGui.QLabel(self.kaptanContainer)
        self.labelMenu_2.setMinimumSize(QtCore.QSize(0, 35))
        self.labelMenu_2.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(6)
        self.labelMenu_2.setFont(font)
        self.labelMenu_2.setAutoFillBackground(False)
        self.labelMenu_2.setStyleSheet(_fromUtf8("color: white;\n"
"background-color: rgba(0, 0, 0, 70);\n"
"padding: 10px;\n"
""))
        self.labelMenu_2.setLineWidth(2)
        self.labelMenu_2.setText(_fromUtf8(""))
        self.labelMenu_2.setScaledContents(False)
        self.labelMenu_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelMenu_2.setWordWrap(False)
        self.labelMenu_2.setIndent(0)
        self.labelMenu_2.setObjectName(_fromUtf8("labelMenu_2"))
        self.horizontalLayout_4.addWidget(self.labelMenu_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.mainStack = QtGui.QStackedWidget(self.kaptanContainer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainStack.sizePolicy().hasHeightForWidth())
        self.mainStack.setSizePolicy(sizePolicy)
        self.mainStack.setStyleSheet(_fromUtf8("QStackedWidget#mainStack{\n"
"/*background-color:rgba(255, 255, 255,0);*/\n"
"margin: 0px;\n"
"border-radius: 0px;\n"
"color: white;\n"
"}\n"
"QLineEdit {\n"
"border: 1px solid gray;\n"
"}"))
        self.mainStack.setFrameShape(QtGui.QFrame.NoFrame)
        self.mainStack.setFrameShadow(QtGui.QFrame.Plain)
        self.mainStack.setLineWidth(0)
        self.mainStack.setObjectName(_fromUtf8("mainStack"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.mainStack.addWidget(self.page)
        self.verticalLayout_4.addWidget(self.mainStack)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.groupBoxMenu = QtGui.QGroupBox(self.kaptanContainer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxMenu.sizePolicy().hasHeightForWidth())
        self.groupBoxMenu.setSizePolicy(sizePolicy)
        self.groupBoxMenu.setMinimumSize(QtCore.QSize(0, 33))
        self.groupBoxMenu.setMaximumSize(QtCore.QSize(16777215, 33))
        self.groupBoxMenu.setStyleSheet(_fromUtf8("#groupBoxMenu{\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(132, 132, 132, 255), stop:0.501481 rgba(70, 70, 70, 255), stop:0.503057 rgba(62, 62, 62, 255), stop:1 rgba(16, 16, 16, 255));\n"
"    border-top: 1px solid white\n"
"}\n"
"\n"
"QPushButton{\n"
"    padding: 3px 10px 3px 10px;\n"
"    color: white;\n"
"    border:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(132, 132, 132, 255), stop:0.501481 rgba(70, 70, 70, 255), stop:0.503057 rgba(62, 62, 62, 255), stop:1 rgba(16, 16, 16, 255));\n"
"    /*background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(120, 146, 172, 255), stop:0.0155729 rgba(99, 141, 164, 255), stop:0.538376 rgba(49, 84, 106, 255), stop:1 rgba(51, 72, 91, 255))*/\n"
"}\n"
"\n"
"QPushButton::flat:hover{\n"
"    border:1px solid  rgba(34, 49, 60, 100);\n"
"    border-radius:2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(129, 3, 3, 255), stop:0.0192308 rgba(160, 35, 25, 255), stop:0.521739 rgba(166, 35, 29, 255), stop:0.531585 rgba(184, 46, 40, 255), stop:0.983696 rgba(168, 78, 74, 255), stop:1 rgba(210, 110, 110, 255))\n"
"}\n"
"\n"
"QPushButton::flat{\n"
"    border:1px solid  rgba(34, 49, 60, 100);\n"
"    border-radius:2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(132, 132, 132, 255), stop:0.501481 rgba(70, 70, 70, 255), stop:0.503057 rgba(62, 62, 62, 255), stop:1 rgba(16, 16, 16, 255));\n"
"    /*\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(26, 38, 45, 150), stop:0.398093 rgba(44, 62, 79, 255), stop:0.521739 rgba(36, 61, 76, 255), stop:0.531585 rgba(40, 68, 86, 255), stop:0.983696 rgba(73, 109, 129, 255), stop:1 rgba(89, 108, 127, 255))\n"
"    */\n"
"}\n"
"\n"
"QPushButton::flat:pressed{\n"
"    border:1px solid  rgba(34, 49, 60, 100);\n"
"    border-radius:2px;\n"
"    padding: 3px 10px 3px 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(129, 3, 3, 255), stop:0.0192308 rgba(160, 35, 25, 255), stop:0.521739 rgba(166, 35, 29, 255), stop:0.531585 rgba(184, 46, 40, 255), stop:0.983696 rgba(168, 78, 74, 255), stop:1 rgba(210, 110, 110, 255))\n"
"}\n"
"\n"
"/*\n"
"QPushButton{\n"
"    padding: 3px 10px 3px 10px;\n"
"    color: white;\n"
"    border:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(120, 146, 172, 255), stop:0.0155729 rgba(99, 141, 164, 255), stop:0.538376 rgba(49, 84, 106, 255), stop:1 rgba(51, 72, 91, 255))\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton::flat:hover{\n"
"    border:1px solid  rgba(34, 49, 60, 100)\n"
"    border-radius:2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(129, 3, 3, 255), stop:0.0192308 rgba(160, 35, 25, 255), stop:0.521739 rgba(166, 35, 29, 255), stop:0.531585 rgba(184, 46, 40, 255), stop:0.983696 rgba(168, 78, 74, 255), stop:1 rgba(210, 110, 110, 255))\n"
"}\n"
"\n"
"QPushButton::flat{\n"
"    border:1px solid  rgba(34, 49, 60, 100);\n"
"    border-radius:2px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(26, 38, 45, 150), stop:0.398093 rgba(44, 62, 79, 255), stop:0.521739 rgba(36, 61, 76, 255), stop:0.531585 rgba(40, 68, 86, 255), stop:0.983696 rgba(73, 109, 129, 255), stop:1 rgba(89, 108, 127, 255))\n"
" \n"
"}\n"
"\n"
"QPushButton::flat:pressed{\n"
"    border:1px solid  rgba(34, 49, 60, 100);\n"
"    border-radius:2px;\n"
"    padding: 3px 10px 3px 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(129, 3, 3, 255), stop:0.0192308 rgba(160, 35, 25, 255), stop:0.521739 rgba(166, 35, 29, 255), stop:0.531585 rgba(184, 46, 40, 255), stop:0.983696 rgba(168, 78, 74, 255), stop:1 rgba(210, 110, 110, 255))\n"
"\n"
"}*/"))
        self.groupBoxMenu.setTitle(_fromUtf8(""))
        self.groupBoxMenu.setFlat(True)
        self.groupBoxMenu.setObjectName(_fromUtf8("groupBoxMenu"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxMenu)
        self.gridLayout_2.setContentsMargins(5, 0, 5, 0)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.buttonCancel = QtGui.QPushButton(self.groupBoxMenu)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pixmap/cross.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonCancel.setIcon(icon1)
        self.buttonCancel.setFlat(True)
        self.buttonCancel.setObjectName(_fromUtf8("buttonCancel"))
        self.gridLayout_2.addWidget(self.buttonCancel, 0, 0, 1, 1)
        self.buttonBack = QtGui.QPushButton(self.groupBoxMenu)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pixmap/arrow-left.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonBack.setIcon(icon2)
        self.buttonBack.setFlat(True)
        self.buttonBack.setObjectName(_fromUtf8("buttonBack"))
        self.gridLayout_2.addWidget(self.buttonBack, 0, 2, 1, 1)
        self.buttonNext = QtGui.QPushButton(self.groupBoxMenu)
        self.buttonNext.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pixmap/arrow-right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonNext.setIcon(icon3)
        self.buttonNext.setCheckable(False)
        self.buttonNext.setAutoRepeat(False)
        self.buttonNext.setAutoExclusive(False)
        self.buttonNext.setAutoDefault(False)
        self.buttonNext.setDefault(False)
        self.buttonNext.setFlat(True)
        self.buttonNext.setObjectName(_fromUtf8("buttonNext"))
        self.gridLayout_2.addWidget(self.buttonNext, 0, 4, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.buttonFinish = QtGui.QPushButton(self.groupBoxMenu)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/raw/pixmap/tick.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonFinish.setIcon(icon4)
        self.buttonFinish.setCheckable(False)
        self.buttonFinish.setAutoRepeat(False)
        self.buttonFinish.setAutoExclusive(False)
        self.buttonFinish.setAutoDefault(False)
        self.buttonFinish.setDefault(False)
        self.buttonFinish.setFlat(True)
        self.buttonFinish.setObjectName(_fromUtf8("buttonFinish"))
        self.gridLayout_2.addWidget(self.buttonFinish, 0, 6, 1, 1)
        self.buttonApply = QtGui.QPushButton(self.groupBoxMenu)
        self.buttonApply.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttonApply.setIcon(icon3)
        self.buttonApply.setCheckable(False)
        self.buttonApply.setAutoRepeat(False)
        self.buttonApply.setAutoExclusive(False)
        self.buttonApply.setAutoDefault(False)
        self.buttonApply.setDefault(False)
        self.buttonApply.setFlat(True)
        self.buttonApply.setObjectName(_fromUtf8("buttonApply"))
        self.gridLayout_2.addWidget(self.buttonApply, 0, 5, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxMenu)
        self.verticalLayout_2.addWidget(self.kaptanContainer)

        self.retranslateUi(kaptan)
        self.mainStack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(kaptan)

    def retranslateUi(self, kaptan):
        kaptan.setWindowTitle(kdecore.i18n(_fromUtf8("Kaptan")))
        self.screenTitle.setText(kdecore.i18n(_fromUtf8("Welcome to Pardus")))
        self.buttonCancel.setText(kdecore.i18n(_fromUtf8("Cancel")))
        self.buttonBack.setText(kdecore.i18n(_fromUtf8("Back")))
        self.buttonNext.setText(kdecore.i18n(_fromUtf8("Next")))
        self.buttonFinish.setText(kdecore.i18n(_fromUtf8("Finish")))
        self.buttonApply.setText(kdecore.i18n(_fromUtf8("Apply Settings")))

import kaptan.kaptan_rc