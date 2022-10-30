from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication

from ui.untitled_designed import Ui_MainWindow


def openImage(self):  # 选择本地图片上传
    global imgName  # 这里为了方便别的地方引用图片路径，我们把它设置为全局变量
    imgName, imgType = QFileDialog.getOpenFileName(self.centralwidget, "打开图片", "",
                                                   "*.jpg;;*.png;;All Files(*)")  # 弹出一个文件选择框，第一个返回值imgName记录选中的文件路径+文件名，第二个返回值imgType记录文件的类型
    jpg = QtGui.QPixmap(imgName).scaled(self.choosepic.width(),
                                        self.choosepic.height())  # 通过文件路径获取图片文件，并设置图片长宽为label控件的长宽
    self.choosepic.setPixmap(jpg)  # 在label控件上显示选择的图片
    self.choosepic.setText(imgName)  # 显示所选图片的本地路径


def saveImage(self):  # 保存图片到本地
    screen = QApplication.primaryScreen()
    pix = screen.grabWindow(self.choosepic.winId())
    fd, type = QFileDialog.getSaveFileName(self.centralwidget, "保存图片", "", "*.jpg;;*.png;;All Files(*)")
    pix.save(fd)



def main():
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        formObj = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(formObj)
        formObj.show()
        sys.exit(app.exec_())
