#include <Servo.h>
Servo servoRight;
Servo servoLeft;
const int in1 = 6;
const int in2 = 7;
const int EnA = 10;
const int in3 = 8;
const int in4 = 9;
const int EnB = 5;
char state = 9;

void set_speed(int, int);
void motors_stop(int);
void motors_forward(int);
void motors_backward(int);
void motors_right(int);
void motors_left(int);

void setup() {
	Serial.begin(9600);
	servoRight.attach(13);
	servoLeft.attach(12);
	servoRight.write(135);
	servoLeft.write(90);
	pinMode(in1, OUTPUT);
	pinMode(in2, OUTPUT);
	pinMode(in3, OUTPUT);
	pinMode(in4, OUTPUT);
	digitalWrite(EnA, HIGH);
	digitalWrite(EnB, HIGH);
	set_speed(255, 255);
}

void loop() {
	if(Serial.available()) {
		state = Serial.read();
	}

	Serial.write(state)

	switch (state) {
		case '0':
			motors_left(100);
			motors_stop(200);
			break;

		case '1':
			motors_forward(150);
			motors_stop(200);
			break;

		case '2':
			motors_right(40);
			motors_stop(200);
			break;

		case '3':
			motors_left(40);
			motors_stop(200);
			break;

		case '4':
			capture();
			break;

		case '9':
			motors_stop(100);
			break;

		default:
			break;
	}
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

void motors_right(int ms) {
	digitalWrite(6, HIGH);
	digitalWrite(7, LOW);
	digitalWrite(8, LOW);
	digitalWrite(9, HIGH);
	delay(ms);
}

void motors_left(int ms) {
	digitalWrite(6, LOW);
	digitalWrite(7, HIGH);
	digitalWrite(8, HIGH);
	digitalWrite(9, LOW);
	delay(ms);
}

void drop() {
	// open claws
	servoRight.write(90);
	servoLeft.write(135);

	motors_stop(100);
	motors_backward(300);
	motors_stop(10000); // TODO correct way to end
}

void capture() {
	// open claws
	servoRight.write(90);
	servoLeft.write(135);
	
	motors_stop(100);
	motors_forward(250);
	motors_right(60); // fix unestable move
	motors_stop(100);

	// close claws
	servoRight.write(135);
	servoLeft.write(90);
}
