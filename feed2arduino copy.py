import serial
import time
import csv

# Serial setup
ser = serial.Serial('COM3', 9600)  # Change 'COM3' to your Arduino's COM port
time.sleep(2)  # wait for the serial connection to initialize

csv_file_path = "C:/Users/mikae/Downloads/netron inference-20230812T013749Z-001/netron inference/edm_spiketrains_data.csv"

with open(csv_file_path, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        for item in row:
            # Assume each item in your CSV is either '1' or '0'
            ser.write(item.encode())  # Send the byte to Arduino
            time.sleep(0.01)  # Optional delay between each byte
        ser.write('E'.encode())  # Send an 'E' after finishing each row
        time.sleep(0.01)  # Optional delay
