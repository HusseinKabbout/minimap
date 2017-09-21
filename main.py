import sys
import re
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtQml import *
from PyQt5.QtQuickWidgets import *
from PyQt5.QtPositioning import *


def search(lineEdit, rootObject):
    try:
        f = re.split(r'(\d+\.?\d*),?\s+(\d+\.?\d*)', lineEdit.text())
        lat = float(f[1])
        lon = float(f[2])
        mapObject = rootObject.findChild(QObject, "map")
        markerObject = rootObject.findChild(QObject, "marker")
        mapObject.setProperty("lat", lat)
        mapObject.setProperty("lon", lon)
        markerObject.setProperty("coordinate", QGeoCoordinate(lat, lon))
        markerObject.setProperty("visible", True)
    except Exception as e:
        QMessageBox.warning(None, "Invalid Coordinate", "Invalid coordinate")
        lineEdit.selectAll()


# Main Function
if __name__ == '__main__':
    # Create main app
    myApp = QApplication(sys.argv)
    # create search option and Button
    lineEdit = QLineEdit()
    searchButton = QPushButton("Search for coordinates")
    # Create Layout
    window = QWidget()
    window.setLayout(QVBoxLayout())
    # Create Qml reference
    view = QQuickWidget()
    view.setSource(QUrl('map.qml'))
    view.setMinimumSize(200, 200)
    view.setResizeMode(view.SizeRootObjectToView)
    rootObject = view.rootObject()
    # Add widgets to layout
    window.layout().addWidget(lineEdit)
    window.layout().addWidget(searchButton)
    window.layout().addWidget(view)
    window.setMinimumSize(500, 500)
    # Connect search slot
    searchButton.clicked.connect(lambda: search(lineEdit, rootObject))
    # Show the Layout
    window.show()
    # Execute the Application and Exit
    myApp.exec_()
    sys.exit()
