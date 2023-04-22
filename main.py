# main.py

from PyQt5.QtWidgets import QApplication
from login import LoginDialog
from Fun_Select import Ui_MainWindow


app = QApplication([])

# Create the login widget and show it
login_widget = Login()
login_widget.show()

# Create the other widgets but don't show them yet
gui2_widget = Gui2()
gui3_widget = Gui3()
gui4_widget = Gui4()

# Connect the login_successful signal from the login widget to the show_gui2 slot of the gui2 widget
login_widget.login_successful.connect(gui2_widget.show_gui2)

# Connect the show_gui3 signal from the gui2 widget to the show_gui3 slot of the gui3 widget
gui2_widget.show_gui3.connect(gui3_widget.show_gui3)

# Connect the show_gui4 signal from the gui2 widget to the show_gui4 slot of the gui4 widget
gui2_widget.show_gui4.connect(gui4_widget.show_gui4)

app.exec_()
