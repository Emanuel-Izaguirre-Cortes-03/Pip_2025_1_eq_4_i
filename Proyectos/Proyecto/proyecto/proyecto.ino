#define PIN_LDR A0
#define LED1 12
#define LED2 11
#define LED3 10

#define PIR_PIN 9
#define BUZZER_PIN 8
#define LED_ROJO 7
#define HC_TRIG 6
#define HC_ECHO 5

#include <DHT.h>
#define DHTPIN 4
#define DHTTYPE DHT11 // o DHT22 según tu sensor
#define LED_TEMP 3

DHT dht(DHTPIN, DHTTYPE);

bool servicioLuzActivo = false;
bool servicioMovimientoActivo = false;
bool servicioTempActivo = false;
String comando = "";
unsigned long ultimoEnvioTemp = 0;
const unsigned long intervaloTemp = 2000; // 2 segundos

void setup() {
  Serial.begin(9600);
  pinMode(PIN_LDR, INPUT);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);

  pinMode(PIR_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(LED_ROJO, OUTPUT);
  pinMode(HC_TRIG, OUTPUT);
  pinMode(HC_ECHO, INPUT);
  pinMode(LED_TEMP, OUTPUT);

  digitalWrite(BUZZER_PIN, LOW);
  digitalWrite(LED_ROJO, LOW);

  dht.begin();
}

void loop() {
  // Leer comandos desde la PC
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '\n') {
      comando.trim();
      if (comando == "L1") {
        servicioLuzActivo = true;
      } else if (comando == "L0") {
        servicioLuzActivo = false;
        digitalWrite(LED1, LOW);
        digitalWrite(LED2, LOW);
        digitalWrite(LED3, LOW);
      } else if (comando == "S2ON") {
        servicioMovimientoActivo = true;
      } else if (comando == "S2OFF") {
        servicioMovimientoActivo = false;
        digitalWrite(BUZZER_PIN, LOW);
        digitalWrite(LED_ROJO, LOW);
      } else if (comando == "S3ON") {
        servicioTempActivo = true;
      } else if (comando == "S3OFF") {
        servicioTempActivo = false;
        digitalWrite(LED_TEMP, LOW);
      }
      comando = "";
    } else {
      comando += c;
    }
  }

  // Servicio 1: Luz ambiental
  if (servicioLuzActivo) {
    int valorLDR = analogRead(PIN_LDR);
    Serial.print("LDR:");
    Serial.println(valorLDR);

    if (valorLDR < 400) {
      digitalWrite(LED1, HIGH);
      digitalWrite(LED2, HIGH);
      digitalWrite(LED3, HIGH);
    } else {
      digitalWrite(LED1, LOW);
      digitalWrite(LED2, LOW);
      digitalWrite(LED3, LOW);
    }
    delay(200);
  }

  // Servicio 2: Detector de movimiento
  if (servicioMovimientoActivo) {
    // Medir distancia
    long duracion, distancia;
    digitalWrite(HC_TRIG, LOW);
    delayMicroseconds(2);
    digitalWrite(HC_TRIG, HIGH);
    delayMicroseconds(10);
    digitalWrite(HC_TRIG, LOW);
    duracion = pulseIn(HC_ECHO, HIGH, 30000);
    distancia = duracion * 0.034 / 2;

    Serial.print("DIST:");
    Serial.println(distancia);

    if (distancia <= 50 && distancia > 0) {
        int movimiento = digitalRead(PIR_PIN);
        Serial.print("PIR:");
        Serial.println(movimiento);
        if (movimiento == HIGH) {
            digitalWrite(BUZZER_PIN, HIGH);
            digitalWrite(LED_ROJO, HIGH);
        } else {
            digitalWrite(BUZZER_PIN, LOW);
            digitalWrite(LED_ROJO, LOW);
        }
    } else {
        digitalWrite(BUZZER_PIN, LOW);
        digitalWrite(LED_ROJO, LOW);
    }
    delay(100); // Reduce el delay para mayor frecuencia
  }

  // Servicio 3: Temperatura y humedad (NO usar delay aquí)
  if (servicioTempActivo) {
    if (millis() - ultimoEnvioTemp >= intervaloTemp) {
      float h = dht.readHumidity();
      float t = dht.readTemperature();
      
      if (!isnan(t) && !isnan(h)) {
        Serial.print("TEMP:");
        Serial.print(t);
        Serial.print(",HUM:");
        Serial.println(h);
      }

      // Enciende el LED si la temperatura es mayor a 20°C
      if (t > 20) {
        digitalWrite(LED_TEMP, HIGH);
      } else {
        digitalWrite(LED_TEMP, LOW);
      }
      ultimoEnvioTemp = millis();
    }
  }
}
