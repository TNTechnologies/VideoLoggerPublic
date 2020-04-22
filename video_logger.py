"""
Video_logger was created to efficiently record and display video streams from downhole cameras.

Author: Kyle Boblitt
Created: 04/21/2020
Edited:
"""

# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

# import Opencv module
import cv2

from ui_main_window import *

class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # create a timer to
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # start view camera function during init
        self.controlTimer()

    #view camera
    def viewCam(self):
        # read image in BGR format
        ret, frame = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # get image information
        height, width, channels = image.shape
        step =  channels * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        #show image in videoLabel
        self.ui.videoLabel.setPixmap(QPixmap.fromImage(qImg))

    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            #create video captured
            self.cap = cv2.VideoCapture(0)
            # start timer
            self.timer.start(20)
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()

if __name__ == '__main__':
    app =  QApplication(sys.argv)

    # create and show main window
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())

