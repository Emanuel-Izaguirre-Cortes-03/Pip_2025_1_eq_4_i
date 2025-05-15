int numero;
int led1 = 5;
int led2 = 6;
int led3 = 7;
int led4 = 8;
int led5 = 9;
int led6 = 10;
int led7 = 11;
int led8 = 12;

int b128, b64, b32, b16, b8, b4, b2, b1; // Mayusculas 65 - 90 , minusculas 97 - 122

void setup() {
 
Serial.begin(9600);
pinMode (led1,OUTPUT);// OUTPUT sirve para poner los leds en modo salida y se puedan prender
pinMode (led2,OUTPUT);
pinMode (led3,OUTPUT);
pinMode (led4,OUTPUT);
pinMode (led5,OUTPUT);
pinMode (led6,OUTPUT);
pinMode (led7,OUTPUT);
pinMode (led8,OUTPUT);
}

void loop() {


if (Serial.available()>0) // Si hay algo ingresado, cuando no esta vacio
{
  String palabra  = Serial.readString();//Agarra lo encontrado y lo convierte a String
  palabra.trim();
  for (int i = 0; i < palabra.length(); i++) //Recorre cada letra
  { 
  numero = palabra[i]; // palabra[i] es un char y al intentar guardarlo en una variable int, se guardara  su numero ascii

  if (numero<=255)
  {
  if (numero >= 128) { b128 = 1; numero = numero % 128;}
  else b128 = 0;
  if (numero >= 64) { b64 = 1; numero = numero % 64;}
  else b64 = 0;
  if (numero >= 32) { b32 = 1; numero = numero % 32;}
  else b32 = 0;
  if (numero >= 16) { b16 = 1; numero = numero % 16;}
  else b16 = 0;
  if (numero >= 8) { b8 = 1; numero = numero % 8;}
  else b8 = 0;
  if (numero >= 4) { b4 = 1; numero = numero % 4;}
  else b4 = 0;
  if (numero >= 2) { b2 = 1; numero = numero % 2;}
  else b2 = 0;
  if (numero >= 1) { b1 = 1; }
  else b1 = 0;
  }
  else 
  {
  b128=1;
  b64=1;
  b32=1;
  b16=1;
  b8=1;
  b4=1;
  b2=1;
  b1=1;
  }

//Encender
digitalWrite(led1,b128);
digitalWrite(led2,b64);
digitalWrite(led3,b32);
digitalWrite(led4,b16);
digitalWrite(led5,b8);
digitalWrite(led6,b4);
digitalWrite(led7,b2);
digitalWrite(led8,b1);
// Apagar
delay(4500);
digitalWrite(led1,0);
digitalWrite(led2,0);
digitalWrite(led3,0);
digitalWrite(led4,0);
digitalWrite(led5,0);
digitalWrite(led6,0);
digitalWrite(led7,0);
digitalWrite(led8,0);
delay(250);
parpadeo(4, 500); // 4 segundos
delay(250);


}// Fin for que recorre cada letra
Serial.print("La palabra fue: ");
Serial.println(palabra);
} //Fin if

}// Fin loop

// Metodos
void parpadeo(int veces, int tiempo) 
{ //Metodo de ayuda
for (int i = 0; i < veces; i++) 
{
 
digitalWrite(led1, 1);
digitalWrite(led2, 1);
digitalWrite(led3, 1);
digitalWrite(led4, 1);
digitalWrite(led5, 1);
digitalWrite(led6, 1);
digitalWrite(led7, 1);
digitalWrite(led8, 1);

delay(tiempo);

digitalWrite(led1, 0);
digitalWrite(led2, 0);
digitalWrite(led3, 0);
digitalWrite(led4, 0);
digitalWrite(led5, 0);
digitalWrite(led6, 0);
digitalWrite(led7, 0);
digitalWrite(led8, 0);

delay(tiempo);
}
}



