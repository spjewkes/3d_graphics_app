#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Application that runs the landscape generator program.
"""
import argparse
import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtGui import QPainter, QImage, QColor

from core.buffer import GBuffer


class AppWindow(QWidget):
    def __init__(self, width, height, parent=None):
        super(AppWindow, self).__init__(parent)

        self.setFixedSize(width, height)
        self.image = GBuffer(width, height)

    def paintEvent(self, event):
        super(AppWindow, self).paintEvent(event)

        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)
        painter.end()


class MainWindow(QMainWindow):
    """
    Main application entry-point for Genscape.
    """

    def __init__(self, width, height, parent=None):
        super(MainWindow, self).__init__(parent)

        self._size = (width, height)

        self.home()

    def home(self):
        """
        Add the GUI elements to the window that represent the home state of the application.
        """
        self.widget = AppWindow(self._size[0], self._size[1])
        self.setCentralWidget(self.widget)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Simple 3d Explorer Application')
    parser.add_argument('--width', default=512,
                        type=int, help='Width of window')
    parser.add_argument('--height', default=512,
                        type=int, help='Height of window')

    args = parser.parse_args()

    # Create the Qt Application
    APP = QApplication(sys.argv)
    # Create and show the form
    MAIN = MainWindow(args.width, args.height)
    MAIN.show()
    # Run the main Qt loop
    sys.exit(APP.exec_())
