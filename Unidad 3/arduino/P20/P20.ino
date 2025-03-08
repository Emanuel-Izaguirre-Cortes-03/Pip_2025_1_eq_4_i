int leds []={10,11,12}; // 3pines digitales 
void setup() {
  // put your setup code here, to run once:
  for(int i=0;i<3;i++){
    pinMode(leds[i],OUTPUT);
  }
  Serial.begin(9600);
  Serial.setTimeout(100);
  

}
String cadena;

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    cadena=Serial.readString();
    for(int i =0; i<3;i++){
      digitalWrite(leds[i],cadena.charAt(i)-48);
    }
  }


}
