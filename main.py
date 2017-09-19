import sys
import re
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtQml import *
from PyQt5.QtQuickWidgets import *


def val(self):
    try:
        s = search.text()
        f = re.split(r',*', s)
        a = f[0]
        b = f[1]
        ctx = view.rootContext()
        ctx.setContextProperty("g", a)
        ctx.setContextProperty("f", b)
        view.rootContext
    except Exception:
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Error 404")
        msgBox.setText("Invalid Coordinates")
        msgBox.addButton(QPushButton("exit"), QMessageBox.RejectRole)
        ret = msgBox.exec_()
    else:
        s = search.text()
        f = re.split(r',*', s)
        a = f[0]
        b = f[1]
        ctx = view.rootContext()
        ctx.setContextProperty("g", a)
        ctx.setContextProperty("f", b)
        view.rootContext


# Main Function
if __name__ == '__main__':
    # Create main app
    myApp = QApplication(sys.argv)
    # create search option and Button
    search = QLineEdit()
    searchButton = QPushButton("Search for coordinates")
    searchButton.clicked.connect(val)

    # Create Layout
    window = QWidget()
    window.setLayout(QVBoxLayout())
    # Create Qml reference
    view = QQuickWidget()
    view.setSource(QUrl('map.qml'))
    view.setMinimumSize(200, 200)
    view.setResizeMode(view.SizeRootObjectToView)
    # Add widgets to layout
    window.layout().addWidget(search)
    window.layout().addWidget(searchButton)
    window.layout().addWidget(view)
    window.setMinimumSize(500, 500)
    # Show the Layout
    window.show()
    # Execute the Application and Exit
    myApp.exec_()
    sys.exit()
