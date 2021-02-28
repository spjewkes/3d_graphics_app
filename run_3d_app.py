#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Application that runs the landscape generator program.
"""
import argparse
import sys
import math

from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtGui import QPainter, QImage, QColor

from core.buffer import GBuffer
from core.geometry import Mesh, Triangle
from core.vector import Vector4d
from core.matrix import Matrix


def createCube():
    vectors = [Vector4d(0, 0, 0), Vector4d(0, 1, 0), Vector4d(1, 1, 0), Vector4d(1, 0, 0),
               Vector4d(0, 0, 1), Vector4d(0, 1, 1), Vector4d(1, 1, 1), Vector4d(1, 0, 1)]

    triangles = [
        # South
        Triangle(vectors[0], vectors[1], vectors[2]),
        Triangle(vectors[0], vectors[2], vectors[3]),
        # West
        Triangle(vectors[0], vectors[4], vectors[5]),
        Triangle(vectors[0], vectors[5], vectors[1]),
        # Up
        Triangle(vectors[1], vectors[5], vectors[6]),
        Triangle(vectors[1], vectors[6], vectors[2]),
        # East
        Triangle(vectors[2], vectors[6], vectors[7]),
        Triangle(vectors[2], vectors[7], vectors[3]),
        # Down
        Triangle(vectors[3], vectors[7], vectors[4]),
        Triangle(vectors[3], vectors[4], vectors[0]),
        # North
        Triangle(vectors[4], vectors[6], vectors[5]),
        Triangle(vectors[4], vectors[7], vectors[6])
    ]

    mesh = Mesh(triangles)

    return mesh


class AppWindow(QWidget):
    def __init__(self, width, height, parent=None):
        super(AppWindow, self).__init__(parent)

        self.cube = createCube()
        self.proj = Matrix.createProjection(width, height, 1.5708, 1000, 0.1)

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
