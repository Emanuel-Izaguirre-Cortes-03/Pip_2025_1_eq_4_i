
int numero;
int ledPins[] = {12, 11, 10, 9, 8, 7, 6, 5};
 
void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 8; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW);
  }
}
 
void loop() {
  if (Serial.available() > 0) {  
    numero = Serial.readString().toInt();
 
    if (numero >= 0 && numero <= 255) {  
      for (int i = 0; i < 8; i++) {
        digitalWrite(ledPins[i], (numero >> (7 - i)) & 1);
        
      }
      

    }
   delay(4500); 

      for (int i = 0; i < 8; i++) {
        digitalWrite(ledPins[i], LOW);
      }
  } 
  
}