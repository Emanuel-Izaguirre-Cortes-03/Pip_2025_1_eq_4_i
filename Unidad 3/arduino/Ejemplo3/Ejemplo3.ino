#include <Servo.h>

#define TRIG 8
#define ECHO 7
#define SERVO 9

Servo servo;

void setup() {
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  servo.attach(SERVO);
}

long medirDistancia() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  
  long duracion = pulseIn(ECHO, HIGH);
  long distancia = duracion * 0.034 / 2;
  return distancia;
}

void loop() {
  for (int angulo = 0; angulo <= 180; angulo += 2) {
    servo.write(angulo);
    delay(50);
    long distancia = medirDistancia();
    Serial.print(angulo);
    Serial.print(",");
    Serial.println(distancia);
  }

  for (int angulo = 180; angulo >= 0; angulo -= 2) {
    servo.write(angulo);
    delay(50);
    long distancia = medirDistancia();
    Serial.print(angulo);
    Serial.print(",");
    Serial.println(distancia);
  }
}
