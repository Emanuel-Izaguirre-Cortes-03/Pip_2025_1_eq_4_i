int pot = A0;
int led1 = 5;
int led2 = 6;
int led3 = 7;
int led4 = 8;

void prenderled(int valor) {
  if (valor < 500) {
    // Encender y apagar de izquierda a derecha
    digitalWrite(led1, HIGH);
    delay(100);
    digitalWrite(led1, LOW);
    
    digitalWrite(led2, HIGH);
    delay(100);
    digitalWrite(led2, LOW);
    
    digitalWrite(led3, HIGH);
    delay(100);
    digitalWrite(led3, LOW);
    
    digitalWrite(led4, HIGH);
    delay(100);
    digitalWrite(led4, LOW);
  } else {
    // Encender y apagar de derecha a izquierda
    digitalWrite(led4, HIGH);
    delay(100);
    digitalWrite(led4, LOW);
    
    digitalWrite(led3, HIGH);
    delay(100);
    digitalWrite(led3, LOW);
    
    digitalWrite(led2, HIGH);
    delay(100);
    digitalWrite(led2, LOW);
    
    digitalWrite(led1, HIGH);
    delay(100);
    digitalWrite(led1, LOW);
  }
}

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int valor = analogRead(pot);  // Leer el valor del potenciómetro
  Serial.println(valor);        // Mostrar en el monitor serie
  prenderled(valor);            // Ejecutar la secuencia de LEDs
  delay(100);
}