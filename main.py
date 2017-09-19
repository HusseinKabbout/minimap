import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtQml import *
from PyQt5.QtQuickWidgets import *


def val(self):
    s = search.text()
    ctx = view.rootContext()
    ctx.setContextProperty("g", s)
    view.rootContext


def vall(self):
    s = ssearch.text()
    ctx = view.rootContext()
    ctx.setContextProperty("f", s)
    view.rootContext


# Main Function
if __name__ == '__main__':
    # Create main app
    myApp = QApplication(sys.argv)
    # create search option and Button
    search = QLineEdit()
    searchButton = QPushButton("Search for X Coordinate")
    searchButton.clicked.connect(val)

    ssearch = QLineEdit()
    ssearchButton = QPushButton("Search for Y Coordinate")
    ssearchButton.clicked.connect(vall)
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
    window.layout().addWidget(ssearch)
    window.layout().addWidget(ssearchButton)
    window.layout().addWidget(view)
    window.setMinimumSize(500, 500)
    # Show the Layout
    window.show()
    # Execute the Application and Exit
    myApp.exec_()
    sys.exit()
