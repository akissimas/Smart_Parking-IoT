# Smart Parking - IoT

## Summary

The project we chose is about Smart Parking, with the use of a sonar and a Raspberry PI we can determine if a car is parked at a certain location.

## Hardware Prerequisites

For the project we need:

- 1kΩ Resistance
- 2kΩ Resistance
- Ultrasonic Sensor HC-SR04
- Breadboard
- Raspberry PI
- A few jumper wires for the connections to the Breadboard and the Raspberry PI

## Connection to the Raspberry PI

<p align = "center">
	<img src = "./img/raspi.png">
</p>
<p align = "center">
	Fig.1 Sonar - Breadbroad - Raspberry Connection
</p>

We need the resistances to create a voltage divider, so that the Sonar and the Raspberry PI can work correctly.

## Software Requirements

All of the Software requirements exist in the raspberry_pi file as requirements.txt and in the smart_parking directory as package.json. 

You can install the Python packages with this command:

```bash
python3 -m pip install -r requirements.txt
```

You can install the NodeJs module with this command:

```bash
npm install
```

## Brief Description
1. The Sonar sends a signal back to the Raspberry PI.
2. The Raspberry PI determines if the Parking Spot is taken or not and sends, using Wi-fi, the correct data to a Mongo Database.
3. After that the website or the Android App collects the latest entry in the Mongo Database and shows the user the state of the Parking Spot.


## Architecture

<p align = "center">
	<img src = "./img/iot-architecture.png">
</p>
<p align = "center">
	Fig.2 Architecture
</p>


## How to Run the Project

- Step 1. Download the project as a zip, or simply clone the git repository.
- Step 2. Configure your Raspberry Pi.
- Step 3. Set-up your Breadboard with the Raspberry Pi.
- Step 4. Install all the Python libraries with this command: 
	```bash
	python3 -m pip install -r requirements.txt
	```
- Step 5. Install NodeJS on your Raspberry Pi or on your PC, you can download it from here https://nodejs.org/en/.
- Step 6. Install all the necessary packages for NodeJS with this command:
	```bash
	npm install
	```
- Step 7. Create an account for MongoDB Atlas at https://www.mongodb.com/atlas/database.
- Step 8. Create a Cluster and a Database at MongoDB Atlas.
- Step 9. Set-up enviroment passwords for your Database, both for your NodeJS file and the Python file.
- Step 10. Download the Android project, or simply clone the git repository from here .
- Step 11. Go to the MainActivity.java and at line 27, change the current IP address to your IP adress and port you will be using.
- Step 12. First run the Python file. After that you run the NodeJS file, finally you can run the Android Studio. You can run the NodeJS file with following command:
	```bash
	node index.js
	```
- Step 13. You can open the webpage or the Android Studio to see if the changes actually come through.
