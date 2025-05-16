#include <Servo.h>

// Pines del sensor LDR
const int ldrPin = A0;
const int led1 = 12;
const int led2 = 11;
const int led3 = 10;

// Variables de control
char comando;
bool servicio1 = false;

void setup() {
  Serial.begin(9600);

  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);

  // Apagar LEDs al inicio
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
}

void loop() {
  if (Serial.available()) {
    comando = Serial.read();

    if (comando == '1') {
      servicio1 = true;
    } 
    else if (comando == '0') {
      servicio1 = false;
      apagarTodo();
    }
  }

  if (servicio1) {
    servicioLuz();
    delay(100);
  }
}

void servicioLuz() {
  int luz = analogRead(ldrPin);
  Serial.println(luz); // SOLO esto debe enviarse por Serial

  if (luz > 400) { // Hay suficiente luz -> apagar LEDs
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
  } else {         // Hay poca luz -> encender LEDs
    digitalWrite(led1, HIGH);
    digitalWrite(led2, HIGH);
    digitalWrite(led3, HIGH);
  }
}

void apagarTodo() {
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
}

