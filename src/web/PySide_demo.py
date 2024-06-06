import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

# 创建一个QApplication实例
app = QApplication(sys.argv)

# 创建一个QWidget作为主窗口
window = QWidget()
window.setWindowTitle('PySide 简单页面')
window.setGeometry(100, 100, 280, 80)  # 设置窗口位置和大小

# 创建一个QVBoxLayout布局管理器
layout = QVBoxLayout()

# 创建一个QLabel
label = QLabel('欢迎使用PySide')
layout.addWidget(label)  # 将标签添加到布局中

# 创建一个QPushButton
button = QPushButton('点击我')
layout.addWidget(button)  # 将按钮添加到布局中

# 设置窗口的布局为之前创建的QVBoxLayout
window.setLayout(layout)

# 连接按钮的点击信号到槽函数
def on_button_clicked():
    label.setText('按钮被点击了')

button.clicked.connect(on_button_clicked)

# 显示窗口
window.show()

# 运行事件循环
sys.exit(app.exec())
