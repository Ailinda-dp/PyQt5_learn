
import sys
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QLabel, QWidget
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self):
        super(QLabelDemo,self).__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel()
        label2 = QLabel()
        label3 = QLabel()
        label4 = QLabel()

        label1.setText('<font color=yellow>这是一个文本标签.</font>')
        label1.setAutoFillBackground(True)
        patette = QPalette()
        patette.setColor(QPalette.Window,Qt.blue)

        label1.setPalette(patette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap('./images/sync.ico'))

        label4.setText("<a href='https://item.jd.com/12417265.html'>感谢关注《python从菜鸟到高手》</a>")
        label4.setAlignment(Qt.AlignRight)
        # 如果设为True，用浏览器打开链接，如果设为False，连接到槽
        label4.setOpenExternalLinks(True)
        label4.setToolTip('这是一个超级链接')

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)

        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')

    def linkHovered(self):
        print("当鼠标滑过label2标签时，触发事件")
    def linkClicked(self):
        print('当鼠标单击label4标签时，触发事件')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()

    sys.exit(app.exec_())