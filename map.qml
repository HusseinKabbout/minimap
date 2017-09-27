import QtQuick 2.0
import QtQuick.Window 2.0
import QtLocation 5.5
import QtPositioning 5.5

Item {
    id: myItem
    property int marker_size: 16
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
        MapItemView {
            id: markerSec
            model: markerModel
            objectName: "secMarker"
            property var titl
            delegate: MapQuickItem{
                anchorPoint: Qt.point(2.5, 2.5)
                coordinate: QtPositioning.coordinate(markerPosition.x, markerPosition.y)
                zoomLevel: 0
                sourceItem: Column{
                        Image {id: imag; source: "image.png"}
                        Text {text: "" + markerSec.titl; font.bold: true}
                }
            }
        }
    }
}
