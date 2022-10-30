import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication

from slide_viewer_47.common.slide_view_params import SlideViewParams
from slide_viewer_47.widgets.slide_viewer_main_window import SlideViewerMainWindow


def excepthook(excType, excValue, tracebackobj):
    print(excType, excValue, tracebackobj)


sys.excepthook = excepthook

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cache_size_in_kb = 700 * 10 ** 3
    QPixmapCache.setCacheLimit(cache_size_in_kb)
    win = SlideViewerMainWindow()
    slide_path = r'D:\PycharmProjects\slide_viewer_47\app_screen.png'

    # slide_path = '/home/dimathe47/Downloads/JP2K-33003-1.svs'
    # slide_path = '/home/dimathe47/Downloads/OS-1.ndpi'
    # slide_path = r'C:\Users\dmitriy\Downloads\JP2K-33003-1.svs'
    # slide_path = r'C:\Users\DIMA\PycharmProjects\slide_cbir_47\downloads\images\19403.svs'
    # slide_path = r'C:\Users\dmitriy\PycharmProjects\slide_cbir_47\downloads\images\19403.svs'
    # slide_path = r'C:\Users\DIMA\PycharmProjects\slide_cbir_47\temp\slides\Aperio\CMU-1.svs'
    win.show()
    slide_view_params = SlideViewParams(slide_path)
    win.slide_viewer.load(slide_view_params)
    sys.exit(app.exec_())
