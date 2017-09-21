import QtQuick 2.0
import QtLocation 5.6
import QtPositioning 5.6

Item {
    id: myItem
    Plugin {
        id: mapPlugin
        name: "osm"
    }

    Map {
        id: map
        property var ipn: la
        property var bpn: lo
        visible: true
        anchors.fill: parent
        plugin: mapPlugin
        center {
            latitude: (map.ipn != undefined) ? map.ipn : 59.91
            longitude: (map.bpn != undefined) ? map.bpn : 10.75
        }
        zoomLevel: 14

        MapQuickItem {
            id: marker
            anchorPoint.x: image.width
            anchorPoint.y: image.height
            coordinate {
                latitude: (map.ipn != undefined) ? map.ipn : 59.91
                longitude: (map.bpn != undefined) ? map.bpn : 10.75
            }
            sourceItem: Image {
                id: image
                source: "/home/hka/Documents/minimap/image.png"
            }
        }
    }
}
