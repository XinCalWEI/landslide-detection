import pandas as pd
import yaml
import csv

# Step 1: Fix unclosed quotes in the CSV file and overwrite the original file
def fix_unclosed_quotes(input_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        rows = []
        for row in reader:
            # Fix unclosed quotes by manually handling quotes in each field
            cleaned_row = [field.replace('"', '') if field.count('"') % 2 != 0 else field for field in row]
            rows.append(cleaned_row)

    # Overwrite the original CSV file with the cleaned data
    with open(input_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)

    print(f"Fixed CSV saved as {input_file}")

# Step 2: Read the cleaned CSV file into a pandas DataFrame and convert to YAML
def convert_csv_to_yaml(input_csv, output_yaml):
    # Fix unclosed quotes first
    fix_unclosed_quotes(input_csv)

    # Read the cleaned CSV into pandas DataFrame
    df = pd.read_csv(input_csv)

    # Function to convert each row into a dictionary
    def convert_to_yaml(row):
        return {
            'title': row['Title'],
            'description': row['Notes/Description'],
            'linkDownload': row['Link for Others to Download'],
            'linkPaper': row['Link to a Paper that Uses This Dataset'],
            'numLandslideRecords': row['Number of Landslide Records'],
            'datasetDetails': row['Specific Details About the Dataset'],
            'inventoryType': row['Landslide Inventory Type'],
            'modelsUsed': row['Model(s) Used'],
            'dataResolution': row['Data Resolution'],
            'inputModel': row['Input of Model'],
            'outputModel': row['Output of Model'],
            'otherInfo': row['Other Information About the Dataset'],
            'country': row['Country'],
            'paperInfo': row['Other Information About the Paper'],
            'coordX': row['CoordinatesX'],
            'coordY': row['CoordinatesY'],
        }

    # Convert each row of the dataframe to a dictionary
    datasets = df.apply(convert_to_yaml, axis=1).tolist()

    # Write to a YAML file
    with open(output_yaml, 'w') as yaml_file:
        yaml.dump(datasets, yaml_file, default_flow_style=False)

    print(f"YAML file saved as {output_yaml}")

# Example usage
convert_csv_to_yaml('datasets.csv', 'dataset.yml')
