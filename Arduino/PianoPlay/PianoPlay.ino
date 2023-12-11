// Define the analog pins for each finger
const int THUMB_PIN = A1;
const int INDEX_PIN = A2;
const int MIDDLE_PIN = A3;
const int RING_PIN = A4;
const int LITTLE_PIN = A5;
// const int sensorPins[] = {A1, A2, A3, A4, A5};

const int piezoPin = 8; // Connect piezo speaker to this pin

const float RESISTOR_VALUE = 2200.0; 

void setup() {
    Serial.begin(9600); // Start the serial communication
  //   for (int i = 0; i < 5; i++) {
  //   pinMode(sensorPins[i], INPUT); // Initialize sensor pins as input
  // }
    pinMode(piezoPin, OUTPUT);
}

void loop() {
    float thumbResistance = readResistance(THUMB_PIN);
    float indexResistance = readResistance(INDEX_PIN);
    float middleResistance = readResistance(MIDDLE_PIN);
    float ringResistance = readResistance(RING_PIN);
    float littleResistance = readResistance(LITTLE_PIN);

    //Send the data in a comma-separated format
    Serial.print(thumbResistance);
    Serial.print(",");
    Serial.print(indexResistance);
    Serial.print(",");
    Serial.print(middleResistance);
    Serial.print(",");
    Serial.print(ringResistance);
    Serial.print(",");
    Serial.println(littleResistance);
    delay(200); // Delay for a second before sending the next data

    // Read sensor values and send them to the Python script
  // for (int i = 0; i < 5; i++) {
  //   float resistance = readResistance(sensorPins[i]);
  //   Serial.print(resistance);
  //   if (i < 4) {
  //     Serial.print(","); // Separate values with a comma
  //   }
  // }
  // Serial.println(); // Signal end of data packet

  // Check if there's a prediction from the Python script
  if (Serial.available() > 0) {
    String fingerBent = Serial.readStringUntil('\n');
    fingerBent.trim();
    playNote(fingerBent); 
  }
}
        // char note = Serial.read();
    // Play the corresponding frequency
    //     if (note == 'D') {
    //         tone(speakerPin, 587.33);  // D note frequency
    //     } else if (note == 'C') {
    //         tone(speakerPin, 523.25);  // C note frequency
    //     } else if (note == 'B') {
    //         tone(speakerPin, 466.16);  // B note frequency
    //     } else if (note == 'A') {
    //         tone(speakerPin, 440.00);  // A note frequency
    //     } else if (note == 'G') {
    //         tone(speakerPin, 392.00);  // G note frequency
    //     } else {
    //         // Handle unknown note or do nothing
    //     }

    //     delay(500);  // Adjust delay as needed
    //     noTone(speakerPin);  // Stop the tone
    
//         int frequency = getFrequency(note);
//         if (frequency != 0) {
//             tone(piezoPin, frequency, 500); // Play the note for 500 ms
//             delay(600); // Wait a bit before the next note
//         }
//     }
// }

// Function to read resistance from analog pin
float readResistance(int analogPin) {
  int analogValue = analogRead(analogPin);
  float voltage = analogValue * (3.3 / 1023.0); // Convert analog value to voltage
  float resistance = (3.3 / voltage - 1) * RESISTOR_VALUE; // Calculate resistance using voltage divider formula
  return resistance;
}

void playNote(String finger) {
  float frequency = 0.0;
  if (finger == "Thumb_bent") frequency = 587.33;   // D note
  else if (finger == "Index_bent") frequency = 523.25; // C note
  // else if (finger == "Middle_bent") frequency = 494; // B note
  else if (finger == "Middle_bent") frequency = 466.16;
  else if (finger == "Ring_bent") frequency = 440.00;   // A note
  else if (finger == "Little_bent") frequency = 392.00; // G note
  else if (finger == "None_bent") frequency = 0; // No finger bent

  if (frequency > 0) {
    tone(piezoPin, frequency, 500); // Play the note for 500 ms
    delay(600); // Delay to prevent overlap of tones
  } else {
    noTone(piezoPin); // Stop any playing tone
  }
}

int getFrequency(char note) {
    switch (note) {
        case 'C': return 262; // Frequency for note C4
        case 'D': return 294; // Frequency for note D4
        case 'E': return 330; // Frequency for note E4
        case 'F': return 349; // Frequency for note F4
        case 'G': return 392; // Frequency for note G4
        default: return 0;  // No note
    }
}

