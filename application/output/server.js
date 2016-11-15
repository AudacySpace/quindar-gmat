var app = require('express')();
var server = require('http').createServer(app);
var port = 3000
var io = require('socket.io').listen(app.listen(port, function(){
	console.log('Server listening at port %d', port);
}));

io.on('connection', function(socket){
	console.log('socket.io server connected.')

	socket.on('satData1', function(data){
		setData1 = data;
		console.log(setData1)
	});

});
