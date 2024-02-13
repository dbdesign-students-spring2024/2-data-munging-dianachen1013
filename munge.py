# Place code below to do the munging part of this assignment.
import os

def clean_data(file_name_to_clean, file_name_output):
    # Use a relative path to the 'data' directory, ensuring compatibility across different OS
    data_folder = 'data'  # Relative path to the data directory from the script's location
    input_file_path = os.path.join(data_folder, file_name_to_clean)
    output_file_path = os.path.join(data_folder, file_name_output)
    
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    cleaned_data = ["Year,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec,J-D,D-N,DJF,MAM,JJA,SON,Year"]

    for line in lines:
        if line.strip() and not line.startswith("Year") and not line.startswith(" Divide") and not line.startswith(" Multiply"):
            parts = line.split()
            if len(parts) == 20:  
                year = parts[0]
                temp_values = parts[1:19]
                final_year = parts[19]
                cleaned_values = [year]

                for value in temp_values:
                    if value == "***":  # Handle missing data with 'NaN'
                        cleaned_values.append("NaN")
                    else:
                        try:
                            # Convert from 0.01 degrees Celsius to Fahrenheit and format to one decimal place
                            fahrenheit = (int(value) / 100) * 1.8
                            cleaned_values.append(f"{fahrenheit:.1f}")
                        except ValueError:
                            cleaned_values.append("NaN")

                cleaned_values.append(final_year)
                cleaned_data.append(",".join(cleaned_values))

    with open(output_file_path, 'w') as output_file:
        for line in cleaned_data:
            output_file.write(line + "\n")

# File names for input and output
file_name_to_clean = 'GLB.Ts+dSST.txt'
file_name_output = 'clean_data.csv'

# Execute the function with file names, ensuring the paths are constructed in a platform-agnostic way
clean_data(file_name_to_clean, file_name_output)
