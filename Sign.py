import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from get_map import uiMain


class filedialogdemo(QWidget):

    def __init__(self, parent=None):
        self.gdThr = 100

        super(filedialogdemo, self).__init__(parent)
        layout = QVBoxLayout()

        # 设置背景阈值
        self.widget_1 = QWidget()
        self.widget_1.setObjectName("widget_1")
        self.form = QFormLayout(self.widget_1)
        self.button = QPushButton("点击设置背景阈值（0-255）黑-白")
        self.button.clicked.connect(self.getInt)
        self.lineEdit = QLineEdit()
        # layout.addRow(self.button, self.lineEdit)
        self.form.addRow(self.button, self.lineEdit)
        layout.addWidget(self.widget_1)

        # 加载图片
        self.btn = QPushButton()
        self.btn.clicked.connect(self.loadFile)
        self.btn.setText("从文件夹获取照片")
        layout.addWidget(self.btn)

        self.label = QLabel()
        layout.addWidget(self.label)

        # # 加载文本 从文本中获取图片
        # self.btn_2 = QPushButton()
        # self.btn_2.clicked.connect(self.loadText)
        # self.btn_2.setText("加载电脑文本文件")
        # layout.addWidget(self.btn_2)

        self.content = QTextEdit()
        layout.addWidget(self.content)
        self.setWindowTitle("Sign By Bio")

        self.setLayout(layout)

    def loadFile(self):
        print("load--file")
        try:
            fname, _ = QFileDialog.getOpenFileName(self, '选择图片', 'c:\\', 'Image files(*.jpg *.gif *.png)')
            self.label.setPixmap(QPixmap(fname))
            result, code = uiMain(fname, self.gdThr)
            if code:
                self.content.setText(f"Image save to: {result}")
            else:
                self.content.setText(f"Error: {result}")
        except Exception as e:
            self.content.setText(f"Error: {e}")

    def loadText(self):
        print("load--text")
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')
            with f:
                data = f.read()
                self.content.setText(data)

    def getInt(self):
        num, ok = QInputDialog.getInt(self, "输入整数框", "输入数字")
        if ok:
            self.gdThr = num if 0 < num < 256 else self.gdThr
            self.lineEdit.setText(str(self.gdThr))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fileload = filedialogdemo()
    fileload.show()
    sys.exit(app.exec_())
    # input('please input any key to exit')




"""
cd Path~/Sign.py
pyinstaller -F -i favicon.ico -w Sign.py -p get_map.py

版本推荐
Package                   Version                   key component
------------------------- ---------
altgraph                  0.17.3
certifi                   2021.5.30
future                    0.18.2
importlib-metadata        4.8.3
numpy                     1.19.5                    *
opencv-python             4.5.3.56                  *
pefile                    2022.5.30
Pillow                    8.4.0
pip                       21.2.2
pyinstaller               4.10                      *
pyinstaller-hooks-contrib 2022.0
PyQt5                     5.15.5                    *
PyQt5-Qt5                 5.15.2
PyQt5-sip                 12.9.1
pywin32-ctypes            0.2.0
setuptools                58.0.4                    *
typing_extensions         4.1.1
wheel                     0.37.1                    *
wincertstore              0.2
zipp                      3.6.0


"""