# Place code below to do the analysis part of the assignment.
import csv

def analyze_temperature_data(csv_file_path):
    # Initialize data structures for storing the data
    difference_by_decade = {}
    seasonal_difference_by_decade = {season: {} for season in ['DJF', 'MAM', 'JJA', 'SON']}
    
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            year = int(row['Year'])
            if year < 1881 or year > 2020:  
                continue
            decade = ((year - 1) // 10) * 10 + 1  # Adjust decade grouping
            
            # Aggregate anomalies for overall and seasonal analysis
            for season in ['DJF', 'MAM', 'JJA', 'SON']:
                dif = row[season]
                if dif != 'NaN':
                    dif = float(dif)
                    if decade not in difference_by_decade:
                        difference_by_decade[decade] = []
                    difference_by_decade[decade].append(dif)
                    
                    if decade not in seasonal_difference_by_decade[season]:
                        seasonal_difference_by_decade[season][decade] = []
                    seasonal_difference_by_decade[season][decade].append(dif)
    
    # Calculate and print the average difference for each decade and season
    print("Average Temperature Difference by Decade (°F):")
    for decade in sorted(difference_by_decade.keys()):
        avg_dif = sum(difference_by_decade[decade]) / len(difference_by_decade[decade])
        print(f"{decade}s: {avg_dif:.2f}")
        
    print("\nSeasonal Averages by Decade:")
    for season in ['DJF', 'MAM', 'JJA', 'SON']:
        print(f"\nSeason: {season}")
        for decade in sorted(seasonal_difference_by_decade[season].keys()):
            avg_dif = sum(seasonal_difference_by_decade[season][decade]) / len(seasonal_difference_by_decade[season][decade])
            print(f"  {decade}s: {avg_dif:.2f}")

# Specify the path to your CSV file
csv_file_path = 'C:\\Users\\86136\\Desktop\\Database\\新建文件夹\\2-data-munging-dianachen1013\\data\\clean_data.csv'
analyze_temperature_data(csv_file_path)

