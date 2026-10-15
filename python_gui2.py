import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,300,1000,1000)

        label = QLabel("haillu",self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(20,20 ,700,100)
        label.setStyleSheet("color : Red;""font-weight : bold;""font-style : italic;""background-color : blue;""text-decoration : underline")
        label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        #label.setAlignment(Qt.AlignLeft)
        #label.setAlignment(Qt.AlignTop)
        #label.setAlignment(Qt.AlignBottom)
        #label.setAlignment(Qt.AlignRight)

def main():
    app =  QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())
if __name__ =="__main__":
    main()

