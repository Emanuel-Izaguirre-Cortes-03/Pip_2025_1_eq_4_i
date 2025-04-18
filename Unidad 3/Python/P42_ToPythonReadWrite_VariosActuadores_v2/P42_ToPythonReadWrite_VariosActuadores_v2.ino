int actuadores[] = {10,11,12};
int pot 
void setup() {
  // put your setup code here, to run once:
  for(int i=0; i<3; i++){
    pinMode(actuadores [i], OUTPUT);
  }
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    String cadena = Serial.readString();
    //Serial.println(cadena);
    int led = cadena.charAt(0)-48;
    int estado = cadena.charAt(1)-48;
    Serial.println(String(led) + " " + String(estado));
    digitalWrite(actuadores[led], estado);
  }
  delay(100);
}
