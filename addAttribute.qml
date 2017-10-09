import QtQuick 2.2
import QtQuick.Layouts 1.1
import QtQuick.Window 2.0
import QtQuick.Controls 2.2
import QtLocation 5.9
import QtPositioning 5.5
import QtQuick.LocalStorage 2.0 as Sql

Window {
    id: mypopDialog
    title: "Set Attributes"
    width: 450
    height: 150
    flags: Qt.Dialog
    modality: Qt.WindowModal
    property var sqlPosition
    GridLayout{
        rowSpacing: 12
        columnSpacing: 30
        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.margins: 30
        Label {
            text: "Your Name"
        }
        TextField {
            id: text
            placeholderText: qsTr("Enter name")
        }
        Button {
            text: "Submit"
            onClicked: {
                var db = Sql.LocalStorage.openDatabaseSync("db_attr", "1.0", "DB for Storing Attributes!", 1000000)
                db.transaction(
                    function(tx) {
                    tx.executeSql("CREATE TABLE IF NOT EXISTS Pin(ID INTEGER PRIMARY KEY AUTOINCREMENT, Name VARCHAR(255), Latitude FLOAT, Longitude FLOAT, unique (Name))")
                    tx.executeSql("INSERT INTO Pin VALUES(NULL, ?, ?, ?)", [text.text, (mypopDialog.sqlPosition.latitude).toFixed(3), (mypopDialog.sqlPosition.longitude).toFixed(3) ])
                    var print = tx.executeSql("SELECT * FROM Pin")
                    for(var i = 0; i < print.rows.length; i++) {
                        var dbItem = print.rows.item(i)
                    console.warn("ID: " + dbItem.ID + ", Name: " + dbItem.Name + ", Latitude: " + dbItem.Latitude + ", Longitude: " + dbItem.Longitude )
                        }
                    }
                )
                mypopDialog.close()
            }
        }
    }
    Button{
        text: "Close"
        x: 342
        y: 100
        onClicked: mypopDialog.close()
    }
}
