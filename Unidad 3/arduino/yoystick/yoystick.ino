int Potx=A0;
int Poty=A1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);


}

void loop() {
  // put your main code here, to run repeatedly:
  int v1 = analogRead(Potx);
  int v2 = analogRead(Poty);
  Serial.println(String(v1)+" "+String(v2));

}
