const int in1 = 6;
const int in2 = 7;
const int EnA = 10;
const int in3 = 8;
const int in4 = 9;
const int EnB = 5;  

void motors_stop();
void motors_forward();
void motors_right();
void motors_left();
void motors_backward();

void setup() {
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  digitalWrite(EnA,HIGH);
  digitalWrite(EnB,HIGH);
  set_speed(255, 255);
}

void loop() {
  delay(1000);
  
  motors_forward();
  delay(3000);
  motors_stop(500);
  
  motors_right(20);
  motors_stop(500);
  
  motors_backward();
  delay(3000);
  motors_stop(500);

  motors_left(20);
  motors_stop(500);
}

void set_speed(int v_a, int v_b) {
  analogWrite(EnA, v_a);
  analogWrite(EnB, v_b);
}

void motors_stop(int miliseconds) {
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  delay(miliseconds);
}


void motors_backward() {
  digitalWrite(6, HIGH);
  digitalWrite(7, LOW);
  digitalWrite(8, HIGH);
  digitalWrite(9, LOW);
}

void motors_forward() {
  digitalWrite(6, LOW);
  digitalWrite(7, HIGH);
  digitalWrite(8, LOW);
  digitalWrite(9, HIGH);
}

void motors_right(int steps) {
  for(int i = 0; i < steps; i++) {
      digitalWrite(6, HIGH);
      digitalWrite(7, LOW);
      digitalWrite(8, LOW);
      digitalWrite(9, HIGH);
      delay(300);
      motors_stop(300);
  } 

}

void motors_left(int steps) {  
  for(int i = 0; i < steps; i++) {
      digitalWrite(6, LOW);
      digitalWrite(7, HIGH);
      digitalWrite(8, HIGH);
      digitalWrite(9, LOW);
      delay(300);
      motors_stop(300);
  }

}
