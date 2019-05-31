import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi

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

        # 样式
        self.SelectButton.setStyleSheet("QPushButton{color:black}"
                                        "QPushButton:hover{color:red}"
                                        "QPushButton{background-color:rgb(78,255,255)}"
                                        "QPushButton{border:2px}"
                                        "QPushButton{border-radius:10px}")
        self.StartButton.setStyleSheet("QPushButton{color:black}"
                                       "QPushButton:hover{color:red}"
                                       "QPushButton{background-color:rgb(78,255,255)}"
                                       "QPushButton{border:2px}"
                                       "QPushButton{border-radius:10px}")
        self.StopButton.setStyleSheet("QPushButton{color:black}"
                                      "QPushButton:hover{color:red}"
                                      "QPushButton{background-color:rgb(255, 78, 116)}"
                                      "QPushButton{border:2px}"
                                      "QPushButton{border-radius:10px}")

    def select_click(self):
        fname = QFileDialog.getOpenFileName(self, 'open file', '/')
        if fname[0]:
            self.FileText.setText(fname[0])
            self.file = fname[0]

    def start_click(self):
        self.ResultView.setPlainText('')
        self.ResultView.setPlainText('分析开始')

    def stop_click(self):
        self.ResultView.setPlainText('')
        self.ResultView.setPlainText('停止分析')

    # 获取文件路径
    def get_file_path(self):
        return self.file


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
