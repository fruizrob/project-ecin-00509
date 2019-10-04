const int in1 = 6;
const int in2 = 7;
const int EnA = 5;
const int in3 = 8;
const int in4 = 9;
const int EnB = 10;


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
}

void loop() {
  motors_stop();
  delay(1000);
  motors_right();
  delay(1000);
  motors_stop();
  delay(1000);
  motors_left();
  delay(1000);
}

void motors_stop() {
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
}

void motors_backward() {
  digitalWrite(6, HIGH);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, HIGH);
}

void motors_forward() {
  digitalWrite(6, LOW);
  digitalWrite(7, HIGH);
  digitalWrite(8, HIGH);
  digitalWrite(9, LOW);
}

void motors_right() {
  digitalWrite(6, LOW);
  digitalWrite(7, HIGH);
  digitalWrite(8, LOW);
  digitalWrite(9, HIGH);
}

void motors_left() {
   digitalWrite(6, HIGH);
  digitalWrite(7, LOW);
  digitalWrite(8, HIGH);
  digitalWrite(9, LOW);
}
