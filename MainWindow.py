import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
import eegAnalyze
import sys

qtCreatorFile = 'EEGAnalyze.ui'  # Window File


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        loadUi('EEGAnalyze.ui', self)
        self.SelectButton.clicked.connect(self.select_click)
        self.StartButton.clicked.connect(self.start_click)
        self.StopButton.clicked.connect(self.stop_click)
        self.ImageLabel.setPixmap(QPixmap('icon.jpg'))
        self.ImageLabel.setScaledContents(True)
        self.file = ''

    def select_click(self):
        fname = QFileDialog.getOpenFileName(self, 'open file', '/')
        if fname[0]:
            self.FileText.setText(fname[0])
            self.FileText.adjustSize()
            self.file = fname[0]

    def start_click(self):
        if self.file == '':
            self.ResultView.setPlainText('请先选择文件再开始！')
            return
        self.ResultView.setPlainText('分析开始')
        res = eegAnalyze.test_Analyze(self.file)
        self.setResult(res)

    def stop_click(self):
        self.ResultView.setPlainText('停止分析')

    # 获取文件路径
    def get_file_path(self):
        return self.file

    def setResult(self, str):
        self.ResultView.setPlainText('分析完成')
        self.ResultView.append(str)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
