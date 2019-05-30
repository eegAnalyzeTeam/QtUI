import sys
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

    def select_click(self):
        fname = QFileDialog.getOpenFileName(self, 'open file', '/')
        if fname[0]:
            self.FileText.setText(fname[0])

    def start_click(self):
        self.ResultView.setPlainText('')
        self.ResultView.setPlainText('分析开始')

    def stop_click(self):
        self.ResultView.setPlainText('')
        self.ResultView.setPlainText('停止分析')


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
