# Place code below to do the munging part of this assignment.
import os
def clean_data(file_path_to_clean, file_path_output):
    input_file_path = os.path.join('data', file_name_to_clean)
    output_file_path = os.path.join('data', file_name_output)
    with open(file_path_to_clean, 'r') as file:
        lines = file.readlines()

    # Define the header for the cleaned CSV file
    cleaned_data = ["Year,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec,J-D,D-N,DJF,MAM,JJA,SON,Year"]

    for line in lines:
        # Exclude non-data lines based on specific keywords
        if line.strip() and not line.startswith("Year") and not line.startswith(" Divide") and not line.startswith(" Multiply"):
            parts = line.split()
            # Ensure the line has the correct number of elements
            if len(parts) == 20:  
                year = parts[0]  # First column is the year
                temp_values = parts[1:19]  # Monthly temperature values
                final_year = parts[19]  # Last column is also the year
                cleaned_values = [year]

                # Process and convert temperature and metadata values
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

                # Append the repeated year without conversion
                cleaned_values.append(final_year)  
                # Add the processed line to the cleaned data
                cleaned_data.append(",".join(cleaned_values))

    # Write the cleaned and fully converted data to the output CSV file
    with open(output_file_path, 'w') as output_file:
        for line in cleaned_data:
            output_file.write(line + "\n")

# Specify the input and output file paths
file_name_to_clean = 'GLB.Ts+dSST.txt'
file_name_output = 'clean_data.csv'

# Execute the data cleaning and conversion function
clean_data(input_file_path, output_file_path)
