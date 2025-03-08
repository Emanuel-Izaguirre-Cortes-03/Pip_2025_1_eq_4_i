int pot = A0;
int led1 = 5;
int led2 = 6;
int led3 = 7;
int led4 = 8;

void prenderled(int valor) {
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
  digitalWrite(led4, LOW);

  int nivel = map(valor, 0, 1023, 0, 3);
  
  if (nivel == 0) {
    digitalWrite(led1, HIGH);
  } else if (nivel == 1) {
    digitalWrite(led2, HIGH);
  } else if (nivel == 2) {
    digitalWrite(led3, HIGH);
  } else if (nivel == 3) {
    digitalWrite(led4, HIGH);
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
  int valor = analogRead(pot);
  Serial.println(valor);
  prenderled(valor);
  delay(100);
}