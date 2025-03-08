int led = 10 ; 
void setup() {
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i =0;i<255;i++){
    analogWrite(led,i);
    delay(10);
  }
  for(int i =255;i>0;i--){
    analogWrite(led,i);
    delay(10);

  }

}
