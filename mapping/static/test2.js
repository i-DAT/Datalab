var exampleSocket = new WebSocket("ws://146.185.174.52:8080/datalab/map/stream");

exampleSocket.onmessage = function (event) {
  payload = JSON.parse(event.data);
  console.log(payload);
  //parse the payload and update a map
};