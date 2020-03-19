# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VideoLogger.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import cv2
import sys


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1305, 949)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 750, 100, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 750, 100, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 750, 1031, 121))
        self.pushButton_3.setMinimumSize(QtCore.QSize(841, 0))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 800, 221, 19))
        self.label.setObjectName("status")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 840, 231, 19))
        self.label_2.setObjectName("timeFile")




        ''''''
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 1280, 720))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("videoLabel")






        MainWindow.setCentralWidget(self.centralwidget)
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
        self.pushButton.setText(_translate("MainWindow", "Record"))
        self.pushButton.setShortcut(_translate("MainWindow", "R"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop"))
        self.pushButton_3.setText(_translate("MainWindow", "Screen Shot"))
        self.pushButton_3.setShortcut(_translate("MainWindow", "Space"))
        self.label.setText(_translate("MainWindow", "Status: Stopped"))
        self.label_2.setText(_translate("MainWindow", "HH:MM:SS  -  400Mb"))
        self.label_3.setText(_translate("MainWindow", "Video Label"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionWell_INfo.setText(_translate("MainWindow", "Well Info"))
        self.actionWell_INfo.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionUpgrade.setText(_translate("MainWindow", "Upgrade"))
        self.actionUpgrade.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionDrive_mapping.setText(_translate("MainWindow", "Drive Map"))

    def close_application(self):
        """Clean exit of application"""

    def record(self):
        '''Initiate save to file'''

    def stop(self):
        '''Stops recording to file'''

    def well_info(self):
        '''Launch well information dialogue box'''

    def update(self):
        '''Update app from github'''

    def take_screenshot(self):
        '''Take a screen shot and save to file'''

    def config_drive_map(self):
        '''Opens the configure drive map interface'''



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
