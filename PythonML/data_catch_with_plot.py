import serial
import csv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Constants
SERIAL_PORT = "/dev/tty.usbmodem101"
BAUD_RATE = 9600

#Initialize serial connection
ser = serial.Serial(SERIAL_PORT,BAUD_RATE)

# Initialize empty lists to store data
x_vals = []
thumbResistance = []
indexResistance = []
middleResistance = []
ringResistance = []
littleResistance = []

#Create a function to read and process data from Arduino
# def read_and_process_dada():
#     line = ser.readline().decode('utf-8').strip()
#     sensorValues = line.split("\t")

#     x_vals.append(len(sensorValues))
#     thumbResistance.append(float(sensorValues[1]))
#     indexResistance.append(float(sensorValues[2]))
#     middleResistance.append(float(sensorValues[3]))
#     ringResistance.append(float(sensorValues[4]))
#     littleResistance.append(float(sensorValues[5]))

# #Print the received values for debugging
#     print(f'Thumb: {sensorValues[0]}, Index: {sensorValues[1]}, Middle: {sensorValues[2]}, Ring: {sensorValues[3]}, Little: {sensorValues[4]}')

# Create a function to read and process data from Arduino
#Version that add error handling for serial communication
def read_and_process_data():
    try:
        line = ser.readline().decode('utf-8').strip()
        sensorValues = line.split("\t")

        if len(sensorValues) == 5:  # Ensure there are 5 values
            x_vals.append(len(x_vals) + 1)
            thumbResistance.append(float(sensorValues[0]))
            indexResistance.append(float(sensorValues[1]))
            middleResistance.append(float(sensorValues[2]))
            ringResistance.append(float(sensorValues[3]))
            littleResistance.append(float(sensorValues[4]))

            # Print the received values for debugging
            print(f'Thumb: {sensorValues[0]}, Index: {sensorValues[1]}, Middle: {sensorValues[2]}, Ring: {sensorValues[3]}, Little: {sensorValues[4]}')
    except ValueError:
        print("Error in data format")
    except Exception as e:
        print(f"An error occurred: {e}")

#Create a function to update the plot
def update_plot(frame):
    read_and_process_data()
    plt.cla()
    plt.plot(x_vals, thumbResistance, label="Thumb")
    plt.plot(x_vals, indexResistance, label="Index")
    plt.plot(x_vals, middleResistance, label="Middle")
    plt.plot(x_vals, ringResistance, label="Ring")
    plt.plot(x_vals, littleResistance, label="Little")
    plt.xlabel('Data Row Number')  # Updated xlabel
    plt.ylabel('Resistance Values')
    plt.legend()

#Create a function to save data to a csv file when the plot window is closed
def on_close(event):
    with open('training_dataset.csv', 'w', newline='') as trainingfile:
        writer = csv.writer(trainingfile)
        writer.writerow(['Thumb', 'Index', 'Middle', 'Ring', 'Little'])
        for s1, s2, s3, s4, s5 in zip(thumbResistance, indexResistance, middleResistance, ringResistance, littleResistance):
            writer.writerow([s1, s2, s3, s4, s5])

# Register the callback function for when the plot window is closed
fig, ax = plt.subplots()
fig.canvas.mpl_connect("close_event", on_close)

ani = FuncAnimation(fig, update_plot, interval=10, cache_frame_data=False)
plt.show()
