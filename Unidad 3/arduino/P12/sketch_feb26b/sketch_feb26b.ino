int pot= A0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  int v = analogRead(pot);
  Serial.println(v);
  delay(100);

}
