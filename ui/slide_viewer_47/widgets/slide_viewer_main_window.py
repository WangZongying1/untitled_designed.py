import cv2
from PyQt5.QtWidgets import QMainWindow

from slide_viewer_47.widgets.slide_viewer import SlideViewer


class SlideViewerMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Slide viewer')
        self.resize(1000, 900)
        self.slide_viewer = SlideViewer(viewer_top_else_left=True)

        self.setCentralWidget(self.slide_viewer)


