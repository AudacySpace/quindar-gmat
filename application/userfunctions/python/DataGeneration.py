import os
import sys
import json
import math
from socketIO_client import SocketIO, LoggingNamespace
from datetime import datetime
global com_name, com_type, com_value, com_time, com_localTime, com_localTimeString

# ('https://qsvr.quindar.space', 443, LoggingNamespace, verify=False)
socketIO = SocketIO('https://qsvr.quindar.space', 443, LoggingNamespace, verify=False)
missionData = {"mission" : "ATest"}
com_name = ""
com_value = ""
com_time = ""
com_localTime = ""
com_localTimeString = ""

def connect():
	socketIO.emit("add-mission", missionData)

def testCommand(*args):
	global com_name, com_type, com_value, com_time
	for arg in args:
		com_cmd = arg["metadata"]["cmd"]
		com_arg = arg["metadata"]["arg"]
		com_time = arg["timestamp"]
		com_data = ""
	com_localTime = datetime.utcnow()
	com_localTimeString = com_localTime.__str__()
	commandResponse = json.dumps({"mission":"ATest","timestamp":com_localTimeString,"metadata":{"status":"Success","data":"N/A","sent_timestamp":com_time},"data":""}, sort_keys=True)
	socketIO.emit('comm-ack',commandResponse)


# platform.audacy.space with port 7904
def Generate(x1,y1,z1,vx1,vy1,vz1,x2,y2,z2,vx2,vy2,vz2,x3,y3,z3,vx3,vy3,vz3,q1_1,q2_1,q3_1, q4_1,
q1_2,q2_2,q3_2,q4_2,q1_3,q2_3,q3_3,q4_3,time):
	#y=sys.version_info
	f = open('../userfunctions/python/clientSettings.txt','r')
	header = f.readline()
	data = f.readline()
	endPoint, dbPort, port = data.split(',')
	f.closed
	timestamp = (time+2430000-2440587.5)*86400.0
	with SocketIO(endPoint, int(port), LoggingNamespace) as socketIO:
		testData1 = json.dumps({ "type": "position", "subtype": "Audacy1",
		"data": {"x": x1, "y": y1, "z": z1, "vx": vx1,"vy": vy1, "vz": vz1, 
		"timestamp": timestamp }}, sort_keys=True)
		testData2 = json.dumps({ "type": "position", "subtype": "Audacy2", 
		"data": {"x": x2, "y": y2, "z": z2, "vx": vx2, "vy": vy2, "vz": vz2, 
		"timestamp": timestamp }}, sort_keys=True)
		testData3 = json.dumps({ "type": "position", "subtype": "Audacy3", 
		"data": {"x": x3, "y": y3, "z": z3, "vx": vx3, "vy": vy3, "vz": vz3, 
		"timestamp": timestamp }}, sort_keys=True)	

		attiData1 = json.dumps({ "type": "attitude", "subtype": "Audacy1", 
		"data": {"q1": q1_1, "q2": q2_1, "q3": q3_1, "q4": q4_1, 
		"timestamp": timestamp }}, sort_keys=True)	
		attiData2 = json.dumps({ "type": "attitude", "subtype": "Audacy2", 
		"data": {"q1": q1_2, "q2": q2_2, "q3": q3_2, "q4": q4_2, 
		"timestamp": timestamp }}, sort_keys=True)	
		attiData3 = json.dumps({ "type": "attitude", "subtype": "Audacy3", 
		"data": {"q1": q1_3, "q2": q2_3, "q3": q3_3, "q4": q4_3, 
		"timestamp": timestamp }}, sort_keys=True)		
		socketIO.emit('position', testData1)
		socketIO.emit('position', testData2)
		socketIO.emit('position', testData3)
		socketIO.emit('attitude', attiData1)
		socketIO.emit('attitude', attiData2)
		socketIO.emit('attitude', attiData3)		
		socketIO.wait(seconds=1)
		return testData1

def Generate_v1_old(x1,y1,z1,vx1,vy1,vz1,x2,y2,z2,vx2,vy2,vz2,x3,y3,z3,vx3,vy3,vz3,q1_1,q2_1,q3_1, q4_1,
q1_2,q2_2,q3_2,q4_2,q1_3,q2_3,q3_3,q4_3,gs1_x,gs1_y,gs1_z,gs2_x,gs2_y,gs2_z,time):
	timestamp = time+2430000
	with SocketIO('https://qsvr.quindar.space', 443, LoggingNamespace) as socketIO:
		r1 = math.sqrt(math.pow(gs1_x,2)+math.pow(gs1_y,2)+math.pow(gs1_z,2))
		longitude1 = math.atan2(gs1_y,gs1_x)/math.pi*180
		latitude1 = math.asin(gs1_z/r1)/math.pi*180

		r2 = math.sqrt(math.pow(gs2_x,2)+math.pow(gs2_y,2)+math.pow(gs2_z,2))
		longitude2 = math.atan2(gs2_y,gs2_x)/math.pi*180
		latitude2 = math.asin(gs2_z/r2)/math.pi*180

		testData1 = json.dumps({ "vehicleId": "Audacy1", "x": x1, "y": y1, "z": z1,
		 "vx": vx1,"vy": vy1, "vz": vz1, "timestamp": timestamp, "stationId": "EarthStation1", 
		 "latitude": latitude1, "longitude": longitude1, "q1": q1_1, "q2": q2_1,
		 "q3": q3_1, "qc": q4_1}, sort_keys=True)
		
		testData2 = json.dumps({ "vehicleId": "Audacy2", "x": x2, "y": y2, "z": z2,
		 "vx": vx2,"vy": vy2, "vz": vz2, "timestamp": timestamp, "stationId": "EarthStation1", 
		 "latitude": latitude1, "longitude": longitude1, "q1": q1_2, "q2": q2_2,
		 "q3": q3_2, "qc": q4_2 }, sort_keys=True)

		testData3 = json.dumps({ "vehicleId": "Audacy3", "x": x3, "y": y3, "z": z3,
		 "vx": vx3,"vy": vy3, "vz": vz3, "timestamp": timestamp, "stationId": "EarthStation1", 
		 "latitude": latitude1, "longitude": longitude1, "q1": q1_3, "q2": q2_3,
		 "q3": q3_3, "qc": q4_3 }, sort_keys=True)
		
		socketIO.emit("satData1", testData1)
		socketIO.emit("satData1", testData2)
		socketIO.emit("satData1", testData3)	
		socketIO.wait(seconds=1)
		return testData1

def Generate_v1(x1,y1,z1,vx1,vy1,vz1,x2,y2,z2,vx2,vy2,vz2,x3,y3,z3,vx3,vy3,vz3,q1_1,q2_1,q3_1, q4_1,
q1_2,q2_2,q3_2,q4_2,q1_3,q2_3,q3_3,q4_3,gs1_x,gs1_y,gs1_z,gs2_x,gs2_y,gs2_z,time):
	timestamp = (time+2430000-2440587.5) * 86400 * 1000 # Modified Julian date to unix time [millisec] 

	testData1 = json.dumps({"mission": "ATest", "timestamp": timestamp,"data": {
		"Audacy1_GNC_position_x": x1,
		"Audacy1_GNC_position_y": y1,
		"Audacy1_GNC_position_z": z1,
		"Audacy1_GNC_velocity_vx": vx1,
		"Audacy1_GNC_velocity_vy": vy1,
		"Audacy1_GNC_velocity_vz": vz1,
		"Audacy1_GNC_attitude_q1": q1_1,
		"Audacy1_GNC_attitude_q2": q2_1,
		"Audacy1_GNC_attitude_q3": q3_1,
		"Audacy1_GNC_attitude_qc": q4_1,
		"Audacy2_GNC_position_x": x2,
		"Audacy2_GNC_position_y": y2,
		"Audacy2_GNC_position_z": z2,
		"Audacy2_GNC_velocity_vx": vx2,
		"Audacy2_GNC_velocity_vy": vy2,
		"Audacy2_GNC_velocity_vz": vz2,
		"Audacy2_GNC_attitude_q1": q1_2,
		"Audacy2_GNC_attitude_q2": q2_2,
		"Audacy2_GNC_attitude_q3": q3_2,
		"Audacy2_GNC_attitude_qc": q4_2,
		"Audacy3_GNC_position_x": x3,
		"Audacy3_GNC_position_y": y3,
		"Audacy3_GNC_position_z": z3,
		"Audacy3_GNC_velocity_vx": vx3,
		"Audacy3_GNC_velocity_vy": vy3,
		"Audacy3_GNC_velocity_vz": vz3,
		"Audacy3_GNC_attitude_q1": q1_3,
		"Audacy3_GNC_attitude_q2": q2_3,
		"Audacy3_GNC_attitude_q3": q3_3,
		"Audacy3_GNC_attitude_qc": q4_3,
		}}, sort_keys=True)
		
	socketIO.emit("satData1", testData1)
	socketIO.wait(seconds=1)
	return testData1

socketIO.on("connect", connect)
socketIO.on("reconnect", connect)

socketIO.on("command", testCommand)
