# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VideoLogger.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """

        :type MainWindow: object
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1305, 949)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.record = QtWidgets.QPushButton(self.centralwidget)
        self.record.setGeometry(QtCore.QRect(10, 750, 231, 27))
        self.record.setObjectName("record")
        self.screenShot = QtWidgets.QPushButton(self.centralwidget)
        self.screenShot.setGeometry(QtCore.QRect(260, 750, 1031, 121))
        self.screenShot.setMinimumSize(QtCore.QSize(841, 0))
        self.screenShot.setObjectName("screenShot")
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(10, 800, 221, 19))
        self.statusLabel.setObjectName("statusLabel")
        self.timeLable = QtWidgets.QLabel(self.centralwidget)
        self.timeLable.setGeometry(QtCore.QRect(10, 840, 231, 19))
        self.timeLable.setObjectName("timeLable")
        self.videoLabel = QtWidgets.QLabel(self.centralwidget)
        self.videoLabel.setGeometry(QtCore.QRect(10, 10, 1280, 720))
        self.videoLabel.setScaledContents(True)
        self.videoLabel.setObjectName("videoLabel")
       # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1305, 24))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionWell_INfo = QtWidgets.QAction(MainWindow)
        self.actionWell_INfo.setObjectName("actionWell_INfo")
        self.actionUpgrade = QtWidgets.QAction(MainWindow)
        self.actionUpgrade.setObjectName("actionUpgrade")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionDrive_mapping = QtWidgets.QAction(MainWindow)
        self.actionDrive_mapping.setObjectName("actionDrive_mapping")
        self.menuMenu.addAction(self.actionWell_INfo)
        self.menuMenu.addAction(self.actionUpgrade)
        self.menuMenu.addAction(self.actionDrive_mapping)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionQuit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Logger"))
        self.record.setText(_translate("MainWindow", "Record"))
        self.record.setShortcut(_translate("MainWindow", "R"))
        self.screenShot.setText(_translate("MainWindow", "Screen Shot"))
        self.screenShot.setShortcut(_translate("MainWindow", "Space"))
        self.statusLabel.setText(_translate("MainWindow", "Status: Recording"))
        self.timeLable.setText(_translate("MainWindow", "HH:MM:SS  -  400Mb"))
        self.videoLabel.setText(_translate("MainWindow", "Video Label"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionWell_INfo.setText(_translate("MainWindow", "Well Info"))
        self.actionWell_INfo.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionUpgrade.setText(_translate("MainWindow", "Upgrade"))
        self.actionUpgrade.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionDrive_mapping.setText(_translate("MainWindow", "Drive Map"))
