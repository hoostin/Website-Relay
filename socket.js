/*eslint-disable */
var exampleSocket = new WebSocket("wss://api.logicparkdev.com");

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
