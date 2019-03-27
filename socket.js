/*eslint-disable */
var WebSocket = require('ws');
var exampleSocket = new WebSocket("ws://ec2-1.logicparkdev.com:8000/ws");

exampleSocket.onmessage = function(event) {
  var color = "";
  var parkingSpot = JSON.parse(event.data);
  var occupancyStatus = Boolean;

    if (occupancyStatus == true) {
        color = "red";
    }else{
        color = "green";
    }

    document.getElementById("rect").style.fill = color;
};
