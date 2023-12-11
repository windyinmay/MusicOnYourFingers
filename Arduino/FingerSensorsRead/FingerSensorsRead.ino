// Define the analog pins for each finger
const int THUMB_PIN = A1;
const int INDEX_PIN = A2;
const int MIDDLE_PIN = A3;
const int RING_PIN = A4;
const int LITTLE_PIN = A5;

//Define speaker
// int speakerPin = 9;

// Define a flag to control data tracking
bool isTracking = true;
//Define the resistors used
const float RESISTOR_VALUE = 2200.0;  // Ohms

void setup() {
  Serial.begin(9600);
//   Move constant related to speaker to separate Arduino sketch
//   pinMode(speakerPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  // Check if data tracking is enabled
  if (isTracking) {
    // Read and print resistance values for each finger
    float thumbResistance = readResistance(THUMB_PIN);
    float indexResistance = readResistance(INDEX_PIN);
    float middleResistance = readResistance(MIDDLE_PIN);
    float ringResistance = readResistance(RING_PIN);
    float littleResistance = readResistance(LITTLE_PIN);
    
    // Here, determine the label for which finger is bent, or 'None'
    // String label = determineFingerBent(thumbValue, indexValue, middleValue, ringValue, littleValue);

    // Send the data in a comma-separated format
    Serial.print(thumbResistance);
    Serial.print(",");
    Serial.print(indexResistance);
    Serial.print(",");
    Serial.print(middleResistance);
    Serial.print(",");
    Serial.print(ringResistance);
    Serial.print(",");
    Serial.print(littleResistance);
    // Serial.print(",");
    // Serial.println("None_bent");
    // Serial.print(",");
    // Serial.println(label);

    delay(100); // Delay for a second before sending the next data

    if (Serial.available() > 0) {
    char input = Serial.read();
    
  
    //Codes below used when collecting data for training
    //Collecting data was processed by having one finger bent separately
    // Input S in massage to Arduino, stretch fingers to have the sensors get back to original states
    //Then input R when one finger is bent to keep collecting
    // If 'S' is received, stop data tracking
    if (input == 'S') {
      isTracking = false;
      Serial.println("Data tracking stopped.");
    }
    // If 'R' is received, resume data tracking
    else if (input == 'R') {
      isTracking = true;
      Serial.println("Data tracking resumed.");
    }
  }
}
}

// We decided not follow this traditional condition as the data would be set in a limitation
// String determineFingerBent(int thumb, int index, int middle, int ring, int little) {
//     // Add your logic here to determine which finger is bent
//     // This can be based on specific thresholds or patterns in the sensor readings
//     // For example:
//     if (thumb < threshold) {
//         return "Thumb_bent";
//     }
//     // ... similar conditions for other fingers ...

//     return "None"; // Return "None" if no specific finger is detected as bent
// }

// Function to read resistance from analog pin
float readResistance(int analogPin) {
  int analogValue = analogRead(analogPin);
  float voltage = analogValue * (3.3 / 1023.0); // Convert analog value to voltage
  float resistance = (3.3 / voltage - 1) * RESISTOR_VALUE; // Calculate resistance using voltage divider formula
  return resistance;
}
