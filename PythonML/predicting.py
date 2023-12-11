import csv
import serial
import joblib

# Load the trained machine learning model
model = joblib.load('finger_bent_model.pkl')

#Constant# Establish serial connection with Arduino
SERIAL_PORT = "/dev/tty.usbmodem101"
BAUD_RATE = 9600

# Open serial connection to Arduino
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
ser.flush()

# def predict_finger_bent(data):
#     # Data is a list of resistance values of Thumb, Index, Middle, Ring, Little
#     features = np.array(data).reshape(1, -1)
#     prediction = model.predict(features)
#     return prediction[0]


def write_to_csv(sensor_values, prediction):
    with open('./Data/testing_dataset.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(sensor_values + [prediction])


while True:
    if ser.in_waiting > 0:
        try:
            # Read a line of data from the serial port
            line = ser.readline().decode('utf-8').rstrip()
            sensor_values = [float(val) for val in line.split(',')]

            # Make sure the correct number of sensor values are read
            if len(sensor_values) == 5:  # Adjust the number based on your sensor count
                # Predict which finger is bent
                prediction = model.predict([sensor_values])[0]

                #For debugging as the conductive yarns easily touch
                print(f'Thumb: {sensor_values[0]}, Index: {sensor_values[1]}, Middle: {sensor_values[2]}, Ring: {sensor_values[3]}, Little: {sensor_values[4]}')
                # Print the prediction
                print(f"Predicted Finger: {prediction}")

                # Write the sensor values and prediction to the CSV file
                write_to_csv(sensor_values, prediction)
                # Send the prediction back to the Arduino
                ser.write(f'{prediction}\n'.encode('utf-8'))

        except ValueError as e:
            print(f"Error in data conversion: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# while True:
#     if ser.in_waiting > 0:
#         line = ser.readline().decode('utf-8').rstrip()
#         sensor_values = list(map(int, line.split(',')))  # Convert string values to int

#         # Predict which finger is bent
#         finger_bent = predict_finger_bent(sensor_values)

#         # Send the prediction back to the Arduino
#         ser.write(finger_bent.encode())

# while True:
#     try:
#         # Read data from Arduino
#         line = ser.readline().decode('utf-8').strip()
#         values = list(map(float, line.split(',')))
        
#         # Create a DataFrame from the incoming data
#         df = pd.DataFrame([values], columns=['Thumb', 'Index', 'Middle', 'Ring', 'Little'])

#         # Make predictions
#         prediction = clf.predict(df)[0]

#         # Print the prediction
#         # if prediction == 'Thumb_bent':
#         #     print("Thumb is bent - D")
#         # elif prediction == 'Index_bent':
#         #     print("Index is bent - C")
#         # elif prediction == 'Middle_bent':
#         #     print("Middle is bent - B")
#         # elif prediction == 'Ring_bent':
#         #     print("Ring is bent - A")
#         # elif prediction == 'Little_bent':
#         #     print("Little is bent - G")
#         # Map predictions to notes
#         note_mapping = {'Thumb_bent': 'D', 'Index_bent': 'C', 'Middle_bent': 'B', 'Ring_bent': 'A', 'Little_bent': 'G'}
#         note = note_mapping.get(prediction, 'Unknown')

#         # Send the note signal to Arduino
#         ser.write(note.encode())

#         print(f"Predicted: {prediction} - Playing Note: {note}")
        
#     except KeyboardInterrupt:
#         # Close serial connection on KeyboardInterrupt
#         ser.close()
#         break