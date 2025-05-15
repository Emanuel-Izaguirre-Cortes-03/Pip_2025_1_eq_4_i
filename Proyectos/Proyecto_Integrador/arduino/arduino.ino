bool servicio1Activo = false;
bool servicio2Activo = false;

const int pirPin = 10;
const int buzzerPin =11;
const int ledMovimiento = 12;
const int ldrPin = A0;

int pinLuz[] = {7, 8, 9};
int numLeds = 3;

bool sensorActivo = false;
bool modoAutomatico = true;

void setup() {
  Serial.begin(9600);

  for (int i = 0; i < numLeds; i++) {
    pinMode(pinLuz[i], OUTPUT);
  }

  pinMode(pirPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(ledMovimiento, OUTPUT);
}

void loop() {
  if (Serial.available()) {
    String comando = Serial.readStringUntil('\n');
    comando.trim();

    if (comando == "ON") {
      modoAutomatico = false;
      for (int i = 0; i < numLeds; i++) digitalWrite(pinLuz[i], HIGH);
    } else if (comando == "OFF") {
      modoAutomatico = false;
      for (int i = 0; i < numLeds; i++) digitalWrite(pinLuz[i], LOW);
    } else if (comando == "AUTO") {
      modoAutomatico = true;
    } else if (comando == "M") {
      sensorActivo = true;
    } else if (comando == "N") {
      sensorActivo = false;
      digitalWrite(buzzerPin, LOW);
      digitalWrite(ledMovimiento, LOW);
    }
  }

  // Servicio 1: Modo automático basado en luz
  if (modoAutomatico) {
    int luz = analogRead(ldrPin);
    Serial.println(luz);  // Puedes usar este dato para graficarlo

    if (luz < 400) {
  for (int i = 0; i < numLeds; i++) digitalWrite(pinLuz[i], HIGH);  // Se encienden con oscuridad
} else {
  for (int i = 0; i < numLeds; i++) digitalWrite(pinLuz[i], LOW);   // Se apagan con luz
}


  // Servicio 2: Detección de movimiento
  if (sensorActivo) {
    int movimiento = digitalRead(pirPin);
    if (movimiento == HIGH) {
      digitalWrite(buzzerPin, HIGH);
      digitalWrite(ledMovimiento, HIGH);
    } else {
      digitalWrite(buzzerPin, LOW);
      digitalWrite(ledMovimiento, LOW);
    }
  }}}

