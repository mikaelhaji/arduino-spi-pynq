// Testing Out Serialization from Python Script [Workaround to Memory Constraints]

const int ledPin = 13; // Assuming we blink an LED for testing, but this can be replaced with your real application.

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600); // Start the serial communication at 9600 baud rate
}

void loop() {
  if (Serial.available()) {  // Check if there's data available to read
    int data = Serial.read(); // Read one byte

    // For this example, let's say if we receive '1', we turn on an LED and for '0', we turn it off.
    if (data == '1') {
      digitalWrite(ledPin, HIGH);
    } else if (data == '0') {
      digitalWrite(ledPin, LOW);
    }
  }
}

