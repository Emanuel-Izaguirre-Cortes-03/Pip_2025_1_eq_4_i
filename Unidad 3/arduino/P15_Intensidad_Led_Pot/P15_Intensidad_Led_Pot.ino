int led = 10 ; 
int pot=A0;

void setup() {
  // put your setup code here, to run once:

}

void loop() {
  int v  = analogRead(pot);//0 -1023
  v=v/4;// map(v,0,1023,0,255)
  analogWrite(led,v);//0-255
  delay(10);


 

}