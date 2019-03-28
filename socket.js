const WebSocket = require('ws');

const ws = new WebSocket('wss://www.logicparkdev.com/ws');

ws.on('open', function open() {
  ws.send('ping');
});

ws.on('message', function incoming(data) {
  console.log(data);
});
