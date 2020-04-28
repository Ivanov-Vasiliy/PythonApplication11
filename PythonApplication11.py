from PyQt5 import QtWidgets
from maingui import Ui_MainWindow
import sys
from square import Square

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.square = Square()

        try:
            self.square.download()
            self.download()
        except Exception:
            self.ui.errorlabel.setText("Загрузка неудалась")

        self.ui.resultButton.clicked.connect(self.checkSquare)
        self.ui.creaeteButton.clicked.connect(self.crete_matrix)

    def download(self):
        self.ui.tableWidget.setRowCount(4)
        self.ui.tableWidget.setColumnCount(4)
        for i in range(0, 4): 
            for j in range(0, 4):
                tableSpinBox = QtWidgets.QSpinBox()
                tableSpinBox.setMinimum(0) 
                tableSpinBox.setMaximum(self.square.N ** 2)
                tableSpinBox.setValue(self.square.square[i][j])
                self.ui.tableWidget.setCellWidget(i, j, tableSpinBox)

    def crete_matrix(self):
        N = 4
        self.square = Square(N)
        self.ui.errorlabel.clear()
        self.ui.result.clear()
        self.download()

    def closeEvent(self, event): 
        for i in range(0, self.square.N):
            for j in range(0, self.square.N):
                self.square.square[i][j] = self.ui.tableWidget.cellWidget(i, j).value()
        self.square.save()
        event.accept()

    def checkSquare(self):
        for i in range(0, self.square.N):
            for j in range(0, self.square.N):
                self.square.square[i][j] = self.ui.tableWidget.cellWidget(i, j).value()
        if self.square.isright(): 
            self.ui.result.setText("Правильное поле!")
        else:
            self.ui.result.setText("Неправильное поле")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())

