import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication

class IconForm(QMainWindow):
    def __init__(self):
        super(IconForm,self).__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 250)

        # 设置主窗口的标题
        self.setWindowTitle('设置窗口图标')
        # 设置窗口的大小
        # self.resize(400,300)

        self.status = self.statusBar()

        self.status.showMessage('只存在5s的消息', 5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('./images/wmp.ico'))
    main = IconForm()
    main.show()

    sys.exit(app.exec_())