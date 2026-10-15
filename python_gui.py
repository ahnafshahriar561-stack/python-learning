import sys

# CHANGE 1: Remove the extra word "import" (it should just start with 'from')
from  PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("hello")
        self.setGeometry(100,200,400,700)
        self.setWindowIcon(QIcon("Ahnaf.jpeg"))
# CHANGE 2: Remove the stray "QApplication" text floating at the end of the function definition
def main ():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# CHANGE 3: Swap the order—the variable '__name__' must be on the left, and the string '__main__' on the right
if __name__ == '__main__':
    main()