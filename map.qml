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
        objectName: "map"
        property double lat: 59.91
        property double lon: 10.75
        visible: true
        anchors.fill: parent
        plugin: mapPlugin
        center {
            latitude: lat
            longitude: lon
        }
        zoomLevel: 14

        MapQuickItem {
            id: marker
            objectName: "marker"
            visible: false
            anchorPoint.x: 0.5 * image.width
            anchorPoint.y: image.height
            sourceItem: Image {
                id: image
                source: "image.png"
            }
        }
    }
}
