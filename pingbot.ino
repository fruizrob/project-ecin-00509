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

void test_line() {
  delay(1000);

  motors_forward(2000);
  motors_stop(1000);

  motors_right(10);
  motors_stop(1000);  
}

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
  test_line();
}

void set_speed(int v_a, int v_b) {
  analogWrite(EnA, v_a);
  analogWrite(EnB, v_b);
}

void motors_stop(int ms) {
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  delay(ms);
}


void motors_backward(int ms) {
  digitalWrite(6, HIGH);
  digitalWrite(7, LOW);
  digitalWrite(8, HIGH);
  digitalWrite(9, LOW);
  delay(ms);
}

void motors_forward(int ms) {
  digitalWrite(6, LOW);
  digitalWrite(7, HIGH);
  digitalWrite(8, LOW);
  digitalWrite(9, HIGH);
  delay(ms);
}

void motors_right(int steps, int ms) {
  for(int i = 0; i < steps; i++) {
      digitalWrite(6, HIGH);
      digitalWrite(7, LOW);
      digitalWrite(8, LOW);
      digitalWrite(9, HIGH);
      delay(ms);
      motors_stop(ms);
  } 

}

void motors_left(int steps, int ms) {  
  for(int i = 0; i < steps; i++) {
      digitalWrite(6, LOW);
      digitalWrite(7, HIGH);
      digitalWrite(8, HIGH);
      digitalWrite(9, LOW);
      delay(ms);
      motors_stop(ms);
  }

}
