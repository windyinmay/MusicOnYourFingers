import serial
import csv
import time

# Serial port configuration
SERIAL_PORT = "/dev/tty.usbmodem1101"
BAUD_RATE = 9600
TIMEOUT = 2

# Open the serial port
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=TIMEOUT)

# CSV file configuration
# CSV_FILE = './Data/finger_bending_data.csv'
CSV_FILE = './Data/training_dataset1.csv'
HEADER = ['Thumb', 'Index', 'Middle', 'Ring', 'Little', 'Label']

# Function to write data to CSV
def write_to_csv(data):
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Write the header
write_to_csv(HEADER)

try:
    # Read data from serial port
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            data = line.split(',')
            if len(data) == 6:  # Ensure data format is correct
                write_to_csv(data)
            else:
                print("Invalid data received:", line)
        time.sleep(0.1)  # Delay to avoid overloading the CPU
except KeyboardInterrupt:
    print("Data collection stopped.")
finally:
    ser.close()  # Close the serial port