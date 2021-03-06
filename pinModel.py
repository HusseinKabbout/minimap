import sys
import re
import untangle
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtQml import *
from PyQt5.QtQuickWidgets import *
from PyQt5.QtPositioning import *
from PyQt5.QtGui import *


class MarkerItem():
    def __init__(self, position, title):
        self._position = position
        self._title = title

    def position(self):
        return self._position

    def setPosition(self, value):
        self._position = value

    def title(self):
        return self._title

    def setTitle(self, value):
        self._title = value


class MarkerModel(QAbstractListModel):
    PositionRole = Qt.UserRole
    TitleRole = Qt.UserRole + 1

    _roles = {PositionRole: QByteArray(
        b"markerPosition"), TitleRole: QByteArray(b"markerTitle")}

    def __init__(self, parent=None):
        QAbstractListModel.__init__(self, parent)
        self._markers = []

    def rowCount(self, index=QModelIndex()):
        return len(self._markers)

    def roleNames(self):
        return self._roles

    def data(self, index, role=Qt.DisplayRole):
        if index.row() >= self.rowCount():
            return QVariant()
        marker = self._markers[index.row()]

        if role == MarkerModel.PositionRole:
            return marker.position()

        elif role == MarkerModel.TitleRole:
            return marker.title()

        return QVariant()

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid():
            marker = self._markers[index.row()]
            if role == MarkerModel.PositionRole:
                marker.setPosition(value)

            if role == MarkerModel.TitleRole:
                marker.setTitle(value)

            self.dataChanged.emit(index, index)
            return True
        return QAbstractListModel.setData(self, index, value, role)

    def addMarker(self, marker):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._markers.append(marker)
        self.endInsertRows()

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        return QAbstractListModel.flags(index) | Qt.ItemIsEditable
