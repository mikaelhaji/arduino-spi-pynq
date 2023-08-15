const int numElectrodes = 73;
char data[numElectrodes];
int index = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char received = Serial.read();

    if (received == 'E') {
      // End of a row detected, process the data if needed
      // Then reset index
      index = 0;
    } else {
      // Storing data in the array
      data[index] = received;
      index++;

      // Optional: Check if index exceeds the buffer size to avoid overflow
      if (index >= numElectrodes) {
        index = numElectrodes - 1;
      }
    }
  }
}

