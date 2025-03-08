const int numLEDs = 8; // Número de LEDs (para representar un byte)
int ledPins[numLEDs] = {2, 3, 4, 5, 6, 7, 8, 9}; // Pines de los LEDs

void setup() {
    Serial.begin(9600); // Iniciar comunicación serial
    for (int i = 0; i < numLEDs; i++) {
        pinMode(ledPins[i], OUTPUT); // Configurar los pines como salida
    }
    Serial.println("Ingrese un número decimal (0-255):");
}

void loop() {
    if (Serial.available()) {
        int numero = Serial.parseInt(); // Leer el número ingresado
        if (numero >= 0 && numero <= 255) {
            Serial.print("Número en binario: ");
            for (int i = 0; i < numLEDs; i++) {
                int bitValue = (numero >> i) & 1; // Extraer el bit correspondiente
                if (bitValue == 1) {
                    digitalWrite(ledPins[i], HIGH); // Encender el LED al máximo brillo
                } else {
                    digitalWrite(ledPins[i], LOW); // Apagar el LED
                }
                Serial.print(bitValue);
            }
            Serial.println();
        } else {
            Serial.println("Número fuera de rango. Ingrese un valor entre 0 y 255.");
        }
    }
}
