const WebSocket = require('ws');

const ws = new WebSocket('wws://ec2-1.logicparkdev.com:8000/ws');

ws.on('open', function open() {
  ws.send('ping');
});

ws.on('message', function incoming(data) {
  console.log(data);
});
