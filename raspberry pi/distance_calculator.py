# Libraries
import RPi.GPIO as GPIO
import time
import os
from pymongo import MongoClient
from dotenv import load_dotenv

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 23  # pin 16 / GPIO 23
GPIO_ECHO = 24 # pin 18 / GPIO 24

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
	# set Trigger to HIGH
	GPIO.output(GPIO_TRIGGER, True)

	# set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)

	StartTime = time.time()
	StopTime = time.time()

	# save StartTime
	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()
 
	# save time of arrival
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()
 
	# time difference between start and arrival
	TimeElapsed = StopTime - StartTime

	# multiply with the sonic speed (34300 cm/s)
	# and divide by 2, because there and back
	Distance = (TimeElapsed * 34300) / 2
 
	return Distance

if __name__ == '__main__':
	# Load config from a .env file:
	load_dotenv()
	MONGODB_URI = os.environ['MONGODB_URI']
	client = MongoClient(MONGODB_URI)
	db = client.get_database("Demo")
	collection = db.get_collection("Timestamp")
	try:
		parked_flag = False
		while True:
			dist = distance()
			
			if (dist < 50 and parked_flag == False):
				parking_time = time.time()
				local_time = time.ctime(parking_time)
				parked_flag = True
				# Send local time to db.
				print ("\nMeasured Distance = {:.1f} cm".format(dist))
				print ("Local time: ", local_time)
				data = { "parking_id" : 0, "parked" : parked_flag, "timestamp" : local_time }
				x = collection.insert_one(data)
				
			elif (dist > 50 and parked_flag == True):
				unparked_time = time.time()
				local_time = time.ctime(unparked_time)
				parked_flag = False
				# Send local time to db.
				print ("\nMeasured Distance = {:.1f} cm".format(dist))
				print ("Local time: ", local_time)
				data = { "parking_id" : 0, "parked" : parked_flag, "timestamp" : local_time }
				x = collection.insert_one(data)
				
			time.sleep(1)
	
	# Reset by pressing CTRL + C
	except KeyboardInterrupt:
		print("\nMeasurement stopped by User")
		client.close()
		GPIO.cleanup()