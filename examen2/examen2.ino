const int ledPins[] = {2, 3, 4, 5, 6, 7, 8, 9};
char palabra[6];
int index = 0;

void setup() {
    Serial.begin(9600);
    for (int pin : ledPins) pinMode(pin, OUTPUT);
    Serial.println("Ingresa una palabra (1 a 5 caracteres en mayúsculas):");
}

void loop() {
    while (Serial.available() > 0) {
        char letra = Serial.read();
        if (letra >= 'A' && letra <= 'Z' && index < 5) palabra[index++] = letra;
    }
    
    if (index > 0) {
        palabra[index] = '\0';
        Serial.println("\nPalabra recibida: " + String(palabra));
        
        for (int i = 0; i < index; i++) {
            Serial.print("Mostrando letra: ");
            Serial.print(palabra[i]);
            Serial.print(" (ASCII: ");
            Serial.print((int)palabra[i]);
            Serial.println(")");
            mostrarBinario(palabra[i]);
            delay(5000);
        }
        apagarLeds();
        index = 0;
        Serial.println("Ingresa otra palabra (1 a 5 caracteres en mayúsculas):");
    }
}

void mostrarBinario(byte valor) {
    Serial.print("Caracter: ");
    Serial.print((char)valor);
    Serial.print(" -> Binario: ");
    
    for (int i = 7; i >= 0; i--) {
        Serial.print(bitRead(valor, i));
        digitalWrite(ledPins[i], bitRead(valor, i));
    }
    Serial.println();
}

void apagarLeds() {
    for (int pin : ledPins) digitalWrite(pin, LOW);
    Serial.println("Todos los LEDs apagados.");
}
