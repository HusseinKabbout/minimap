import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtQml import QQmlApplicationEngine


def val(self):
    s = search.text()
    ctx = engine.rootContext()
    ctx.setContextProperty("g", s)
    engine.rootObjects()[0]


def vall(self):
    s = ssearch.text()
    ctx = engine.rootContext()
    ctx.setContextProperty("f", s)
    engine.rootObjects()[0]


# Main Function
if __name__ == '__main__':
    # Create main app
    myApp = QApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.load(QUrl('map.qml'))
    # create search option
    search = QLineEdit()
    searchButton = QPushButton("searchg")
    searchButton.clicked.connect(val)

    ssearch = QLineEdit()
    ssearchButton = QPushButton("searchf")
    ssearchButton.clicked.connect(vall)
    # Execute the Application and Exit
    search.show()
    ssearch.show()
    searchButton.show()
    ssearchButton.show()
    myApp.exec_()
    sys.exit()
