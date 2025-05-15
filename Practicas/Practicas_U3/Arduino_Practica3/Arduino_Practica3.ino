
int v;
int sensores []= {A0,A1,A2,A3}; //Sensores digitales o analogicos
//LDR, potenciometro, HCSR04, PIR, LM35, ...
int valores_Sensores []= {0, 0, 0,0};

int led = 13;

void setup() {
pinMode(led, OUTPUT);
Serial.begin(9600);
Serial.setTimeout(100);
}

void loop() {
  // put your main code here, to run repeatedly:
  String cadena = "";
  for (int i = 0; i<4; i++){
  valores_Sensores[i] = analogRead(sensores[i]);
  cadena += String(valores_Sensores[i]) + "@";
  }
  

  Serial.println(cadena);

  if(Serial.available()>0){
    v = Serial.readString().toInt();
    digitalWrite(led, v);
  }

  delay(100);
}
