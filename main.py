import sys
import re
import untangle
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtQml import *
from PyQt5.QtQuickWidgets import *
from PyQt5.QtPositioning import *


def openList(lineEdit, rootObject):
    fileName = QFileDialog.getOpenFileName(
        None, "Open", "/home", "Only Xml(*.xml)")
    listEdit.setText(fileName[0])
    url = listEdit.text()
    if url:
        XML = '/home/hka/Documents/minimap/coordinates.xml'
        o = untangle.parse(XML)
        secObject = rootObject.findChild(QObject, "secMarker")
        for item in o.rss.channel.item:
            titl = item.title.cdata
            lati = item.latitude.cdata
            longi = item.longitude.cdata
            secObject.setProperty("titl", titl)
            secObject.setProperty("coordinate", QGeoCoordinate(
                float(lati), float(longi)))
        secObject.setProperty("visible", True)


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
    except Exception:
        QMessageBox.warning(None, "Invalid Coordinate", "Invalid coordinate")
        lineEdit.selectAll()


# Main Function
if __name__ == '__main__':
    # Create main app
    myApp = QApplication(sys.argv)
    # create search option and Button
    lineEdit = QLineEdit()
    searchButton = QPushButton("Search for coordinates")
    listEdit = QLineEdit()
    listButton = QPushButton("Open List of coordinates")
    # Create Layout
    window = QWidget()
    window.setLayout(QVBoxLayout())
    # Create Qml reference
    view = QQuickWidget()
    view.setSource(QUrl('qml.qml'))
    view.setMinimumSize(200, 200)
    view.setResizeMode(view.SizeRootObjectToView)
    rootObject = view.rootObject()
    # Add widgets to layout
    window.layout().addWidget(lineEdit)
    window.layout().addWidget(searchButton)
    window.layout().addWidget(listEdit)
    window.layout().addWidget(listButton)
    window.layout().addWidget(view)
    window.setMinimumSize(500, 500)
    # Connect search slot
    searchButton.clicked.connect(lambda: search(lineEdit, rootObject))
    listButton.clicked.connect(lambda: openList(lineEdit, rootObject))
    # Show the Layout
    window.show()
    # Execute the Application and Exit
    myApp.exec_()
    sys.exit()
