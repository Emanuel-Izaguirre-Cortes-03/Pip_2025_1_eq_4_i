int led1 = 5;
int led2 = 6;
int led3 = 7;
int led4 = 8;

void prenderled() {
  // Encender y apagar  de izquierda a derecha 
  digitalWrite(led1, 1);
  delay(100);
  digitalWrite(led1, 0); 
  digitalWrite(led2, 1); 
  delay(100);
  digitalWrite(led2, 0); 
  digitalWrite(led3, 1); 
  delay(100);
  digitalWrite(led3, 0); 
  digitalWrite(led4, 1);
  delay(100);
  digitalWrite(led4,0);
 
  //Encender  y apagar de derecha a izquierda 
  digitalWrite(led4,1);
  delay(100);
  digitalWrite(led4,0); 
  digitalWrite(led3,1); 
  delay(100);
  digitalWrite(led3,0); 
  digitalWrite(led2,1); 
  delay(100);
  digitalWrite(led2,0); 
  digitalWrite(led1,1); 
  delay(100);
  digitalWrite(led1,0); 


 
}

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);

  prenderled(); // Ejecutar la secuencia de inicio correctamente
}

int v;

void loop() {
  if (Serial.available() >= 0) {
    v = Serial.readString().toInt();
    prenderled();  // Se ejecuta la secuencia antes de encender un LED
    digitalWrite(v, 1); // Enciende el LED recibido por Serial
 

    

  }
  delay(100);
}
