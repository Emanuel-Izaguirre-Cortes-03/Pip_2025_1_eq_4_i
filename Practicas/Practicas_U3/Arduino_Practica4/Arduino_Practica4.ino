
int v;
int sensores []= {A0,A1,A2}; //Sensores digitales o analogicos
//LDR, potenciometro, HCSR04, PIR, LM35, ...
int valores_Sensores []= {A0, A1, A2};

int led = 13;

void setup() {
pinMode(led, OUTPUT);
Serial.begin(9600);
Serial.setTimeout(100);
}

int sensor1() {
  return analogRead(sensores[0]); // Lectura del LDR
}

int sensor2() {
  return analogRead(sensores[1]); // Lectura del LM35
}

int sensor3() {
  return analogRead(sensores[2]); // Lectura del sensor PIR
}

void loop() {
  // put your main code here, to run repeatedly:

  valores_Sensores[0] = sensor1();
  valores_Sensores[1] = sensor2();
  valores_Sensores[2] = sensor3();

  String cadena = "";
  for (int i = 0; i<3; i++)
  {
  // valores_Sensores[i] = analogRead(sensores[i]); // ya no se usa
  cadena += String(valores_Sensores[i]) + "@";
  }
  
  Serial.println(cadena);

  if(Serial.available()>0)
  {
    v = Serial.readString().toInt();
    digitalWrite(led, v);
  }

  delay(100);
}
