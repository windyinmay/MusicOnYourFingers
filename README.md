# SmartGlove Music Interaction System

## Overview

This repository contains the source code for a SmartGlove Music Interaction System. The project integrates Arduino, machine learning, and Python to create a wearable glove that recognizes gestures and produces musical notes.

## Repository Structure

- **Arduino:**
  - `FingerSensorsRead.ino`: Arduino code to collect resistance values of 5 sensors on 5 fingers for training data.
  - `PianoPlay.ino`: Arduino code to collect resistance values and send them to the Python file for prediction and play the Piezo Speaker corresponding to which finger is bent.

- **Datasets:**
  - `training_dataset.csv`: CSV file containing the labeled training dataset for machine learning.
  - `testing_dataset.csv`: CSV file containing the data was colleted with different hand sizes of testers in real-time during the testing phrase.  

- **MachineLearning:**
  - `training_data_collector.py`: Python code for connecting to pySerial, sending data that collected from Arduino to Python to write CSV files - training_dataset.csv.
  - `training.py`: Python code for training the machine learning model to recognize bent fingers based on the labeled CSV file.
  - `predicting.py`: Python code for predicting which finger is bent based on the model and data collected from Arduino and sending the result back to Arduino for real-time music generation.

## Usage

For better understanding and implementation, it is recommended to read section 4 - Software Design in the report below:

Report shared link: [Final report of this project](https://www.overleaf.com/read/wyssykfwqxpj#e9779f) or URL: <https://www.overleaf.com/read/wyssykfwqxpj#e9779f>

## Dependencies

- Arduino IDE
- Python 3.x
- Required Python packages (specified in `python files`)

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. I welcome any improvements on recognition accuracy! So far, the accuracy of the machine learning model is more than 95% with the sample size is more than 7,000.