import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWin, self).__init__(parent)

        self.setWindowTitle("第一个主窗口应用")

        self.resize(400, 300)

        self.status = self.statusBar()

        self.status.showMessage('只存在5s的消息', 5000)
        self.center()
        # 只在Windows下有显示效果
        self.setWindowIcon(QIcon('./images/IMG_2344.ico'))

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = round((screen.width() - size.width()) / 2)
        newTop = round((screen.height() - size.height()) / 2)
        self.move(newLeft, newTop)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("G:\shiyan\PyQt5_learn\src\controls\images\IMG_2344.ico"))

    main = FirstMainWin()
    main.show()

    sys.exit(app.exec_())