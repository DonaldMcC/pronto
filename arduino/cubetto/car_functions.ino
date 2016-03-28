//one wheel is composed of 32 slices
//16 black and 16 white.

void testmotors() {

  //forward left
  analogWrite(leftForward, 88);
  digitalWrite(leftReverse, LOW);
  delay(2000);
  stopLeft();
  delay(2000);
  analogWrite(rightForward, 88);
  digitalWrite(rightReverse, LOW);
  delay(2000);  
  stopRight();
}


//rotate wheels until the next sign
void initialize() {
  int vl = digitalRead(leftEncoder);

  //forward left
  analogWrite(leftForward, 88);
  digitalWrite(leftReverse, LOW);

  while (digitalRead(leftEncoder) == vl);

  stopLeft();
  delay(100);

  int vr = digitalRead(rightEncoder);

  //forward right
  analogWrite(rightForward, 88);
  digitalWrite(rightReverse, LOW);

  while (digitalRead(rightEncoder) == vr);
  stopRight();
}

/* MOTION FUNCTIONS */

void backward(int speed, int steps) {
  int vL, pvL = 0;
  int vR, pvR = 0;

  int counterL = 0, counterR = 0;

  //right backward
  digitalWrite(rightForward, LOW);
  analogWrite(rightReverse, speed);



  //left backward
  digitalWrite(leftForward, LOW);
  analogWrite(leftReverse, speed);


  while (counterL <= steps || counterR <= steps) {
    if (counterL <= steps) {
      vL = digitalRead(leftEncoder);
      if (vL != pvL) counterL++;
      pvL = vL;
    }
    else  {
    stopLeft();
    }
    if (counterR <= steps) {
      vR = digitalRead(rightEncoder);
      if (vR != pvR) counterR++;
      pvR = vR;
    }
    else  {
    stopRight();
    }
  }

  stop();
}

void forward(int speed, int steps) {
  int vL, pvL = 0;
  int vR, pvR = 0;

  int counterL = 0, counterR = 0;

  //left forward
  digitalWrite(leftForward, speed);
  analogWrite(leftReverse, LOW);

  //right forward
  digitalWrite(rightForward, speed);
  analogWrite(rightReverse, LOW);
  

  while (counterL <= steps || counterR <= steps) {
    if (counterL <= steps) {
      vL = digitalRead(leftEncoder);
      if (vL != pvL) counterL++;
      pvL = vL;
    }
    else {
      stopLeft();
    }
    if (counterR <= steps) {
      vR = digitalRead(rightEncoder);
      if (vR != pvR) counterR++;
      pvR = vR;
    }
        else {
      stopRight();
    }
  }

  stop();
}

void left(int speed, int steps) {
  int vL, pvL = 0;
  int vR, pvR = 0;

  int counterL = 0, counterR = 0;

  //right forward
  digitalWrite(rightForward, speed);
  analogWrite(rightReverse, LOW);

  //left backward
  digitalWrite(leftForward, LOW);
  analogWrite(leftReverse, speed);

  //count rotation
  while (counterL <= steps || counterR <= steps) {
    if (counterL <= steps) {
      vL = digitalRead(leftEncoder);
      if (vL != pvL) counterL++;
      pvL = vL;
    }
            else {
      stopLeft();
    }
    if (counterR <= steps) {
      vR = digitalRead(rightEncoder);
      if (vR != pvR) counterR++;
      pvR = vR;
    }
            else {
      stopRight();
    }
  }

  stop();
}

void right(int speed, int steps) {

  int vL, pvL = 0;
  int vR, pvR = 0;

  int counterL = 0, counterR = 0;

  pvL = digitalRead(leftEncoder);
  pvR = digitalRead(rightEncoder);

  //right reverse
  digitalWrite(rightForward, LOW);
  analogWrite(rightReverse, speed);

  //left forward
  digitalWrite(leftReverse, LOW);
  analogWrite(leftForward, speed);

  //count rotation
  while (counterL <= steps || counterR <= steps) {
    if (counterL <= steps) {
      vL = digitalRead(leftEncoder);
      if (vL != pvL) counterL++;
      pvL = vL;
    }
    else  {
    stopLeft();
    }
    if (counterR <= steps) {
      vR = digitalRead(rightEncoder);
      if (vR != pvR) counterR++;
      pvR = vR;
    }
    else  {
    stopRight();
    }
  }
  stop();
}

/* STOP FUNCTIONS */
void stopLeft() {
  digitalWrite(leftForward, LOW);
  digitalWrite(leftReverse, LOW);
}

void stopRight() {
  digitalWrite(rightForward, LOW);
  digitalWrite(rightReverse, LOW);
}

void stop() {
  stopLeft();
  stopRight();
}

void hardStop() {
  digitalWrite(leftForward, HIGH);
  digitalWrite(leftReverse, HIGH);

  digitalWrite(rightForward, HIGH);
  digitalWrite(rightReverse, HIGH);
}

