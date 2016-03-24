/*
http://primo.io

This sketch is part of the Primo Prototype Documentation.
http://docs.primo.io

Tested on the Arduino UNO.
Load this into Cubetto, the little cube robot.
*/

#define FORWARD 1
#define BACKWARD 0

//serial protocol
#define STOP 'O'
#define INIT 'I'

//standard setup
#define LEFT 'L'
#define RIGHT 'R'
#define FORWARD 'F'
#define BACKWARD 'B'


//left motor
const int leftEnable = 13;
const int leftForward = 11;
const int leftReverse = 10;

//right motor
const int rightEnable = 12;
const int rightForward = 9;  /reverse from std
const int rightReverse = 5;  //change from std as pin not avail

//encoders
const int leftEncoder = A1;
const int rightEncoder = A4;

char instruction = '0';

void setup() {

  Serial.begin(9600);

  //initialize left
  pinMode(leftEnable, OUTPUT);
  pinMode(leftReverse, OUTPUT);
  pinMode(leftForward, OUTPUT);

  //initialize right
  pinMode(rightEnable, OUTPUT);
  pinMode(rightForward, OUTPUT);
  pinMode(rightReverse, OUTPUT);

  //enable motors
  digitalWrite(leftEnable, HIGH);
  digitalWrite(rightEnable, HIGH);

  //initialize aligns the wheels
  initialize();

  delay(2000);
}

void loop() {

  //read from the xbee
  if (Serial.available() > 0) {
    instruction = Serial.read();
  }

  //decode instruction
  switch (instruction) {    

    case FORWARD:
      initialize();
      forward(128, 16);
      break;
      
    case BACKWARD:
      initialize();
      backward(128, 16);
      break;

    case LEFT:
      initialize();
      left(128, 9);
      break;

    case RIGHT:
      initialize();
      right(128, 9);
      break;

    case INIT:
      initialize();
      break;
  
    case STOP:
      stop();
      break;

    default:
      stop();
      break;
  }
  instruction = '0';
}






