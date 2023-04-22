# 为了将这两段代码合并到一个页面中，我们可以创建一个新的主窗口类，将这两个窗口的布局添加到该类中，并使用选项卡小部件将它们分开。以下是实现这个目标的示例代码：

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QFileDialog, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QTextEdit, QMessageBox, QTableWidget, QTableWidgetItem
)
import shutil
import os
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget
)
from PyQt5 import QtCore, QtGui, QtWidgets
import shutil
import os
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis




# 将 MyWidget 类代码放在这里
class MyWidget(QMainWindow):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 600)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 367, 75, 24))

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(670, 500, 75, 24))

        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 100, 550, 400))
        self.widget.setObjectName("widget")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.checkBox = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "导入"))
        self.pushButton1.setText(_translate("MainWindow", "执行"))
        self.checkBox.setText(_translate("MainWindow", "PCA"))
        self.checkBox_2.setText(_translate("MainWindow", "LDA"))
        self.label_2.setText(_translate("MainWindow", "模块"))
        self.label_5.setText(_translate("MainWindow", "其他"))
        self.label.setText(_translate("MainWindow", "半球"))
        self.label_3.setText(_translate("MainWindow", "Rich-Club"))
        self.label_4.setText(_translate("MainWindow", "纤维长度"))

    # PCA 特征选择
    def do_pca(X, n_components):
        pca = PCA(n_components=n_components)
        X_pca = pca.fit_transform(X)
        return X_pca

    # LDA 特征选择
    def do_lda(X, y, n_components):
        lda = LinearDiscriminantAnalysis(n_components=n_components)
        X_lda = lda.fit_transform(X, y)
        return X_lda

# 将 App 类代码放在这里
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = '文件拷贝'
        self.left = 100
        self.top = 100
        self.width = 600
        self.height = 400
        self.file_paths = []
        self.target_path = ''
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # 创建一个标签
        label = QLabel('请选择要选择的文件或文件夹:', self)

        # 创建一个表格
        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['路径', '大小'])
        self.table.horizontalHeader().setStretchLastSection(True)

        # 创建一个按钮，用于选择拷贝文件的路径
        target_button = QPushButton('选择目标路径', self)
        target_button.setToolTip('点击选择目标路径')
        target_button.clicked.connect(self.chooseTargetPath)

        # 创建一个按钮，用于选择要拷贝的文件或文件夹
        file_button = QPushButton('选择文件或文件夹', self)
        file_button.setToolTip('点击选择文件或文件夹')
        file_button.clicked.connect(self.chooseFiles)

        # 创建一个按钮，用于执行拷贝操作
        copy_button = QPushButton('拷贝', self)
        copy_button.setToolTip('点击拷贝文件或文件夹')
        copy_button.clicked.connect(self.copyFiles)

        # 创建一个垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(self.table)

        # 创建一个水平布局，用于放置选择文件或文件夹和选择目标路径的按钮
        hbox1 = QHBoxLayout()
        hbox1.addWidget(file_button)
        hbox1.addWidget(target_button)

        # 创建一个水平布局，用于放置拷贝按钮
        hbox2 = QHBoxLayout()
        hbox2.addWidget(copy_button)

        # 将水平布局添加到垂直布局中
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        # 将垂直布局设置为窗口的主要布局
        self.setLayout(vbox)

        self.show()

    def chooseTargetPath(self):
        # 打开文件夹选择对话框，选择拷贝文件的目标路径
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        target_path = QFileDialog.getExistingDirectory(self, "选择目标路径", options=options)
        if target_path:
            self.target_path = target_path

    def chooseFiles(self):
        # 打开文件或文件夹选择对话框，选择要拷贝的文件或文件夹
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_dialog = QFileDialog(self, "选择文件或文件夹", "", "All Files (*);;Python Files (*.py)", options=options)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        if file_dialog.exec_():
            file_names = file_dialog.selectedFiles()
            # 将选择的文件或文件夹添加到表格中
            self.file_paths = file_names
            self.table.setRowCount(len(self.file_paths))
            for i, path in enumerate(self.file_paths):
                # 获取文件或文件夹名
                name = os.path.basename(path)
                # 获取文件或文件夹大小
                size = self.getFileSize(path)
                # 在表格中添加文件或文件夹路径和大小
                self.table.setItem(i, 0, QTableWidgetItem(name))
                self.table.setItem(i, 1, QTableWidgetItem(size))

    def getFileSize(self, path):
        # 获取文件或文件夹大小
        if os.path.isfile(path):
            size = os.path.getsize(path)
            return self.convertSize(size)
        elif os.path.isdir(path):
            size = sum(os.path.getsize(os.path.join(dirpath, filename)) for dirpath, dirnames, filenames in os.walk(path) for filename in filenames)
            return self.convertSize(size)

    def convertSize(self, size):
        # 将文件或文件夹大小转换为可读格式
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f"{size:.2f}{unit}"
            size /= 1024.0

    def copyFiles(self):
        # 拷贝文件或文件夹
        if not self.file_paths:
            QMessageBox.warning(self, '警告', '请选择要运行的文件或文件夹', QMessageBox.Ok)
            return
        if not self.target_path:
            QMessageBox.warning(self, '警告', '请选择运行文件或文件夹执行的目标路径', QMessageBox.Ok)
            return
        for path in self.file_paths:
            # 获取文件或文件夹名
            name = path.split('/')[-1]
            target_path = self.target_path
            # 拷贝文件或文件夹
            try:
                shutil.copy(path, os.path.join(self.target_path, name))
            except FileExistsError:
                shutil.copy(path, os.path.join(self.target_path, f"{name} (1)"))
            QMessageBox.information(self, '提示', '拷贝成功', QMessageBox.Ok)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('PCA、LDA导入界面')
        self.setGeometry(100, 100, 800, 600)

        # 创建一个选项卡小部件
        self.tab_widget = QTabWidget()

        # 创建 MyWidget 和 App 实例
        self.my_widget = MyWidget()
        self.app = App()

        # 将实例添加到选项卡小部件中
        self.tab_widget.addTab(self.app, 'Tab 1')
        self.tab_widget.addTab(self.my_widget, 'Tab 2')

        # 创建一个布局，将选项卡小部件添加到布局中
        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)

        # 创建一个部件，将布局添加到部件中
        widget = QWidget()
        widget.setLayout(layout)

        # 将部件设置为主窗口的中央部件
        self.setCentralWidget(widget)


app = QApplication([])
app.setApplicationName("Calculon")
window = MainWindow()
window.show()
app.exec_()

