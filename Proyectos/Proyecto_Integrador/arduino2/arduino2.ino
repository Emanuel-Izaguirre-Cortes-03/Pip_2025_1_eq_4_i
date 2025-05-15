// Pines del sensor LDR y LEDs
const int ldrPin = A0;
const int led1 = 7;
const int led2 = 8;
const int led3 = 9;

void setup() {
  Serial.begin(9600);

  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
}

void loop() {
  servicioLuz();
  delay(500); // Espera para evitar lecturas excesivas
}

void servicioLuz() {
  int luz = analogRead(ldrPin);
  Serial.print("Valor de luz: ");
  Serial.println(luz);

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
