import QtQuick 2.1
import QtQuick.Window 2.0
import QtQuick.Controls 1.4
import QtLocation 5.6
import QtPositioning 5.6

Window {
    width: 512
    height: 512
    visible: true

    Plugin {
        id: mapPlugin
        name: "osm"
    }

    Map {
        id: map
        anchors.fill: parent
        plugin: mapPlugin
        center {
            latitude: g
            longitude: f
        }
        zoomLevel: 14
    }
}
