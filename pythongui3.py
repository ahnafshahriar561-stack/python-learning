import sys
from PyQt5.QtWidgets import QApplication,QMainWindow ,QLabel,QWidget,QHBoxLayout,QVBoxLayout,QGridLayout
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,500,500)
        self.Init_ui()
    def Init_ui(self):
        central_widjet = QWidget()
        self.setCentralWidget(central_widjet)

        label1 = QLabel("#1")
        label2 = QLabel("#2")
        label3 = QLabel("#3")
        label4 = QLabel("#4")
        label5 = QLabel("#5")

        label1.setStyleSheet("background-color : red")
        label2.setStyleSheet("background-color : green")
        label3.setStyleSheet("background-color : blue")
        label4.setStyleSheet("background-color : yellow")
        label5.setStyleSheet("background-color : pink")

        vbox = QGridLayout()

        vbox.addWidget(label1,0,0)
        vbox.addWidget(label2,1,1)
        vbox.addWidget(label3,2,2)
        vbox.addWidget(label4,2,1)
        vbox.addWidget(label5,1,2)

        central_widjet.setLayout(vbox)


def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())
if __name__=='__main__':
    main()


