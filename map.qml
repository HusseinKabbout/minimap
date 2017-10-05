import QtQuick 2.0
import QtQuick.Controls 2.2
import QtQuick.Window 2.0
import QtLocation 5.9
import QtPositioning 5.5
import QtQuick.LocalStorage 2.0 as Sql


Item {
    id: myItem

    Plugin {
        id: mapPlugin
        name: "mapboxgl"
    }

    Map {
        id: map
        objectName: "mapboxgl"
        property double lat: 47.368649
        property double lon: 8.5391825
        visible: true
        anchors.fill: parent
        plugin: mapPlugin
        center {
            latitude: lat
            longitude: lon
        }
        zoomLevel: 14

        ListView {
            height: 1
            model: map
            delegate: Text {
                text: "Latitude: " + (center.latitude).toFixed(3) + " Longitude: " + (center.longitude).toFixed(3)
                }
            }

            MouseArea{
                id: mouseArea
                property var positionRoot: map.toCoordinate(Qt.point(mouseX, mouseY))
                anchors.fill: parent
                onClicked: {
                    var db = Sql.LocalStorage.openDatabaseSync("db_attr", "1.0", "DB for Storing Attributes!", 1000000)
                    db.transaction(
                        function(tx) {
                        tx.executeSql("CREATE TABLE IF NOT EXISTS Pin(ID INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR(255), Latitude FLOAT, Longitude FLOAT)")
                        tx.executeSql("INSERT INTO Pin VALUES(NULL, ?, ?, ?)", ["Hussein", (positionRoot.latitude).toFixed(3), (positionRoot.longitude).toFixed(3) ])
                        var print = tx.executeSql("SELECT * FROM Pin")
                        for(var i = 0; i < print.rows.length; i++) {
                            var dbItem = print.rows.item(i)
                        console.warn("ID: " + dbItem.ID + ", Name: " + dbItem.Name + ", Latitude: " + dbItem.Latitude + ", Longitude: " + dbItem.Longitude )
                            }
                        }
                    )
                }
            }

        MapQuickItem {
            id: marker
            objectName: "marker"
            visible: false
            anchorPoint.x: 0.5 * image.width
            anchorPoint.y: image.height
            sourceItem: Image {
                id: image
                source: "image.png"
                MouseArea{
                    anchors.fill: parent
                    onClicked: {
                        ToolTip.timeout = 2000
                        ToolTip.visible = true
                        ToolTip.text = qsTr("Coordinates: %1, %2").arg(marker.coordinate.latitude).arg(marker.coordinate.longitude)
                    }
                }
            }
        }

        MapItemView {
            model: markerModel
            delegate: MapQuickItem{
                anchorPoint: Qt.point(2.5, 2.5)
                coordinate: QtPositioning.coordinate(markerPosition.x, markerPosition.y)
                zoomLevel: 0
                sourceItem: Column{
                        Image {
                            id: imag
                            source: "image.png"
                            MouseArea{
                                anchors.fill: parent
                                onClicked: {

                                    ToolTip.timeout = 2000
                                    ToolTip.visible = true
                                    ToolTip.text = qsTr("Coordinates: %1, %2".arg(markerPosition.x).arg(markerPosition.y))
                                }
                            }
                        }

                        Text {
                            text: markerTitle
                            font.bold: true
                        }
                }
            }
        }
        MapParameter {
        type: "source"
        property var name: "coordinates"
        property var sourceType: "geojson"
        property var data: '{ "type": "FeatureCollection", "features": \
            [{ "type": "Feature", "properties": {}, "geometry": { \
            "type": "LineString", "coordinates": [[ 8.541484, \
            47.366850 ], [8.542171, 47.370018],[8.545561, 47.369233]]}}]}'
        }

        MapParameter {
            type: "layer"
            property var name: "layer"
            property var layerType: "line"
            property var source: "coordinates"
            property var before: "road-label-small"
        }

        MapParameter {
            objectName: "paint"
            type: "paint"
            property var layer: "layer"
            property var lineColor: "black"
            property var lineWidth: 8.0
        }

        MapParameter {
            type: "layout"
            property var layer: "layer"
            property var lineJoin: "round"
            property var lineCap: "round"
        }
    }
}
