var prompt = require('prompt');
var promptAnswer = "";

var
var SerialPort =  serialport.serialPort;

prompt.start();

function termInput(){
	prompt.get(['hello'], function (err, result){
		if (err) done();
		else {
			promptAnswer = 	hello.result;
		}


	});

	console.log(promptAnswer);
}

termInput();

