import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建QApplication这个类的一个实例
    app = QApplication(sys.argv)

    # 创建一个窗口
    w = QWidget()

    # 设置窗口的尺寸
    w.resize(400, 200)

    # 移动窗口（将左上角移到指定位置）
    w.move(300, 300)

    # 设置窗口标题
    w.setWindowTitle('first')

    # 显示
    w.show()

    # 进入程序的主循环，并通过exit函数确保主循环正常结束
