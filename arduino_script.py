import csv

# Step 1: Read CSV Data
csv_file_path = "C:\\Users\\mikae\\Downloads\\netron inference-20230812T013749Z-001\\netron inference\\edm_spiketrains_data.csv"

data_matrix = []

with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        # Convert each row from string to integer
        int_row = [int(float(item)) for item in row]
        data_matrix.append(int_row)

# Step 2: Convert to PROGMEM-Compatible C++ Code
array_name = "edm_data"
header = f"const int {array_name}[3000][78] PROGMEM = {{\n"
footer = "};\n"

# Convert data matrix to string with proper formatting
data_str = ",\n".join(["{" + ",".join(map(str, row)) + "}" for row in data_matrix])

# Combine header, data, and footer
arduino_code = header + data_str + footer

# Optionally save to a .h or .cpp file for inclusion in an Arduino project
with open("edm_spiketrains_data_arduino.h", 'w') as f:
    f.write(arduino_code)

print("Conversion done! You can now include edm_spiketrains_data_arduino.h in your Arduino project.")
