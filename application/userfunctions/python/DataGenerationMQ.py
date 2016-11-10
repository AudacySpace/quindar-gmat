import pika
import json
import base64

def SendMQ(x1,y1,z1,vx1,vy1,vz1,x2,y2,z2,vx2,vy2,vz2,x3,y3,z3,vx3,vy3,vz3,q1_1,q2_1,q3_1,q4_1,
q1_2,q2_2,q3_2,q4_2,q1_3,q2_3,q3_3,q4_3,time):
        #load systemSettings
	f = open('../userfunctions/python/systemSettings.txt','r')
	header = f.readline()
	data = f.readline()
	exchangeName,keyName,exchangeType,URLParam = data.split(',')
	f.closed
	#y=sys.version_info
	exchange_name = exchangeName
	key_name = keyName
	params = pika.URLParameters(URLParam.rstrip())
	params.socket_timeout = 5 
	connection = pika.BlockingConnection(params)
	channel = connection.channel()
	
	channel.exchange_declare(exchange=exchangeName,durable=True,type=exchangeType)

	timestamp = (time+2430000-2440587.5)*86400.0
	testData1 = json.dumps({ "vehicleId": "Audacy1", "x": x1, "y": y1, "z": z1, "vx": vx1, 
		"vy": vy1, "vz": vz1, "timestamp": timestamp }, sort_keys=True)
	testData2 = json.dumps({ "vehicleId": "Audacy2", "x": x2, "y": y2, "z": z2, "vx": vx2, 
		"vy": vy2, "vz": vz2, "timestamp": timestamp }, sort_keys=True)
	testData3 = json.dumps({ "vehicleId": "Audacy3", "x": x3, "y": y3, "z": z3, "vx": vx3, 
		"vy": vy3, "vz": vz3, "timestamp": timestamp }, sort_keys=True)	
	
	# Encode #
	Data1 = base64.b64encode(bytes(testData1,"utf-8"))
	Data2 = base64.b64encode(bytes(testData2,"utf-8"))
	Data3 = base64.b64encode(bytes(testData3,"utf-8"))
	channel.basic_publish(exchange = exchange_name,
                      routing_key = key_name,
                      body = Data1)
	channel.basic_publish(exchange = exchange_name,
                      routing_key = key_name,
                      body = Data2)
	channel.basic_publish(exchange = exchange_name,
                      routing_key = key_name,
                      body = Data3)
					  
	#print(" [x] Sent 'connected'")
	#connection.close()
