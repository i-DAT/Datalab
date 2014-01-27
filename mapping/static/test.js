console.log('hi');



    

    


//client = new Messaging.Client("146.185.174.52", 80, "datalabwebtest");
client = new Messaging.Client("test.mosquitto.org", 80, "datalabwebtest");
    function onConnectionLost(responseObject) {
      if (responseObject.errorCode !== 0)
        console.log("onConnectionLost:"+responseObject.errorMessage);
    };
    function onMessageArrived(message) {
      console.log("onMessageArrived:"+message.payloadString);
      //alert("onMessageArrived:"+message.payloadString);
      //client.disconnect(); 
    }

  function onConnect() {
      // Once a connection has been made, make a subscription and send a message.
      console.log("onConnect");
      client.subscribe("datalab/test");
      //message = new Messaging.Message("Hello");
      //message.destinationName = "/World";
      //client.send(message);
    }

  function onFail(){
      console.log("failed");
    }

    //client.disconnect();
    client.onConnectionLost = onConnectionLost;
    client.onMessageArrived = onMessageArrived;
    client.connect({onSuccess:onConnect, onFailure: onFail });

    

    
