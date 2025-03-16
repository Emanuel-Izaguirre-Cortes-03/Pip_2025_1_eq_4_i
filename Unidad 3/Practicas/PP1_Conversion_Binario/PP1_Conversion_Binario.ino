int numLEDs = 8;
int ledPins[] = {2, 3, 4, 5, 6, 7, 8, 9};  // Pines de los LEDs
int ultimoNumero = -1;  // Variable para almacenar el último número recibido

void setup() {
    Serial.begin(9600);
    
    for (int i = 0; i < numLEDs; i++) {
        pinMode(ledPins[i], OUTPUT);  // Configura cada pin de LED como salida
        digitalWrite(ledPins[i], LOW);  // Apaga todos los LEDs al inicio
    }
}

void loop() {
    if (Serial.available()) {
        int numero = Serial.parseInt();  // Leer un número ingresado por el monitor serial
        
        // Solo actualizar los LEDs si el número es diferente al último ingresado
        if (numero >= 0 && numero <= 255 && numero != ultimoNumero) {
            Serial.print("Número en binario: ");
            
            // Encender o apagar LEDs según los bits del número
            for (int i = 0; i < numLEDs; i++) {
                int estado = (numero >> i) & 1;  // Extrae el bit correspondiente a cada LED
                digitalWrite(ledPins[i], estado);  // Enciende o apaga el LED según el bit
                Serial.print(estado);  // Imprime el estado del bit (0 o 1) en el monitor serial
            }
            
            Serial.println();  // Nueva línea en la salida Serial
            ultimoNumero = numero;  // Guarda el número actual para evitar actualizaciones innecesarias
        } else if (numero < 0 || numero > 255) {
            Serial.println("Número fuera de rango. Ingrese un valor entre 0 y 255.");
        }
    }
}



