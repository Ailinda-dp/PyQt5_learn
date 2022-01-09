import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget
def onClick_Button():
    # print("onClick")
    print("1")  # 窗口坐标
    print('Widget.x() = %d' % widget.x())
    print('widget.y() = %d' % widget.y())
    print('widget.width() = %d' % widget.width())
    print('widget.height() = %d' % widget.height())

    print('2')  # 工作区坐标
    print('Widget.geometry().x() = %d' % widget.geometry().x())
    print('widget.geometry().y() = %d' % widget.geometry().y())
    print('widget.geometry().width() = %d' % widget.geometry().width())
    print('widget.geometry().height() = %d' % widget.geometry().height())

    print('3')  # 窗口坐标（包含标题栏）
    print('Widget.framegeometry().x() = %d' % widget.frameGeometry().x())
    print('widget.framegeometry().y() = %d' % widget.frameGeometry().y())
    print('widget.framegeometry().width() = %d' % widget.frameGeometry().width())
    print('widget.framegeometry().height() = %d' % widget.frameGeometry().height())

app = QApplication(sys.argv)
widget = QWidget()
btn = QPushButton(widget)
btn.setText("按钮")
btn.clicked.connect(onClick_Button)

btn.move(24,52)

widget.resize(300,240)

widget.move(250,200)

widget.setWindowTitle('屏幕坐标系')

widget.show()

sys.exit(app.exec_())

