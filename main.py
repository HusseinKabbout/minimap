import sys
import re
import untangle
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtQml import *
from PyQt5.QtQuickWidgets import *
from PyQt5.QtPositioning import *
from pain import *
import xml.etree.ElementTree as ET


def selectColor(comboBox, rootObject):
    selected = comboBox.currentText()
    paintObject = rootObject.findChild(QObject, "paint")
    paintObject.setProperty("lineColor", selected)


def openList(listEdit, rootObject):
    fileName = QFileDialog.getOpenFileName(
        None, "Open", "/home", "Only Xml(*.xml)")
    listEdit.setText(fileName[0])
    url = listEdit.text()
    if url:
        if checkBox.isChecked():
            i = 0
            titl = []
            tree = ET.parse(url)
            root = tree.getroot()
            for elem in root.findall('.//{'
                                     'http://ogr.maptools.org/}Name'):
                titl.append(elem.text)
            for elem in root.findall('.//{'
                                     'http://www.opengis.net/gml}coordinates'):
                coord = []
                coord.append(elem.text)
                for elem in coord:
                    part = elem.split(",")
                    lati = part[0]
                    longi = part[1]
                    model.addMarker(
                        MarkerItem(QPointF(
                            float(lati), float(longi)), titl[i]))
                    mapObject = rootObject.findChild(QObject, "mapboxgl")
                    mapObject.setProperty("zoomLevel", 2)
                    i = i + 1
        else:
            XML = url
            parXml = untangle.parse(XML)
            for item in parXml.items.item:
                titl = item.title.cdata
                lati = item.latitude.cdata
                longi = item.longitude.cdata
                model.addMarker(
                    MarkerItem(QPointF(float(lati), float(longi)), titl))
            mapObject = rootObject.findChild(QObject, "mapboxgl")
            mapObject.setProperty("zoomLevel", 2)


def search(lineEdit, rootObject):
    try:
        f = re.match(
            r'^([+-]?\d+\.?\d*),?\s+([+-]?\d+\.?\d*)$', lineEdit.text())
        if float(f[1]) <= 90 and float(f[2]) <= 180:
            lat = float(f[1])
            lon = float(f[2])
        mapObject = rootObject.findChild(QObject, "mapboxgl")
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
    # create color_list
    colors = []
    colors.append("blue")
    colors.append("red")
    colors.append("yellow")
    colors.append("black")
    colors.append("white")
    # create gui
    lineEdit = QLineEdit()
    searchButton = QPushButton()
    searchButton.resize(searchButton.sizeHint())
    icon = QIcon()
    icon.addPixmap(QPixmap(
        "icons/searchIcon.png"), QIcon.Normal, QIcon.Off)
    searchButton.setIcon(icon)
    listEdit = QLineEdit()
    listButton = QPushButton()
    listButton.resize(listButton.sizeHint())
    icon = QIcon()
    icon.addPixmap(QPixmap(
        "icons/listsearchIcon.png"), QIcon.Normal, QIcon.Off)
    listButton.setIcon(icon)
    comboBox = QComboBox()
    comboBox.addItems(colors)
    selectColorBtn = QPushButton()
    selectColorBtn.resize(selectColorBtn.sizeHint())
    icon = QIcon()
    icon.addPixmap(QPixmap(
        "icons/changecolorIcon.png"), QIcon.Normal, QIcon.Off)
    selectColorBtn.setIcon(icon)
    checkBox = QCheckBox("import GML")
    # Create Layout
    window = QWidget()
    window.setLayout(QVBoxLayout())
    controlS = QWidget()
    controlS.setLayout(QHBoxLayout())
    controlS.setMaximumSize(495, 50)
    controlX = QWidget()
    controlX.setLayout(QHBoxLayout())
    controlX.setMaximumSize(495, 50)
    jsonLine = QWidget()
    jsonLine.setLayout(QHBoxLayout())
    jsonLine.setMaximumSize(495, 50)
    # Create Qml reference and create new Model
    view = QQuickWidget()
    model = MarkerModel()
    context = view.rootContext()
    context.setContextProperty('markerModel', model)
    view.setSource(QUrl('map.qml'))
    view.setMinimumSize(200, 200)
    view.setResizeMode(view.SizeRootObjectToView)
    rootObject = view.rootObject()
    # Add widgets to layout
    controlS.layout().addWidget(lineEdit)
    controlS.layout().addWidget(searchButton)
    controlX.layout().addWidget(listEdit)
    controlX.layout().addWidget(listButton)
    controlX.layout().addWidget(checkBox)
    jsonLine.layout().addWidget(comboBox)
    jsonLine.layout().addWidget(selectColorBtn)
    window.layout().addWidget(controlS)
    window.layout().addWidget(controlX)
    window.layout().addWidget(jsonLine)
    window.layout().addWidget(view)
    window.setMinimumSize(500, 500)
    # Connect search slot
    searchButton.clicked.connect(lambda: search(lineEdit, rootObject))
    lineEdit.returnPressed.connect(lambda: search(lineEdit, rootObject))
    listButton.clicked.connect(lambda: openList(listEdit, rootObject))
    selectColorBtn.clicked.connect(lambda: selectColor(comboBox, rootObject))
    # Show the Layout
    window.setWindowTitle("Minimap")
    window.show()
    # Execute the Application and Exit
    myApp.exec_()
    sys.exit()
