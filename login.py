from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QMessageBox, QMainWindow
from PyQt5.QtGui import QFont
from Fun_Select import Ui_MainWindow
import sys

class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.setWindowTitle('Login')
        self.setFixedSize(300, 120)

        # 设置字体
        font = QFont()
        font.setPointSize(12)
        self.setFont(font)

        # 创建控件
        self.username_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton('Login')
        self.login_button.setDefault(True)
        self.login_button.clicked.connect(self.login)
        self.message_label = QLabel()


        # 创建布局
        layout = QVBoxLayout()
        form_layout = QFormLayout()
        form_layout.addRow('Username:', self.username_edit)
        form_layout.addRow('Password:', self.password_edit)
        layout.addLayout(form_layout)
        layout.addWidget(self.login_button)
        layout.addWidget(self.message_label)

        self.setLayout(layout)

    def login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        # TODO: 在这里编写验证用户名和密码的代码
        # 如果验证成功，关闭窗口，并返回 QDialog.Accepted
        # 如果验证失败，显示错误信息，并返回 QDialog.Rejected
        # 例如：
        if username == 'admin' and password == '123456':
            self.accept()
        else:
            self.message_label.setText('Invalid username or password')
            QMessageBox.warning(self, 'Error', 'Invalid username or password', QMessageBox.Ok)

app = QApplication([])
login_dialog = LoginDialog()

if login_dialog.exec_() == QDialog.Accepted:
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
else:
    sys.exit(app.exec_())
