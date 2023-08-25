import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from signature.get_map import uiMain
import PyPDF2

class PDFMerge(QWidget):

    def __init__(self, parent=None):
        self.saveDir = "C:/tmp"

        super(PDFMerge, self).__init__(parent)
        layout = QVBoxLayout()

        # 设置背景阈值
        # self.widget_1 = QWidget()
        # self.widget_1.setObjectName("widget_1")
        # self.form = QFormLayout(self.widget_1)
        # self.button = QPushButton("点击设置背景阈值（0-255）黑-白")
        # self.button.clicked.connect(self.getInt)
        # self.lineEdit = QLineEdit()
        # # layout.addRow(self.button, self.lineEdit)
        # self.form.addRow(self.button, self.lineEdit)
        # layout.addWidget(self.widget_1)

        # 加载图片
        self.btn = QPushButton()
        self.btn.clicked.connect(self.loadFile)
        self.btn.setText("选择要合并的PDF")
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
            fnames, _ = QFileDialog.getOpenFileNames(
                self, '选择文件', 'c:\\', 'All files(*)'
            )
            # for i, fname in enumerate(fnames):
            #     reader = PdfReader(fname)
            #     for page in reader.pages:
            #         # image = page.to_pixmap().toImage()
            #         image = page.extract_images()[0][0]
            #         self.label.setPixmap(QPixmap.fromImage(image))
            outputPath = f"{self.saveDir}/result.pdf"
            self.mergePdfs(fnames, outputPath)
            self.content.setText(f"PDF save to: {outputPath}")
        except Exception as e:
            self.content.setText(f"Error: {e}")

    # def loadText(self):
    #     print("load--text")
    #     dlg = QFileDialog()
    #     dlg.setFileMode(QFileDialog.AnyFile)
    #     dlg.setFilter(QDir.Files)
    #     if dlg.exec_():
    #         filenames = dlg.selectedFiles()
    #         f = open(filenames[0], 'r')
    #         with f:
    #             data = f.read()
    #             self.content.setText(data)
    #
    # def getInt(self):
    #     num, ok = QInputDialog.getInt(self, "输入整数框", "输入数字")
    #     if ok:
    #         self.gdThr = num if 0 < num < 256 else self.gdThr
    #         self.lineEdit.setText(str(self.gdThr))

    def mergePdfs(self, inputPaths, outputPath):
        # pdf_writer = PyPDF2.PdfFileWriter()
        pdfWriter = PyPDF2.PdfWriter()

        # 遍历输入的每个PDF文件路径
        for path in inputPaths:
            with open(path, 'rb') as file:
                pdfReader = PyPDF2.PdfReader(file)

                # 将每个输入的页追加到输出的PdfWriter对象中
                # for page_number in range(pdf_reader.numPages):
                #     page = pdf_reader.getPage(page_number)
                #     pdf_writer.addPage(page)
                for i, page in enumerate(pdfReader.pages):
                    # page = pdf_reader.getPage(page)

                    # page['/Contents']['/P'] = PyPDF2.generic.NumberObject(i + 1)

                    pdfWriter.add_page(page)

        # 将合并后的内容写入新的输出文件中

        with open(outputPath, 'wb') as outputFile:
            pdfWriter.write(outputFile)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fileload = PDFMerge()
    fileload.show()
    sys.exit(app.exec_())
    # input('please input any key to exit')



