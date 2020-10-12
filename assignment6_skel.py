import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        n = QLabel("Name:", self)
        n.move(15, 10)
        a = QLabel("Age:", self)
        a.move(175, 10)
        s = QLabel("Score:", self)
        s.move(335, 10)
        am = QLabel("Amount:", self)
        am.move(200, 40)
        k = QLabel("Key:", self)
        k.move(390, 40)
        r = QLabel("Reslt:", self)
        r.move(15, 100)

        N = QLineEdit(self)
        N.move(57,7)
        A = QLineEdit(self)
        A.move(202, 7)
        S = QLineEdit(self)
        S.move(377, 7)
        AM = QLineEdit(self)
        AM.move(254, 38)

        addb = QPushButton("Add", self)
        addb.move(70, 70)
        delb = QPushButton("Del", self)
        delb.move(153,70)
        findb = QPushButton("Find", self)
        findb.move(236, 70)
        incb = QPushButton("inc", self)
        incb.move(319, 70)
        showb = QPushButton("show", self)
        showb.move(402, 70)

        cb = QComboBox(self)
        cb.addItem("Age")
        cb.addItem("Name")
        cb.addItem("Score")
        cb.move(420,37)


        R = QTextEdit(self)
        R.move(15,120)
        R.resize(470,120)


        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        pass


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())



