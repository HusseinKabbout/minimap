import QtQuick 2.0
import QtLocation 5.6
import QtPositioning 5.6
import QtQuick.XmlListModel 2.0

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

    XmlListModel {
        id: xmlModel
        source: "coordinates.xml"
        query: "/rss/channel/item"

        XmlRole { name: "title"; query: "title/string()" }
        XmlRole { name: "coordinate"; query: "coordinate/string()" }
    }

    ListView {
    width: 180; height: 300
    model: xmlModel
    delegate: Text { text: title + ": " + coordinate }
    }
}
